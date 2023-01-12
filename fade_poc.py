import datetime
from PIL import Image
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx
import numpy as np
import sys

from loop_audio import loop_audio
  
videoDuration = 60 * 60 * 3

verbose = True
# clip_rain = VideoFileClip("movies/overlays/pexels-atypeek-dgn-7043616.mp4")
# clip_rain = vfx.speedx(clip_rain, 50)
# clip_rain = VideoFileClip("movies/overlays/4K_Silver_White_Sparkles_loop_Videvo.mp4")
# clip_rain = clip_rain.subclip(0, clip_rain.duration - 1).set_audio(None)

# TODO: test this audio looping method ,ay be much faster than what we have 
# make sure the it doesnt have the silent gaps between loops
# audio = afx.audio_loop( audioClip, duration=videoDuration)
# backgroun_path = "movies/final_2022-02-21.mp4"
backgroun_path = "movies/overlays/River-44509.mp4"

background = VideoFileClip(backgroun_path).set_audio(None)#.resize(clip_rain.size)
# background = background.subclip(0, 9).set_audio(None)

# background = vfx.time_symmetrize(background)
background = vfx.loop(background, duration=videoDuration)



# imagePath = "pictures/pexels-jan-kopřiva-3634855.jpeg";
# image = Image.open(backgroun_path)
# im = image.resize(clip_rain.size)
# imageArray = np.array(im)

# background = ImageClip(imageArray)

audioPath = "audio/Hopeful Freedom - Asher Fulero.mp3"
audioClip = AudioFileClip(audioPath)
audioClip = audioClip.subclip(0, audioClip.duration - 7)
audio = loop_audio(videoDuration, audioClip=audioClip, overlap=5)#audioPath=audioPath)
# alarm_path = "audio/219244__zyrytsounds__alarm-clock-short.wav"
# alarm = AudioFileClip(alarm_path)
# alarm = alarm.set_start(videoDuration - alarm.duration)
# audio = CompositeAudioClip([audio, alarm]).volumex(5)
# clip_rain = clip_rain.set_audio(audio)
# final = CompositeVideoClip([background], size=background.size).set_duration(audio.duration).set_audio(audio)
# final = concatenate_videoclips([final,alarm])
# clip_rain = vfx.loop(clip_rain, duration=audio.duration) # like this
# clip_rain = clip_rain.set_opacity(.50)
final = background.set_audio(audio).set_duration(videoDuration)#CompositeVideoClip([background], size=clip_rain.size).set_duration(audio.duration).set_audio(audio)
# final = vfx.fadein(clip=final, duration=2, initial_color=None)
today = datetime.date.today()
final_clip_path = "movies/final_" + str(today) + ".mp4"
# showing final clip
# final.write_videofile(final_clip_path, verbose=False, logger=None)
logger = logger="bar" if verbose else None
final.write_videofile(final_clip_path, threads=64, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", logger="bar" if verbose else None)
command = "open"
if sys.platform == 'win32':
    command = "start"


command = command + " " + final_clip_path
print(command)
os.system(command=command)

# final = concatenate_videoclips([video1, video2])
# final = final.set_audio(audio.set_duration(final))

# this could be faster
# final.write_videofile("movies/output.mp4", audio="audio.mp3")