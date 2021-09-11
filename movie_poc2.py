from os import dup
from moviepy.editor import *
videoDuration = 300
audioName = 'Waves-Crashing-on-Rock-Beach'
imageclip = ImageClip('pictures\\water-on-ocean-rocks.jpg')
# videoclip = VideoFileClip()
originalAudio = AudioFileClip('audio\\' + audioName + '.mp3')
audio = originalAudio.audio_loop(duration=videoDuration)

patchtimes = []
timestamp = originalAudio.duration;
for x in range(int(videoDuration/originalAudio.duration)): 
    patchtimes.append(0 + timestamp - 1)
    timestamp+=originalAudio.duration

audioclip = CompositeAudioClip([originalAudio.set_start(timestamp).set_end(timestamp + 3) for timestamp in patchtimes]).set_duration(videoDuration)
audio = CompositeAudioClip([audio, audioclip])
imageclip = imageclip.set_audio(audio).set_duration(audio.duration)


# Write the result to a file (many options available !)
imageclip.write_videofile("movies\\" + audioName + ".mp4", fps=12)