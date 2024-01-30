"""
06 Serving.

Use the to_np() method to serve a corpus that has an associated media file as a numpy array.
"""

import mmma
import utils
import os

# Get some media files:
video_files = utils.test_media("video")
audio_files = utils.test_media("audio")
image_files = utils.test_media("image")

# Create a corpus from a file:
video_file = mmma.Corpus(render_path = video_files[1])
audio_file = mmma.Corpus(render_path = audio_files[0])
image_file = mmma.Corpus(render_path = image_files[0])

# Use the to_np() method to get the numpy array:
np_array_audio = audio_file.to_np()
np_array_image = image_file.to_np()
np_array_video, np_array_video_audio = video_file.to_np(video = True, audio = True)

print(f"Video (frames): {np_array_video.shape} ({np_array_video.dtype})")
print(f"Video (audio): {np_array_video_audio.shape} ({np_array_video_audio.dtype})")
print(f"Audio: {np_array_audio.shape} ({np_array_audio.dtype})")
print(f"Image: {np_array_image.shape} ({np_array_image.dtype})")