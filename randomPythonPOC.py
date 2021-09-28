from moviepy.editor import *
import numpy as np
from PIL import Image




imagePath = "pictures/Fire.jpg";
image = Image.open(imagePath)
# imageHeight = image.height if image.height % 2 == 0 else image.height - 1
# imageWidth = image.width if image.width % 2 == 0 else image.width -1
imageArray = np.array([])

print(imageArray)

clip = ImageClip(imageArray).resize(400,600)
image.show()