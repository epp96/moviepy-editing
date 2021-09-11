import sys
from os import dup
from moviepy.editor import *

if len(sys.argv) < 5:
    print("need to add some arguments: imagePath, audioPath, duration, createdMovieName")
    exit()
imagePath = sys.argv[1]
audioPath = sys.argv[2]
videoDuration = int(sys.argv[3])
movieName = sys.argv[4]

imageclip = ImageClip(imagePath)

originalAudio = AudioFileClip(audioPath)
audio = originalAudio.audio_loop(duration=videoDuration)

patchtimes = []
timestamp = originalAudio.duration;
for x in range(int(videoDuration/originalAudio.duration)): 
    patchtimes.append(timestamp - 1)
    timestamp+=originalAudio.duration

print ("time stamps are " + str(patchtimes))

audioclip = CompositeAudioClip([originalAudio.set_start(timestamp).set_end(timestamp + 3) for timestamp in patchtimes]).set_duration(videoDuration)
audio = CompositeAudioClip([audio, audioclip])
imageclip = imageclip.set_audio(audio).set_duration(audio.duration).volumex(5)


# Write the result to a file (many options available !)
imageclip.write_videofile("movies\\" + movieName + ".mp4", fps=12)





