import datetime
import sys
from os import dup
from moviepy.editor import *
import numpy as np
from PIL import Image


if len(sys.argv) < 5:
    print("need to add some arguments: imagePath, audioPath, duration, createdMovieName")
    exit()
imagePath = sys.argv[1]
audioPath = sys.argv[2]
videoDuration = int(sys.argv[3])
movieName = sys.argv[4]

im = Image.open(imagePath)
imageHeight = im.height if im.height % 2 == 0 else im.height - 1
imageWidth = im.width if im.width % 2 == 0 else im.width -1
im = im.resize([imageWidth, imageHeight])
imageArray = np.array(im)
imageclip = ImageClip(imageArray)


originalAudio = AudioFileClip(audioPath)
audio = originalAudio.audio_loop(duration=videoDuration)

patchtimes = []
timestamp = originalAudio.duration;
for x in range(int(videoDuration/originalAudio.duration)): 
    patchtimes.append(timestamp - 1)
    timestamp+=originalAudio.duration

print ("time stamps are " + str([str(datetime.timedelta(seconds = patchtime)) for patchtime in patchtimes]))
audioList = [audio]
if (len(patchtimes) > 0):
    patchesClip = CompositeAudioClip([originalAudio.set_start(timestamp).set_end(timestamp + 3) for timestamp in patchtimes]).set_duration(videoDuration)
    audioList.append(patchesClip)
audio = CompositeAudioClip(audioList)
imageclip = imageclip.set_audio(audio).set_duration(audio.duration).volumex(5)


# Write the result to a file (many options available !)
imageclip.write_videofile("movies\\" + movieName + ".mp4", fps=12, threads=4)