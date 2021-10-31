import datetime
import moviepy.video.fx.all as vfx

from moviepy.editor import *
import os

from loop_audio import loop_audio

videoDuration = 60 * 6

# some times i get an error that says it cannot read the first (i think it means last) frame of the video
# internet solution is to take out one sec at the end
clip = VideoFileClip("movies\\pexels-tima-miroshnichenko-6316263winter.mp4")
clip = clip.subclip(0, 10)

audio = loop_audio(videoDuration, audioPath="audio\\Night Snow Asher Fulero.mp3")

# clip = vfx.time_symmetrize(clip)

final = vfx.make_loopable(cross=3, clip=clip)
# final = vfx.fadein(clip=final, duration=2, initial_color=None)
final = vfx.loop(clip, duration=videoDuration).set_audio(audio)


clip_name = "movies\\makeLoopable" + str(datetime.datetime.timestamp(datetime.datetime.now())) + ".mp4"

# final.write_videofile(clip_name)

final.write_videofile(clip_name, threads=256, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", logger="bar")
command = "open"
if sys.platform == 'win32':
    command = "start"

os.system(command + " " + clip_name)
