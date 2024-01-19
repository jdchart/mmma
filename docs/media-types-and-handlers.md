# Media types and handlers

With mmma, the idea is that the user can handle many different types of media, and the various formats within which they are encoded in one standardized way. For example, the process for obtaining the dimensions of a video file, or obtaining a frame from a video can vary depening on the format (mp4 or mov). With mmma, the user will use a same set of commands for treating different formats. Additionally, when this can be applied, same commands will be used to handle media of different types - for example getting the length of a video or audio file. mmma proposes a system for maintaing different file formats with **handlers**.

## Handlers

Every media file is represented with a base `Media()` class - this is the class that the user will use to load any media file. mmma derives the type of the media file into a set of different categories (`"Video"`, `"Image"`, `"Audio"`, `"Document"` etc.). Each of these types has a basic **handler** class (`VideoHandler()`, `ImageHandler()`, `AudioHandler()`, `DocumentHandler()` etc.). Each supported file format has it's own handler class that inherits from the basic file type handler class (for example `MP4Handler(VideoHandler)`).

Each basic handler has a certain number of _attributes_ (for example `duration`, `dims`, obtained from the `decode()` method) and a certain number of _methods_ (for example `get_frame()`). Each file type handler must allow for the retrieval of these attributes and the execution of these methods. Sometimes the base class method will suffice, however when adding new media formats, it may be necessary to wrtie a new method for the file type handler.

## Standardization

This means that a certain number of decisions have been made to allow for all file formats and media types to interact smoothly. For example, the decision was made for a frame of a video, and an image to always be served as a 3-channel numpy array. Decisions around standardization have been taken in the spirit of pythonic best practices and standards. 