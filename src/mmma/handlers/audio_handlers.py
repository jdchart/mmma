import audiofile

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
        self.frames = None
        self.channels = None
        self.frame_rate = None
        self.bit_depth = None

    def decode(self):
        """Get basic info about media file."""

        self.duration_ms = audiofile.duration(self.corpus.render_path) * 1000
        self.frames = audiofile.samples(self.corpus.render_path)
        self.channels = audiofile.channels(self.corpus.render_path)
        self.frame_rate = audiofile.sampling_rate(self.corpus.render_path)
        self.bit_depth = audiofile.bit_depth(self.corpus.render_path)

class WAVHandler(AudioHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

def get_audio_handler(ext : str, corpus) -> AudioHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "wav":
        return WAVHandler(corpus)
    elif ext == "mpg":
        pass