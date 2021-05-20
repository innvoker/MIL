
#对单张图片进行预测

from frcnn1 import FRCNN
from PIL import Image
from torch.jit.annotations import List

frcnn = FRCNN()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = frcnn.detect_image(image)
        r_image.show()
