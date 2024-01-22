"""
02 Annotations and annotation lists.

A Corpus can be described with Annotations.
An Annotation pertains to a specific region of the Corpus, and is not to be confised with metadata.
An annotation can also be added to an AnnotationList.
"""

import mmma
import utils

# Get some media files:
audio_files = utils.test_media("audio")

# Create a corpus from a file:
audio_file = mmma.Corpus(render_path = audio_files[0])

# Create an annotation spanning the first 2 seconds of the audio file:
my_annotation = audio_file.add_annotation(region = {"start" : {"value" : 0, "unit" : "ms"}})


print(my_annotation.target.render_path)
print(my_annotation.region.start)