# Handler minimum requirements.

## Serving
A handler must be able to serve a media file as a numpy array using the `to_np()` method.

### Video
Must serve a np array containign video frames of shape (frames, height, width, channels) and a numpy array of audio of shape (frames, channels).

### Audio
Must serve a np array of shape (frames, channels).

### Image
Must serve a np array of shape (height, width, channels).