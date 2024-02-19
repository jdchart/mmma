import cv2
from .utils import update_space_from_region, decode_region
import numpy as np
import os
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

    def to_np(self, region):
        """Serve the associated image file as a numpy array."""

        image = cv2.imread(self.corpus.render_path)
        data = np.array(image)

        region_decode = decode_region(region, self.corpus)

        if region_decode["x"] == -1:
            region_decode["x"] = 0
        if region_decode["y"] == -1:
            region_decode["y"] = 0
        if region_decode["width"] == -1:
            region_decode["width"] = self.dimensions["width"]
        if region_decode["height"] == -1:
            region_decode["height"] = self.dimensions["height"]

        return data[region_decode["y"]:region_decode["y"] + region_decode["height"], region_decode["x"]:region_decode["x"] + region_decode["width"]]
    
    def render(self, data, path):
        """Render the image file to a new png file at path."""
        if os.path.splitext(path)[1] == ".png":
            cv2.imwrite(path, data)
            return path
        else:
            print("Unable to render, must render to png format.")
            return None

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