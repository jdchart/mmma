# The different kinds of media files accepted by mmma:
accepted_media = {
    "Video" : [
        {"ext" : "mp4", "alias" : []},
        #{"ext" : "mpg", "alias" : []}
    ],
    "Audio" : [
        #{"ext" : "aif", "alias" : []},
        {"ext" : "wav", "alias" : ["wave"]}
        #{"ext" : "ogg", "alias" : []},
        #{"ext" : "mp3", "alias" : []}
    ],
    "Image" : [
        {"ext" : "png", "alias" : []},
        {"ext" : "jpg", "alias" : ["jpeg"]}
    ],
    "Document" : [
        {"ext" : "pdf", "alias" : []},
        {"ext" : "xml", "alias" : []},
        {"ext" : "mxl", "alias" : []},
        {"ext" : "mscx", "alias" : []},
        {"ext" : "mscz", "alias" : []},
    ]
}