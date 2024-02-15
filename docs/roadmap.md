# Roadmap

## Version 0.1:
- [ ] Update docs
    - [ ] Usage examples for readme
    - [x] Installation
    - [ ] Annotations and annotation lists
    - [ ] Analysis
    - [ ] List the minimum requirements for handlers
- [ ] Functionality
    - [ ] requirements.txt
    - [ ] AnnotationList:
        - [ ] Remove annotation
        - [ ] Inserting
        - [ ] Filtering
        - [ ] Reordering
        - [ ] Pretty printing
    - [ ] Corpus
        - [x] Corpora can have regions
            - [x] When updating a corpus's region, need to update corpus handler attributes
        - [ ] Render
    - [ ] Handlers
        - [x] Serve media
            - [x] Audio
            - [x] Video
            - [x] Image
        - [ ] Attributes
            - [ ] Video bit depth
            - [ ] Image bit depth
            - [ ] Image channels
            - [ ] Video channels
        - [ ] Get corpus from region (as regioned corpus and as new file)
            - [ ] Audio -> audio
            - [ ] Video -> Video
            - [ ] Video -> audio
            - [ ] Video -> image
            - [ ] Image -> image
        - [ ] Audio to mono routine.
        - [ ] Video to greyscale routine.
- [ ] Examples
    - [ ] Reading and writing
    - [ ] Analysis workflow (vosk example)
        - [ ] From video, get audio
        - [ ] Perfom analysis on audio
        - [ ] Create annotation list of words detected
        - [ ] MFCC of each slice.

## Supported media types
- [x] Image
- [x] Video
- [x] Audio
- [ ] Document
- [ ] 3D

## Various
- [ ] Add support for "document" file types.
- [ ] Supress output of ffmpeg
- [ ] For videos, allow for choosing between frames and framerate to correspond to video or audio
- [ ] Decompose audio frames.
- [ ] Investigate the need for Annotations that would target other things than a Corpus.
- [ ] Better metadata system (reading from a data file etc.)
- [ ] Investigate layer regions
- [ ] Space decomposition for cms
- [ ] Add functionality for a handler to target a region of the associated media file (?).
- [ ] Add support of media stocked online (corpora with a url render_path).
- [ ] Add routine for installing flucoma binaries.