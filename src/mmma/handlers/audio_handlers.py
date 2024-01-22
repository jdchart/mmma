import audiofile
#import scipy

class AudioHandler:
    def __init__(self, media_object) -> None:
        self.media_object = media_object
        self.duration = None
        self.frames = None
        self.channels = None
        self.sample_rate = None
        self.bit_depth = None

        # self.start_frame = kwargs.get("start_frame", 0)
        # self.end_frame = kwargs.get("start_frame", -1)

    def decode(self):
        """Get basic info about media file."""

        self.duration = audiofile.duration(self.media_object.media_path) * 1000
        self.frames = audiofile.samples(self.media_object.media_path)
        self.channels = audiofile.channels(self.media_object.media_path)
        self.sample_rate = audiofile.sampling_rate(self.media_object.media_path)
        self.bit_depth = audiofile.bit_depth(self.media_object.media_path)

    def get_frame(self):
        """Return an fft frame, or not... this should return a media type"""
        #scipy.fft()
        pass

class WAVHandler(AudioHandler):
    def __init__(self, media_object) -> None:
        super().__init__(media_object)

def get_audio_handler(ext : str, media_object) -> AudioHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "wav":
        return WAVHandler(media_object)
    elif ext == "mpg":
        pass