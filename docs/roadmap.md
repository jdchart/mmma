# Roadmap

## Version 0.1:
- [ ] Update docs
    - [ ] Usage examples for readme
    - [ ] Installation
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
    - [ ] Handlers
        - [ ] Get corpus from region
            - [ ] Audio -> audio
            - [ ] Video -> Video
            - [ ] Video -> audio
            - [ ] Video -> image
            - [ ] Image -> image
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
- [ ] Investigate the need for Annotations that would target other things than a Corpus.
- [ ] Better metadata system (reading from a data file etc.)
- [ ] Investigate layer regions
- [ ] Add functionality for a handler to target a region of the associated media file (?).
- [ ] Add support of media stocked online (corpora with a url render_path).
- [ ] Add routine for installing flucoma binaries.