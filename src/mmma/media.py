import os
from .mmma_element import MMMAElement
from .handlers import get_video_handler, get_audio_handler

class Media(MMMAElement):
    def __init__(self, media_path : str) -> None:
        """
        Representation of a media file and its data.

        
        """

        super().__init__()

        self.media_path = media_path
        self.type, self.ext = self._get_type(self.media_path)

        self.handler = self._get_handler(self.type, self.ext)

        self.handler.decode()

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
        # elif media_type == "Image":
        #     return_data = self._get_image_file_data(path, ext)
        # elif media_type == "Document":
        #     return_data = self._get_document_file_data(path, ext)