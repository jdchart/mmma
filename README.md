# mmma
_MultiModal Media Analysis_

MMMA offers a format-agnostic environment for multimodal media analysis. Not to be confused with [MMA](https://en.wikipedia.org/wiki/Mixed_martial_arts).

1. [Installation](#installation)
2. [Basic usage](#basic-usage)
3. [Theoretical premise](#theoretical-premise)
4. [Technical premise](#technical-premise)

Consult the [docs](/docs/) for the project [roadmap](/docs/roadmap.md), guides for [contributing](/docs/contributing.md) etc.

## Installation
Coming soon...

## Basic usage

```python
import mmma
```

## Theoretical premise

### Corpora
MMMA is built upon that idea that all media object (and most transparently _multimedia_ objects) are **composed objects**, or said plainly: **all media is multimodal**. Here are some examples:

- A **video** is a composed of a series of images and audio.
- A **sound** is composed of smaller slices of sounds.
- An **image** is composed of pixels or groups of pixels, which themselves can be considered images.
- A **document** is a hierarchichal sturcture of media objects. When rendered, it is composed of regions of images (some of these regions are decoded by a human as words).

Therefore, the basic object that the user manipulates is a **Corpus**. A corpus is composed of other corpora. The user does not always need to conceptually deal with the various elements of a corpus - they may think of a video as being a single object. But under the hood, MMMA deals with a video file as a multimoda corpus of audio and images (themselves composed corpora).

A corpus can organize its constitutive objects in various ways. Here are some examples:

- A video corpus organises its images and its audio in time. 
- An audio corpus can be thought of as organizing other audio file not only in time, but as superposed layers (as is revealed through analysis processes such as source separation). 

Video files, audio files, image files and document files are corpora that organize their constitutive objects in a standardized manner - they are constructions that follow a set of norms, they are [_capta_](https://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html).

However, other forms of corpus can exist. This is where we return to a more traditional definition of a corpus as a collection of disperate documents. The same _grouping_ mechnisms are at play, it is the _organizational_ mechanisms that are different. Here are some examples:

- Some corpora may organize their constitutive objects in time, but according to a "date of creation".
- Some corpora may organize their constitutive object in a space, for example "place of creation".
- Some corpora may have no organizational mechnism at all, or use a mix of several vectors.

The corpus gives its constitutive objects **context**, it is the space (spatial, temporal, conceptual) within which its objects exist. A video file gives a duration and a space within which images and sound are organized. A conceptual corpus groups objects by vertue of their origin or their meaning, or perhaps across a time span like a century, a place like a town or a country.

### Metadata and annotations.
A corpus can be described in a number of ways. In MMMA, we draw a difference between **metadata** and **annotations**.

**Metadata** are global descriptions that pertain to the corpus at a global level. Here are some examples: name, date of creation, description, author etc. In constrast to annotations, metadata does not point to a specific **region** in the corpus. 

In MMMA, every `Corpus` can be given any number of metadata (there is no default, but we recommend using a system such as [Dublin Core](https://www.dublincore.org/)). However, metadata can also be given to `Annotation`s and `AnnotationList`s.

**Annotations** target a specific `Corpus`, and a specific **region** of the corpus (be is spatial, temporal or conceptual). An annotation is simply considered to be a supplementary information regarding the given region, however it can be a composed object (in MMMA, like metadata, there is no limit to the properties that can be given to an annotation). Here are some examples:

- Colorimetric data of the region of an image.
- A word that is dictated at a specific moment of audio.
- Biographic elements of a person represented at a specific region and specific time in a video.

In MMMA, annotations are grouped together into lists, allowing the user to perform operations of groupings of annotations, such as filtered selections, visualizations etc.

## Technical premise

![MMMA Architecture](/docs/mmma%20architechture.jpg "MMMA Architecture")

### Corpora and handlers
MMMA is an environment for the analysis of different types of media files.

The most basic operation is the load a media file. All media files are represented by the `Corpus` class, irrespective of file type. When representing a media file, a `Corpus` has two major attributes: `render_path` (the file path or url pointing to the media) and `handler`.

The handler is an instance of the `Handler` class. Upon creation, the `Corpus` class will detect what type of media file is being loaded, and attribute the corresponding `Handler` subclass. For example, when loading a _.wav_ file, MMMA will attribute it the `WAVHandler` class, which is a subclass of `AudioHandler`, which is a subclass of `Handler`. In another instance, we may load an _.mp3_ file, which will be attributed the `MP3Handler` handler, which is again a subclass of `AudioHandler` and `Handler`.

Each handler needs to provide a basic set of functions and attributes that vary according to its type - for example all video handlers must have the function `get_frame(idx)` which must always return a corpus object that is the image of that frame, all video and audio handlers must have an attribute called `duration_ms` which give the length of the file in milliseconds. A list of obligatory functions and attributes can be found in the [contributing](/docs/contributing.md) section.

This means that, whether the user is using a _.wav_ or _/mp3_ file, the user will always interact with the same `Corpus` class. Further still, whether they are manipulating a video or audio file, to get the length they will always use `Corpus().duration_ms`. MMMA is designed to be extensible - we provide a large number of handlers for basic media formats, but we encourage [constribution](/docs/contributing.md) to add other formats.

### Annotations and annotation lists
Coming soon...
annotaitons are seperate things, but have a target (get target from annotation but not vice versa)
annotation lists are not attached to anything (can have multiple targets)

### Analysis
Coming soon...