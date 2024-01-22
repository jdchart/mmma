import cv2

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
        self.dimensions = None
        self.duration_ms = None
        self.frames = None
        self.frame_rate = None

    def decode(self):
        """Get basic info about media file."""

        cap = cv2.VideoCapture(self.corpus.render_path)
        self.dimensions = {"width" : int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), "height" : int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}
        self.frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_rate = cap.get(cv2.CAP_PROP_FPS)
        self.duration_ms = (self.frames / self.frame_rate) * 1000

class MP4Handler(VideoHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

def get_video_handler(ext : str, corpus) -> VideoHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "mp4":
        return MP4Handler(corpus)
    elif ext == "mpg":
        pass