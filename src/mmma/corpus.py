import os
from .mmma_element import MMMAElement
from .handlers import get_video_handler, get_audio_handler, get_image_handler
from .region import Region
from .annotation import Annotation

class Corpus(MMMAElement):
    def __init__(self, **kwargs) -> None:
        """
        Representation of a mmma Corpus.

        attributes
        ----------
        - render_path : str. Path or url to a rendered media file that represents the corpus.
        - render_type : str. The type of an associated media file ('Audio', 'Video' etc.).
        - render_ext : str. The extension of an associated media file ('mp4', 'jpg' etc.).
        - handler : Handler(). The handler object for the associated media file (depends on the file format, for example MP4Handler(), WAVHandler() etc.).
        - region : Region(). Associate a region with the corpus.
        """

        # Initialize MMMAElement class with corpus mmma_type:
        super().__init__(mmma_type = "Corpus")

        # If associated with a media file, get the path, type and extension:
        self.render_path = kwargs.get('render_path', None)
        self.render_type, self.render_ext = self._get_type(self.render_path)
        
        # Set a region for the object:
        if "region" in kwargs:
            self.region = Region(target = self, **kwargs.get("region"))
        else:
            self.region = Region(target = self)

        if self.render_path != None:
            # Set the cropus's handler:
            self.handler = self._get_handler(self.render_type, self.render_ext)
            if self.handler != None:
                # Decode media attributes:
                self.handler.decode()

    def add_annotation(self, **kwargs):
        """Create a new annotation object that targets the Corpus."""
        new_annotation = Annotation(target = self, region = Region(**kwargs.get("region", None)), props = kwargs.get("props", None))
        new_annotation.region.target = new_annotation
        return new_annotation
    
    def to_np(self, **kwargs):
        """Serve the associated media file as a numpy array."""
        return self.handler.to_np(self.region, **kwargs)

    def to_dict(self) -> dict:
        """Represent the corpus as a dict."""
        ret = super().to_dict()
        ret["region"] = self.region.to_dict()
        if self.render_path != None:
            ret["render_path"] = self.render_path
        if self.render_type != None:
            ret["render_type"] = self.render_type
        if self.render_ext != None:
            ret["render_ext"] = self.render_ext
        return ret

    def _get_type(self, path : str):
        """Determine the media file's type."""

        from .data import accepted_media

        if os.path.isfile(path):
            ext = os.path.splitext(path)[1][1:].lower()
            for media_type in accepted_media:
                for sub_type in accepted_media[media_type]:
                    if ext == sub_type["ext"] or ext in sub_type["alias"]:
                        return [media_type, sub_type["ext"]]
            print(f"Could not find an excepted media type for \"{path}\".")
            return [None, None]
        else:
            print(f"Cannot determine type of \".{path}\". the file does not exist.")

    def _get_handler(self, media_type : str, ext : str) -> dict:
        """Retrieve the handler object that corresponds to the media type and file format."""

        if media_type == "Video":
            return get_video_handler(ext, self) 
        elif media_type == "Audio":
            return get_audio_handler(ext, self)
        elif media_type == "Image":
            return get_image_handler(ext, self)
        elif media_type == "Document":
            # return get_document_handler(ext, self)
            return None
        else:
            return None
        
    def __getattr__(self, attr): 
        """Update get method in order to access handler attributes directly."""

        if attr not in self.__dict__ and self.handler and self.region != None:
            if attr in self.handler.__dict__:
                return getattr(self.handler, attr)
            else:
                print(f"Neither the Corpus nor its handler has the attribute \"{attr}\".")
                return None
        else:
            return self.__getattr__(attr) 