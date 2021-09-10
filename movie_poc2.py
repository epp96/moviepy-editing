from moviepy.editor import *
videoDuration = 300
audioName = 'Waves-Crashing-on-Rock-Beach'
imageclip = ImageClip('pictures\\water-on-ocean-rocks.jpg')
# videoclip = VideoFileClip()
music = AudioFileClip('audio\\' + audioName + '.mp3')
audio = afx.audio_loop( music, duration=videoDuration)
imageclip = imageclip.set_audio(audio).set_duration(videoDuration)
# Write the result to a file (many options available !)
imageclip.write_videofile("movies\\" + audioName + ".mp4", fps=12)