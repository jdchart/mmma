"""
06 Numpy processing.

MMMMA provides some simple numpy array processing for performing traditional ML-related pre-processing
tasks such as converting audio to mono, converting images to greyscale etc.
"""

import mmma
import utils
import os

# Import the numpy processing package:
import mmma.npproc as nproc

# Get some media files:
video_files = utils.test_media("video")
audio_files = utils.test_media("audio")
image_files = utils.test_media("image")

# Create a corpus from a file:
video_file = mmma.Corpus(render_path = video_files[0])
audio_file = mmma.Corpus(render_path = audio_files[0])
image_file = mmma.Corpus(render_path = image_files[0])

# Get the numpy arrays of the media files:
np_array_audio = audio_file.to_np()
np_array_image = image_file.to_np()
# np_array_video, np_array_video_audio, audio_rate = video_file.to_np(video = True, audio = True)

# Create a folder to export the renders:
output_dir = utils.create_output_folder()

# Convert an image to greyscale:
greyscale_image = nproc.to_greyscale(np_array_image)
# greyscale_video = nproc.to_greyscale(np_array_video)

# See what they look like:
nproc.render(os.path.join(output_dir, "GREY_IMG.png"), greyscale_image)
# nproc.render(os.path.join(output_dir, "GREY_VIDEO.mp4"), greyscale_video)

# Resize an image:
small_image = nproc.resize(np_array_image, 50, 50)
nproc.render(os.path.join(output_dir, "SMALL_IMG.png"), small_image)
big_image = nproc.resize(np_array_image, 1000, 100)
nproc.render(os.path.join(output_dir, "BIG_IMG.png"), big_image)

# Or a video:
# small_video = nproc.resize(np_array_video, 50, 50)
# nproc.render(os.path.join(output_dir, "SMALL_IMG.png"), small_video)
# big_video = nproc.resize(np_array_video, 1000, 100)
# nproc.render(os.path.join(output_dir, "BIG_IMG.png"), big_video)

# There's also zoom


# RESAMPLE

# MONO