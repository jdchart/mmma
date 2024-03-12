import scipy
import os
import cv2
import shutil
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip

def to_wav(path, np_array, sr):
    if os.path.splitext(path)[1] == ".wav":
        scipy.io.wavfile.write(path, sr, np_array)
        return path
    else:
        print("Unable to render, must render to wav format.")
        return None
    
def to_png(path, np_array):
    if os.path.splitext(path)[1] == ".png":
        cv2.imwrite(path, np_array)
        return path
    else:
        print("Unable to render, must render to png format.")
        return None

def to_mp4(data, path):
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
    
def write_video(data, path, fr, w, h):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path, fourcc, fr, (w, h))
    for frame_array in data:
        out.write(frame_array)
    out.release()