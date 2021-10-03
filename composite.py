import datetime
import sys
import os
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import numpy as np
from PIL import Image
from loop_audio import loop_audio


inputDuration = sys.argv[1]
overlayPath = sys.argv[2]
overlayOpacity = float(sys.argv[3])
overlaySpeed = float(sys.argv[4])
backgroundPath = sys.argv[5]
audioPath = sys.argv[6]


print ("these are the inputs: " + "inputDuration: " + inputDuration + ", " + "overlayPath: " + overlayPath + ", " + "overlayOpacity: " + str(overlayOpacity) + ", " + "overlaySpeed: " + str(overlaySpeed) + ", " + "backgroundPath: " + backgroundPath + ", " + "audioPath: " + audioPath)


# if inputDuration is none or 0 and below make video 60 mins
videoDuration = 60 if inputDuration == None or int(inputDuration) < 1 else int(inputDuration)

print("overlay paths + " + str(len([VideoFileClip(path) for path in overlayPath.split(',')])))
# set overlay
overlay = CompositeVideoClip([VideoFileClip(path) for path in overlayPath.split(',')], size=[1280,720]).set_audio(None)
print("overlay duration original: " + str(overlay.duration))
# applying speed effect
overlay = overlay.fx(vfx.speedx, overlaySpeed)
print("overlay duration after speed up: " + str(overlay.duration))
# applying loop
overlay = vfx.loop(overlay, duration=videoDuration) # like this
print("overlay duration after loop: " + str(overlay.duration))
# applying opacity
overlay = overlay.set_opacity(overlayOpacity)

# set Background
background = ImageClip(np.array(Image.open(backgroundPath).resize(overlay.size)))

# Set audio + length
audio = loop_audio(videoDuration, audioPath=audioPath)

final = CompositeVideoClip([background, overlay], size=overlay.size).set_audio(audio).set_duration(videoDuration)

final_clip_path = "movies\\temp\\composite.mp4"
final.write_videofile(final_clip_path)
# overlay.write_videofile(final_clip_path)
os.system("start " + final_clip_path)
