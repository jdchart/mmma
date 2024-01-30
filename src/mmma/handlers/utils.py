def ms_to_frames(ms, frame_rate):
    return int((frame_rate * ms) / 1000)

def frames_to_ms(frames, frame_rate):
    return (frames * 1000) / frame_rate

def update_time_from_region(handler) -> None:
    """Update the public-facing duration_ms and frames according to region data."""
    if handler.corpus.region.time_unit == "ms":
        start = 0
        end = handler._full_duration_ms
        if handler.corpus.region.start != None:
            start = handler.corpus.region.start
        if handler.corpus.region.end != None:
            end = handler.corpus.region.end
        handler.duration_ms = end - start
        handler.frames = ms_to_frames(handler.duration_ms, handler.frame_rate)
    elif handler.corpus.region.time_unit == "frames":
        start = 0
        end = handler._full_frames
        if handler.corpus.region.start != None:
            start = handler.corpus.region.start
        if handler.corpus.region.end != None:
            end = handler.corpus.region.end
        handler.frames = end - start
        handler.duration_ms = frames_to_ms(handler.frames, handler.frame_rate)
    else:
        handler.frames = handler._full_frames
        handler.duration_ms = handler._full_duration_ms

def update_space_from_region(handler) -> None:
    """Update the public-facing dimensions according to region data."""
    
    if handler.corpus.region.space_unit == "px":
        x = 0
        y = 0
        width = handler._full_dimensions["width"]
        height = handler._full_dimensions["width"]
        if handler.corpus.region.x != None:
            x = handler.corpus.region.x
        if handler.corpus.region.x != None:
            y = handler.corpus.region.y
        if handler.corpus.region.x != None:
            width = handler.corpus.region.width
        if handler.corpus.region.x != None:
            height = handler.corpus.region.height
        handler.dimensions = {"width" : width, "height" : height}
    else:
        handler.dimensions = handler._full_dimensions