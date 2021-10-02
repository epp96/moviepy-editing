import datetime
import sys
from os import dup
from moviepy.editor import *
import numpy as np
from PIL import Image
from loop_audio import loop_audio


if len(sys.argv) < 5:
    print("need to add some arguments: imagePath, audioPath, duration, createdMovieName")
    exit()
imagePath = sys.argv[1]
audioPath = sys.argv[2]
videoDuration = int(sys.argv[3])
movieName = sys.argv[4]

print ("resizing image if needed")
im = Image.open(imagePath)
imageHeight = im.height if im.height % 2 == 0 else im.height - 1
imageWidth = im.width if im.width % 2 == 0 else im.width -1
im = im.resize([imageWidth, imageHeight])
imageArray = np.array(im)

print ("image dimensions -> width: " + str(imageWidth) + ", height: " + str(imageHeight))

imageclip = ImageClip(imageArray)

audio = loop_audio(videoDuration, audioPath)
imageclip = imageclip.set_audio(audio).set_duration(audio.duration).volumex(5)


# Write the result to a file (many options available !)
# TODO see if lowering the fps helps with performance - so far it is just an image 
#   so I dont think it will do anything if it is 1 fps instead of 12
imageclip.write_videofile("movies\\" + movieName + ".mp4", fps=1, threads=4)