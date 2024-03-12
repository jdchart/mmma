import audiofile
import numpy as np
import scipy
import os
from .utils import update_time_from_region, decode_region

class AudioHandler:
    def __init__(self, corpus) -> None:
        """
        Base class for all audio handlers.

        attributes
        ----------
        - duration_ms : float. Duration in milliseconds.
        - frames : int. Number of audio frames.
        - channels : int. Number of audio channels.
        - frame_rate : float. Number of samples/second.
        - bit_depth : int. Number of bits used to describe each frame.
        """

        # Associated Corpus object:
        self.corpus = corpus
        
        # Audio attributes:
        self.duration_ms = None
        self._full_duration_ms = None
        self.frames = None
        self._full_frames = None
        self.channels = None
        self.frame_rate = None
        self.bit_depth = None

        self.media_type = "Audio"

    def decode(self):
        """Get basic info about media file."""

        self._full_duration_ms = audiofile.duration(self.corpus.render_path) * 1000
        self._full_frames = audiofile.samples(self.corpus.render_path)
        self.channels = audiofile.channels(self.corpus.render_path)
        self.frame_rate = audiofile.sampling_rate(self.corpus.render_path)
        self.bit_depth = audiofile.bit_depth(self.corpus.render_path)

        update_time_from_region(self)

    def render(self, data, path):
        """Render the audio file to a new wav file at path."""
        if os.path.splitext(path)[1] == ".wav":
            scipy.io.wavfile.write(path, self.frame_rate, data)
            return path
        else:
            print("Unable to render, must render to wav format.")
            return None
        
class WAVHandler(AudioHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

    def to_np(self, region) -> np.array:
        """Serve the wav file as a numpy array."""
        
        rate, data = scipy.io.wavfile.read(self.corpus.render_path)
        
        region_decode = decode_region(region, self.corpus)
        if region_decode["start"] == -1:
            region_decode["start"] = 0
        if region_decode["end"] == -1:
            region_decode["end"] = self._full_frames

        if len(data) == 1:
            data = data.reshape(-1, 1)
        
        return data[region_decode["start"]:region_decode["end"]]

def get_audio_handler(ext : str, corpus) -> AudioHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "wav":
        return WAVHandler(corpus)
    elif ext == "mpg":
        pass