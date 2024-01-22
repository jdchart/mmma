import cv2

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
        self.dimensions = None

    def decode(self):
        """Get basic info about media file."""

        openCVimg = cv2.imread(self.corpus.render_path, cv2.IMREAD_UNCHANGED)
        self.dimensions = {"width" : int(openCVimg.shape[1]), "height" : int(openCVimg.shape[0])}

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