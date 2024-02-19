"""
05 Render.

You can render the region of a corpus to a media file (either from the Corpus's region or an Annotation's region).
"""

import mmma
import utils
import os

# Get some media files:
video_files = utils.test_media("video")
audio_files = utils.test_media("audio")
image_files = utils.test_media("image")

# Create a corpus from a file:
#video_file = mmma.Corpus(render_path = video_files[0])
video_file = mmma.Corpus(render_path = "/Users/jacob/Documents/Repos/mmma/test-corpora/videos/video_and_sound.mp4", region = {"x" : 50, "y" : 50, "width" : 50, "end" : 1000})
audio_file = mmma.Corpus(render_path = audio_files[0])
image_file = mmma.Corpus(render_path = image_files[0])

# Create a folder to export the renders:
output_dir = utils.create_output_folder()

# Render from the Corpus's region using the render() function.
video_file.render(os.path.join(output_dir, "video_output.mp4"), video = True, audio = True)
audio_file.render(os.path.join(output_dir, "audio_output.wav"))
image_file.render(os.path.join(output_dir, "image_output.png"))