"""
01 Load a media file.

Media files get loaded into the Corpus() object.
Different types of media are treated in the same way (for example, audio and video files both have the duration_ms attribute).
"""

import mmma
import utils

# Get some media files:
audio_files = utils.test_media("audio")
video_files = utils.test_media("video")
image_files = utils.test_media("image")

# Load some of the files:
audio_file = mmma.Corpus(render_path = audio_files[0])
video_file = mmma.Corpus(render_path = video_files[0])
image_file = mmma.Corpus(render_path = image_files[0])

# Get basic info about the media file:
print(audio_file.duration_ms)
print(video_file.duration_ms)
print(image_file.dimensions)