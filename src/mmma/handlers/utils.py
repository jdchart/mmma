import numpy as np

def ms_to_frames(ms, frame_rate):
    return int((frame_rate * ms) / 1000)

def frame_rate_convert(original_frames, original_fr, new_fr):
    """Take a value in a given frame rate, and convert to a new frame rate."""
    return int((original_frames * new_fr) / original_fr)

def frames_to_ms(frames, frame_rate):
    return (frames * 1000) / frame_rate

def decode_region(region, corpus) -> dict:
    """
    If possible, decode region to pixels and frames.
    
    TODO: This function strikes me as horrific, maybe a better way to do this? Used when serving to np.
    """
    
    ret = {"start" : -1, "end" : -1, "x" : -1, "y" : -1, "z" : -1, "width" : -1, "height" : -1, "depth" : -1, "path" : []}
    
    if region.start != None or region.end != None:
        if region.time_unit == "ms":
            if region.start != None:
                ret["start"] = ms_to_frames(region.start, corpus.frame_rate)
            if region.end != None:
                ret["end"] = ms_to_frames(region.end, corpus.frame_rate)
        elif region.time_unit == "frames":
            if region.start != None:
                ret["start"] = region.start
            if region.end != None:
                ret["end"] = region.end

    if region.x != None or region.y != None or region.z != None or region.width != None or region.height != None or region.depth != None:
        if region.space_unit == "px":
            if region.x != None:
                ret["x"] = region.x
            if region.y != None:
                ret["y"] = region.y
            if region.z != None:
                ret["z"] = region.z
            if region.width != None:
                ret["width"] = region.width
            if region.height != None:
                ret["height"] = region.height
            if region.depth != None:
                ret["depth"] = region.depth

    return ret
                
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
        height = handler._full_dimensions["height"]
        if handler.corpus.region.x != None:
            x = handler.corpus.region.x
        if handler.corpus.region.y != None:
            y = handler.corpus.region.y
        if handler.corpus.region.width != None:
            width = handler.corpus.region.width
        if handler.corpus.region.height != None:
            height = handler.corpus.region.height
        handler.dimensions = {"width" : width, "height" : height}
    else:
        handler.dimensions = handler._full_dimensions

# def trim_time_series_array(original_array, region, corpus) -> np.array:
#     """Trim a time series numpy array with a new start and end frame."""
#     if region.time_unit == "ms":
#         start_frame = 