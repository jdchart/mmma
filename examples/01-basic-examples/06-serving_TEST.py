import mmma

import cv2

from scipy.io.wavfile import write


# Create a corpus from a file:
audio_file = mmma.Corpus(render_path = "/Users/jacob/Documents/Repos/mmma/test-corpora/audios/truc2.wav", region = {"start" : 1000, "end" : 2000})

#image_file = mmma.Corpus(render_path = "/Users/jacob/Documents/Repos/mmma/test-corpora/images/images.jpeg")
image_file = mmma.Corpus(render_path = "/Users/jacob/Documents/Repos/mmma/test-corpora/images/images.jpeg", region = {"x" : 100, "y" : 100})


video_file = mmma.Corpus(render_path = "/Users/jacob/Documents/Repos/mmma/test-corpora/videos/video_and_sound.mp4")


# Use the to_np() method to get the numpy array:
np_array_audio = audio_file.to_np()
np_array_image = image_file.to_np()
np_array_video = video_file.to_np()



print()
print(f"Audio: {np_array_audio.shape} ({np_array_audio.dtype})")
print(f"Audio: {np_array_image.shape} ({np_array_image.dtype})")
print(f"Video: {np_array_video.shape} ({np_array_video.dtype})")









# Write Audio:
write("/Users/jacob/Documents/Repos/mmma/OUTPUT_audio.wav", audio_file.frame_rate, np_array_audio)

# Write Image:
cv2.imwrite("/Users/jacob/Documents/Repos/mmma/OUTPUT_img.png", np_array_image)


# Write video:
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("/Users/jacob/Documents/Repos/mmma/OUTPUT_video.mp4", fourcc, video_file.frame_rate, (video_file.dimensions["width"], video_file.dimensions["height"]))
for frame_array in np_array_video:
    out.write(frame_array)
out.release()