import cv2
import os
import scipy
import shutil
import subprocess
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip
from .utils import update_time_from_region, update_space_from_region, decode_region, frame_rate_convert, write_video

class VideoHandler:
    def __init__(self, corpus) -> None:
        """
        Base class for all video handlers.

        attributes
        ----------
        - dimensions : dict. Video size in pixels {width : int, height : int}.
        - duration_ms : float. Duration in milliseconds.
        - frames : int. Number of audio frames.
        - frame_rate : float. Number of samples/second.
        """

        # Associated Corpus object:
        self.corpus = corpus
        
        # Video attributes:
        self._full_dimensions = None
        self.dimensions = None
        self._full_duration_ms = None
        self.duration_ms = None
        self._full_frames = None
        self.frames = None
        self.frame_rate = None

        self.media_type = "Video"

    def decode(self):
        """Get basic info about media file."""

        cap = cv2.VideoCapture(self.corpus.render_path)
        self._full_dimensions = {"width" : int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), "height" : int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}
        self._full_frames = self.get_num_frames()
        self.frame_rate = cap.get(cv2.CAP_PROP_FPS)
        self._full_duration_ms = (self._full_frames / self.frame_rate) * 1000

        # TODO : Add cap.release() ?

        update_space_from_region(self)
        update_time_from_region(self)

    def get_num_frames(self) -> int:
        """
        Return the number of frames in a video.

        The reason this is used and not int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), is beacuse
        CAP_PROP_FRAME_COUNT appears to be giving incorrect values.
        This appears to be a known issue : https://stackoverflow.com/questions/31472155/python-opencv-cv2-cv-cv-cap-prop-frame-count-get-wrong-numbers
        The problem is that this method is very slow. TODO : imprve this method!
        """

        cap = cv2.VideoCapture(self.corpus.render_path)

        fc = 0
        ret = True
        while ret:
            ret, frame = cap.read()
            if ret:
                fc = fc + 1

        cap.release()
        return fc

    def to_np(self, region, **kwargs):
        """Serve the associated media file as a numpy array."""
        
        # TODO : This can be optimised by just doing the region:
        if kwargs.get("video", True):
            cap = cv2.VideoCapture(self.corpus.render_path)

            buffer = np.empty((self._full_frames, self._full_dimensions["height"], self._full_dimensions["width"], 3), np.dtype('uint8'))

            fc = 0
            ret = True
            while fc < self._full_frames and ret:
                ret, buffer[fc] = cap.read()
                fc = fc + 1

            cap.release()

        if kwargs.get("audio", False):
            # TODO : There must surely be a way to do this without creating a temporary file...
            temp_audio_path = os.path.join(os.getcwd(), "temp", "temp_audio_out.wav")
            if os.path.isdir(os.path.dirname(temp_audio_path)) == False:
                os.makedirs(os.path.dirname(temp_audio_path))
            self.extract_audio(temp_audio_path)
            if os.path.isfile(temp_audio_path):
                audio_rate, audio_data = scipy.io.wavfile.read(temp_audio_path)
                shutil.rmtree(os.path.dirname(temp_audio_path))
            else:
                audio_data = np.array([])
        
        region_decode = decode_region(region, self.corpus)
        if region_decode["start"] == -1:
            region_decode["start"] = 0
        if region_decode["end"] == -1:
            region_decode["end"] = self._full_frames
        if region_decode["x"] == -1:
            region_decode["x"] = 0
        if region_decode["y"] == -1:
            region_decode["y"] = 0
        if region_decode["width"] == -1:
            region_decode["width"] = self.dimensions["width"]
        if region_decode["height"] == -1:
            region_decode["height"] = self.dimensions["height"]
        
        if kwargs.get("audio", False):
            start_audio = frame_rate_convert(region_decode["start"], self.frame_rate, audio_rate)
            end_audio = frame_rate_convert(region_decode["end"], self.frame_rate, audio_rate)

        if kwargs.get("video", True):
            video_trim = buffer[region_decode["start"]:region_decode["end"], :, :, :]
            roi_trim = video_trim[:, region_decode["y"]:region_decode["y"]+region_decode["height"], region_decode["x"]:region_decode["x"]+region_decode["width"], :]

        if kwargs.get("video", True) and kwargs.get("audio", False) == False:
            return roi_trim
        elif kwargs.get("video", True) == False and kwargs.get("audio", False):
            return audio_data[start_audio:end_audio], audio_rate
        elif kwargs.get("video", True) and kwargs.get("audio", False):
            return roi_trim, audio_data[start_audio:end_audio], audio_rate
        
    def render(self, data, path):
        """Render the video file to a new mp4 file at path, or a wav file."""

        if os.path.splitext(path)[1] == ".mp4" or os.path.splitext(path)[1] == ".wav":
            if isinstance(data, dict):
                if "video" in data:
                    # Both
                    if os.path.splitext(path)[1] == ".mp4":
                        temp_audio_path = os.path.join(os.getcwd(), "temp", "temp_audio_out.wav")
                        temp_video_path = os.path.join(os.getcwd(), "temp", "temp_video_out.mp4")
                        if os.path.isdir(os.path.dirname(temp_audio_path)) == False:
                            os.makedirs(os.path.dirname(temp_audio_path))

                        write_video(data["video"], temp_video_path, self.frame_rate, data["video"].shape[2], data["video"].shape[1])
                        
                        # Add audio
                        scipy.io.wavfile.write(temp_audio_path, data["audio_rate"], data["audio"])

                        video_clip = VideoFileClip(temp_video_path)
                        audio_clip = AudioFileClip(temp_audio_path)
                        video_clip = video_clip.set_audio(audio_clip)
                        video_clip.write_videofile(path, codec="libx264", audio_codec="aac")

                        video_clip.close()
                        audio_clip.close()

                        shutil.rmtree(os.path.dirname(temp_audio_path))
                        return path
                    else:
                        print("Unable to render, must render to mp4 format.")
                        return None
                else:
                    # Just audio
                    if os.path.splitext(path)[1] == ".wav":
                        scipy.io.wavfile.write(path, data["audio_rate"], data["audio"])
                        return path
                    else:
                        print("Unable to render, must render to wav format.")
                        return None
            else:
                # Just video:
                if os.path.splitext(path)[1] == ".mp4":
                    write_video(data, path, self.frame_rate, data.shape[2], data.shape[1])
                    return path
                else:
                    print("Unable to render, must render to mp4 format.")
                    return None
        else:
            print("Unable to render, must render to mp4 or wav format.")
            return None
        
    def extract_audio(self, dest : str):
        """Extract the audio from the video file as a wav file."""

        subprocess_args = ["ffmpeg", "-i", self.corpus.render_path, dest]
        subprocess.run(subprocess_args)

class MP4Handler(VideoHandler):
    def __init__(self, corpus) -> None:
        super().__init__(corpus)

def get_video_handler(ext : str, corpus) -> VideoHandler:
    """Get the handler corresponding to file format."""
    
    if ext == "mp4":
        return MP4Handler(corpus)
    elif ext == "mpg":
        pass