import cv2
from .utils import update_space_from_region
import imageio.v3 as iio

class ImageHandler:
    def __init__(self, corpus) -> None:
        """
        Base class for all image handlers.

        attributes
        ----------
        - dimensions : dict. Image size in pixels {width : int, height : int}.
        """

        # Associated Corpus object:
        self.corpus = corpus
        
        # Image attributes:
        self._full_dimensions = None
        self.dimensions = None

    def decode(self):
        """Get basic info about media file."""

        openCVimg = cv2.imread(self.corpus.render_path, cv2.IMREAD_UNCHANGED)
        self._full_dimensions = {"width" : int(openCVimg.shape[1]), "height" : int(openCVimg.shape[0])}

        update_space_from_region(self)

    def to_np(self):
        """Serve the associated image file as a numpy array."""
        return iio.imread(self.corpus.render_path) # This should also work with urls.

class PNGHandler(ImageHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

class JPGHandler(ImageHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

def get_image_handler(ext : str, corpus) -> ImageHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "png":
        return PNGHandler(corpus)
    elif ext == "jpg":
        return JPGHandler(corpus)