from moviepy.editor import *
import numpy as np
from PIL import Image



im = Image.open("pictures\\Morning Farm.jpg")

print ("before resizing -> width: " + str(im.width) + ", height: " + str(im.height))
im.show()
im = im.resize([650, 492])
print ("before resizing -> width: " + str(im.width) + ", height: " + str(im.height))
im.show()


im = np.array(im)
imageclip = ImageClip(im).set_duration(10)
imageclip.preview()
