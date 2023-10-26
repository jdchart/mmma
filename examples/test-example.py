import mmma
import utils

vid = utils.test_media("image")[1]

test = mmma.Media(vid)

print(test.ext)
print(test.type)