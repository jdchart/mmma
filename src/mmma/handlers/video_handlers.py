import cv2
from .utils import update_time_from_region, update_space_from_region

class VideoHandler:
    def __init__(self, corpus) -> None:
        """
        Base class for all video handlers.

        attributes
        ----------
        - dimensions : dict. Video size in pixels {width : int, height : int}.
        - duration_ms : float. Duration in milliseconds.
        - frames : int. Number of audio frames.
        - frame_rate : float. Number of samples/second.
        """

        # Associated Corpus object:
        self.corpus = corpus
        
        # Video attributes:
        self._full_dimensions = None
        self.dimensions = None
        self._full_duration_ms = None
        self.duration_ms = None
        self._full_frames = None
        self.frames = None
        self.frame_rate = None

    def decode(self):
        """Get basic info about media file."""

        cap = cv2.VideoCapture(self.corpus.render_path)
        self._full_dimensions = {"width" : int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), "height" : int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}
        self._full_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_rate = cap.get(cv2.CAP_PROP_FPS)
        self._full_duration_ms = (self._full_frames / self.frame_rate) * 1000

        update_space_from_region(self)
        update_time_from_region(self)

class MP4Handler(VideoHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

def get_video_handler(ext : str, corpus) -> VideoHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "mp4":
        return MP4Handler(corpus)
    elif ext == "mpg":
        pass