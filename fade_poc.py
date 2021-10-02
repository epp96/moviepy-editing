import datetime
from PIL import Image
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx
import numpy as np
  
videoDuration = 60 * 1
clip_rain = VideoFileClip("movies\\practice\\rain.mp4")
clip_rain = vfx.loop(clip_rain, duration=videoDuration) # like this
clip_rain = clip_rain.set_opacity(.50)

# TODO: test this audio looping method ,ay be much faster than what we have 
# make sure the it doesnt have the silent gaps between loops
# audio = afx.audio_loop( audioClip, duration=videoDuration)


imagePath = "pictures\\Thunder with Birds and Flies.jpg";
image = Image.open(imagePath)
im = image.resize(clip_rain.size)
imageArray = np.array(im)

newUserImage = ImageClip(imageArray)

audioPath = "audio\\Rain on Car Heavy.mp3"


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
    # do we need to set the duration here or in the final audio composite
    patchesClip = CompositeAudioClip([originalAudio.set_start(timestamp).set_end(timestamp + 3) for timestamp in patchtimes]).set_duration(videoDuration)
    audioList.append(patchesClip)
audio = CompositeAudioClip(audioList)
clip_rain = clip_rain.set_audio(audio).volumex(5)
final = CompositeVideoClip([newUserImage, clip_rain], size=clip_rain.size).set_duration(videoDuration)

today = datetime.date.today()

# showing final clip
final.write_videofile("movies\\rain-and-thunder" + str(today) + ".mp4")


# final = concatenate_videoclips([video1, video2])
# final = final.set_audio(audio.set_duration(final))

# this could be faster
# final.write_videofile("movies/output.mp4", audio="audio.mp3")