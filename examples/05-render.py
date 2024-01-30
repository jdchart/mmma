"""
05 Render.

Using annotations, you can decompose their target corpora to a new corpus according to the annotation's region.
"""

import mmma
import utils

# Get some media files:
video_files = utils.test_media("video")
audio_files = utils.test_media("audio")
image_files = utils.test_media("image")

# Create a corpus from a file:
video_file = mmma.Corpus(render_path = video_files[0])
audio_file = mmma.Corpus(render_path = audio_files[0])
image_file = mmma.Corpus(render_path = image_files[0])

# Create an annotation of the video file of one second:
video_annotation = video_file.add_annotation(region = {"start" : 1000, "end" : 2000})
