import datetime
from PIL import Image
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx
import numpy as np

from loop_audio import loop_audio
  
videoDuration = 60 * 60 * 3

verbose = True
# clip_rain = VideoFileClip("movies/overlays/pexels-atypeek-dgn-7043616.mp4")
clip_rain = VideoFileClip("movies/overlays/pexels-gusat-andrei-6527130.mp4")
clip_rain = vfx.speedx(clip_rain, 50)
clip_rain = vfx.loop(clip_rain, duration=videoDuration) # like this
clip_rain = clip_rain.set_opacity(.50)

# TODO: test this audio looping method ,ay be much faster than what we have 
# make sure the it doesnt have the silent gaps between loops
# audio = afx.audio_loop( audioClip, duration=videoDuration)

# background = VideoFileClip("movies/production ID_4154555.mp4")
# background = background.subclip(0, 9)

# background = vfx.time_symmetrize(background)
# background = vfx.loop(background, duration=videoDuration).set_audio(None)



imagePath = "pictures/pexels-jan-kopřiva-3634855.jpeg";
image = Image.open(imagePath)
im = image.resize(clip_rain.size)
imageArray = np.array(im)

background = ImageClip(imageArray)

audioPath = "audio/543449__kostas17__howling-wind.wav"
audio = loop_audio(videoDuration, audioPath=audioPath)
clip_rain = clip_rain.set_audio(audio).volumex(5)
final = CompositeVideoClip([background, clip_rain], size=clip_rain.size).set_duration(videoDuration)

today = datetime.date.today()
final_clip_path = "movies/windhouling" + str(today) + ".mp4"
# showing final clip
# final.write_videofile(final_clip_path, verbose=False, logger=None)
logger = logger="bar" if verbose else None
final.write_videofile(final_clip_path, threads=32, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", logger="bar" if verbose else None)

command = "open " + final_clip_path
print(command)
os.system(command=command)

# final = concatenate_videoclips([video1, video2])
# final = final.set_audio(audio.set_duration(final))

# this could be faster
# final.write_videofile("movies/output.mp4", audio="audio.mp3")