# mmma
MultiModal Media Analysis


roadmap
3D

https://sweetcode.io/python-file-importation-multi-level-directory-modules-packages/
need to add routine for installing flucoma binaries


```python
import mmma


```

detections
intra annotations
    (duraiton  or dimension based)
    descriptions
    text detection
inter annotations


annotation (by position (time + dim/channels/spectra))
annotations series (only for audio and video)
    but what about overlapping fft analyses ?
    ok, but accomodate for overlaps when processing stats


an annotation is not a visualisation.
need to make that separation




decompositions
each time must be able to be returned as media
sound 
    layers -> new object
    slices -> same object but with update dfields or new object
    objects (series of layers) - spectral contour -> magnitude spectrograme (basis) + amplitude envelope -> new object
videos
    slices -> same object but with update dfields or new object
    region series
        - > can be exported for visualisation with compomises but given to analysis as region series.
image
    regions

descriptions
sound
    of sound file
video


sound analysis can 