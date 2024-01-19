class VideoHandler:
    def __init__(self, media_object) -> None:
        self.media_object = media_object
        self.dims = None
        self.duration = None
        self.frames = None

    def decode(self):
        print("decoding...")

    def get_frame(self):
        """Return frame as an image media object."""
        pass

    def get_audio(self):
        """Return audio as an ausio media object."""





class MP4Handler(VideoHandler):
    def __init__(self, media_object) -> None:
        super().__init__(media_object)

def get_video_handler(ext : str, media_object) -> VideoHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "mp4":
        return MP4Handler(media_object)
    elif ext == "mpg":
        pass