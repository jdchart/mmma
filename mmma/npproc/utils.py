import scipy.signal
from scipy.ndimage import zoom as scipy_zoom
from .render import to_wav, to_png, to_mp4
import numpy as np

def render(path : str, np_array, **kwargs):
    """Convert the numpy array to a media file."""
    if isinstance(np_array, dict):
        # Video or video + audio or audio dict:
        to_mp4(np_array, path)
    else:
        if len(np_array.shape) == 2:
            # AUDIO:
            to_wav(path, np_array, kwargs.get("frame_rate"))
        elif len(np_array.shape) == 3:
            # IMAGE:
            to_png(path, np_array)
        elif len(np_array.shape) == 4:
            # VIDEO:
            to_mp4(np_array, path)

def to_mono(np_array : np.array) -> np.array:
    """
    Take the mean of a multi-channel numpy array and compress to one channel.
    
    This can be used to convert multichannel audio to mono, or colour images to greyscale.
    """
    
    mono = np.mean(np_array, axis=1)
    
    #clipped_mono = np.clip(mono, -1.0, 1.0)

    int16__scale = np.int16(np_array / np.max(np.abs(np_array)) * 32767)

    mono_2d = int16__scale.reshape(-1, 1)



    return mono_2d

def normalize(np_array : np.array) -> np.array:
    normalized = np_array / np.max(np.abs(np_array), axis=0)
    return normalized

def to_greyscale(np_array : np.array, method = 1) -> np.array:
    """
    Convert rgb to greyscale.

    method = 0 : take the mean of each channel.
    method = 1 : use the luminosity method.
    
    The luminosity method uses weights to estimate human perception of intensity
    using the following formula:
    Y=0.299⋅R+0.587⋅G+0.114⋅B
    """

    # if method == 1:
    #     greyscale = np.dot(np_array[..., :3], [0.299, 0.587, 0.114])
    # else:
    #     greyscale = np.mean(np_array[..., :3], axis=-1)

    if method == 1:
        greyscale = np.dot(np_array, [0.299, 0.587, 0.114])
    else:
        greyscale = np.mean(np_array, axis=-1)
    
    #return greyscale.reshape(np_array.shape[:-1])
    return greyscale[..., np.newaxis]

def resample(np_array : np.array, old_sr, new_sr) -> np.array:
    """Resample a numpy array ith a new sampe rate."""

    resampling_ratio = float(new_sr) / float(old_sr)
    new_num_samples = int(len(np_array) * resampling_ratio)
    resampled = scipy.signal.resample(np_array, new_num_samples)
    return resampled

def resize(np_array : np.array, width, height, order = 3) -> np.array:
    """
    Resize a given image or video numpy array, stretching or compressing the image accordingly.
    
    order=0: Nearest-neighbor interpolation. It assigns the value of the nearest pixel to the non-grid position.
    order=1: Bilinear interpolation. It uses linear interpolation along each axis independently.
    order=3: Cubic interpolation. It uses cubic splines to interpolate values.
    """

    height_scale_factor = height / np_array.shape[0]
    width_scale_factor = width / np_array.shape[1]
    
    if len(np_array.shape) == 3:
        return scipy_zoom(np_array, zoom=(height_scale_factor, width_scale_factor, 1), order=order)
    else:
        return scipy_zoom(np_array, zoom=(1, height_scale_factor, width_scale_factor, 1), order=order)

def zoom(np_array : np.array, zoom_factor, order = 3) -> np.array:
    """
    Zoom a given image or video numpy array, stretching or compressing the image accordingly.
    
    order=0: Nearest-neighbor interpolation. It assigns the value of the nearest pixel to the non-grid position.
    order=1: Bilinear interpolation. It uses linear interpolation along each axis independently.
    order=3: Cubic interpolation. It uses cubic splines to interpolate values.
    """

    height_scale_factor = zoom_factor
    width_scale_factor = zoom_factor

    if len(np_array.shape) == 3:
        return scipy_zoom(np_array, zoom=(height_scale_factor, width_scale_factor, 1), order=order)
    else:
        return scipy_zoom(np_array, zoom=(1, height_scale_factor, width_scale_factor, 1), order=order)