# Adding media formats

You can contribute by adding a new media type to the mmma ecosystem. To do this, you will need to assure that a certain number of requirements have been met.

## 1. Add to the accepted_media list

In [data](/src/mmma/data.py), add the new media format to the `accepted_media` dict. You will need to add an entry in the corresponding type list (Video, Image, Audio or Document) and provide the base extension (ext) and any aliases (for example `jpg` has the alias `jpeg`):

```json
{"ext" : "wav", "alias" : ["wave"]}
```

This example would be added to the `"Audio"` list.

## 2. Add a handler

