import mmma
import utils
import os


audio_path = utils.test_media("audio")[0]

test = mmma.Media(audio_path)

print(test.handler.duration)
print(test.handler.channels)
print(test.handler.sample_rate)
print(test.handler.frames)
print(test.handler.bit_depth)

test.write(os.path.join(os.getcwd(), "test-audio.pkl"))


#test2 = mmma.DescriptionAnalysis("test")
test2 = mmma.MFCCAnalysis(audio_path)
print(test2.process())


#loaded = mmma.read(os.path.join(os.getcwd(), "test-audio.pkl"))