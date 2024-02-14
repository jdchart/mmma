"""
02 Annotations and annotation lists.

A Corpus can be described with Annotations.
An Annotation pertains to a specific region of the Corpus, and is not to be confised with metadata.
An annotation can also be added to an AnnotationList.
"""

import mmma
import utils

# Get some media files:
video_files = utils.test_media("video")

# Create a corpus from a file:
video_file = mmma.Corpus(render_path = video_files[0])

# Create an annotation spanning the first 2 seconds of the video file:
my_annotation = video_file.add_annotation(region = {"start" : 0, "end" : 2000})

# Change the time unit (it was by defualt "ms", this will make,the region span from 0-2000 frames):
my_annotation.region.time_unit = "frames"

# You can also create lists of annotations. Note that an annotation is attached to a specific target corpus,
# but an annotation list is not (meaning that annotations from different corpora can be in the same list.
# First, create the annotation list:
my_annotation_list = mmma.AnnotationList()

# Then append the annotatio to the list:
my_annotation_list.append_annotation(my_annotation)
print(my_annotation_list.to_dict())