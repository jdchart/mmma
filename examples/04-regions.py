"""
04 Regions.

Regions can be applied to both corpora and annotations.
"""

import mmma
import utils

# Get some media files:
video_files = utils.test_media("video")
audio_files = utils.test_media("audio")
image_files = utils.test_media("image")

# Create a corpus from a file, and set a region.
# Note that when you don't specify par tof the region, mmma defaults to the orginal file's value.
# for example, here we set the region from 1 second to the end of the file:
video_file = mmma.Corpus(render_path = video_files[0], region = {"start" : 1000})

# Here we set the region to be the first 2 seconds:
audio_file = mmma.Corpus(render_path = audio_files[0], region = {"end" : 2000})

# Here we set the spatial region (this can be applied to videos also):
image_file = mmma.Corpus(render_path = image_files[0], region = {"x" : 0, "y" : 0, "width" : 50, "height" : 50})

# Note the durations which are different to the orginal file:
print(video_file.duration_ms)
print(audio_file.duration_ms)

# Update the region like this:
audio_file.region.end = 3000
print(audio_file.duration_ms)