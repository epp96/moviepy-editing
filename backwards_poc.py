import datetime
import moviepy.video.fx.all as vfx

from moviepy.editor import *
import os

from loop_audio import loop_audio

videoDuration = 3600

clip = VideoFileClip("movies\\practice\\windy-autum.mp4")
# some times i get an error that says it cannot read the first (i think it means last) frame of the video
# internet solution is to take out one sec at the end
audio = loop_audio(videoDuration, audioClip=clip.audio)

clip = clip.subclip(0, clip.duration - 1)

clip = vfx.time_symmetrize(clip)

final = vfx.loop(clip, duration=videoDuration).set_audio(audio)

clip_name = "movies\\windy-autum" + str(datetime.datetime.timestamp(datetime.datetime.now())) + ".mp4"

final.write_videofile(clip_name)

# os.system("start " + clip_name)
