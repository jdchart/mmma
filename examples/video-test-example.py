import mmma
import utils

vid_path = utils.test_media("video")[0]

test = mmma.Media(vid_path)

print(test.ext)
print(test.type)