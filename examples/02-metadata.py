"""
02 Metadata.

Corpus, Annotation and AnnotationList objects can have metadata attributed to them.
"""

import mmma
import utils

# Get some media files:
audio_files = utils.test_media("audio")

# Create a corpus from a file:
audio_file = mmma.Corpus(render_path = audio_files[0])

# Set a value:
audio_file.set_metadata("title", "My audio file")
print(audio_file.metadata.title)