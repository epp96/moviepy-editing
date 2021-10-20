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

audioPath = ""
use_overlay_audio = False
audio = None
if len(sys.argv) > 6:
    audioPath = sys.argv[6]
    audio = AudioFileClip(audioPath)
else: 
    use_overlay_audio = True


print ("these are the inputs: " + "inputDuration: " + inputDuration + ", " + "overlayPath: " + overlayPath + ", " + "overlayOpacity: " + str(overlayOpacity) + ", " + "overlaySpeed: " + str(overlaySpeed) + ", " + "backgroundPath: " + backgroundPath + ", " + "audioPath: " + audioPath)

# if inputDuration is none or 0 and below make video 60 mins
videoDuration = 60 if inputDuration == None or int(inputDuration) < 1 else int(inputDuration)
overlay_paths = overlayPath.split(',')
overlay_clips = [vfx.loop(vfx.speedx(VideoFileClip(path).set_opacity(overlayOpacity/len(overlay_paths)), overlaySpeed), duration=videoDuration) for path in overlay_paths]
print("overlay paths + " + str(len(overlay_clips)))
# set overlay
overlay = CompositeVideoClip(overlay_clips, size=[1280,720]).set_audio(None)
print("overlay duration original: " + str(overlay.duration))

# applying speed effect
# overlay = overlay.fx(vfx.speedx, overlaySpeed)
# overlay = vfx.speedx(overlay, overlaySpeed)
# print("overlay duration after loop: " + str(overlay.duration))
# applying loop
# overlay = vfx.loop(overlay, duration=videoDuration) # like this
# print("overlay duration after speed up: " + str(overlay.duration))

# applying opacity
# overlay = overlay.set_opacity(overlayOpacity)

# set Background
background = ImageClip(np.array(Image.open(backgroundPath).resize(overlay.size))).set_duration(videoDuration)

# Set audio + length
try:
    if use_overlay_audio:
        audio = overlay_clips[0].audio
    audio = loop_audio(videoDuration, audio)
except:
    print ("audio is not valid using overlay audio will be using audio from: " + overlay_paths[0])
finally:
    if audio == None: 
        audio = loop_audio(videoDuration, audioPath=overlay_paths[0])

overlay = overlay.set_audio(audio)

print("overlay duration before composite: " + str(overlay.duration))

final = CompositeVideoClip([background, overlay], size=overlay.size).set_duration(videoDuration)

final_clip_path = "movies/temp/composite.mp4"
# final.write_videofile(final_clip_path)
# final.write_videofile(final_clip_path, verbose=False, logger=None) #,threads=32)
# overlay.write_videofile(final_clip_path, verbose=False, logger=None) #,threads=32)
final.write_videofile(final_clip_path, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


command = "start " + final_clip_path
print(command)
os.system(command=command)
