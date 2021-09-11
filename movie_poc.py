# Import everything needed to edit video clips
from moviepy.editor import *
from moviepy.video.fx import resize
# import time

videoDuration = 300

audioName = "Waves-Crashing-on-Rock-Beach"

imageClip = ImageClip("pictures\\water-on-ocean-rocks.jpg", duration = videoDuration)


# concat audio clips
audioClipPath = "audio\\" + audioName + ".mp3"
audioClip = AudioFileClip(audioClipPath)

print (f"original clip duration: {audioClip.duration}")



numberOfAudioClips = range(int(videoDuration/audioClip.duration))

arrayAudioClips = [audioClip]
# create array of audio clips
for i in numberOfAudioClips:
    arrayAudioClips.append(audioClip)
    print ("appended clip: " + str(len(arrayAudioClips)))

# audioClip = concatenate_audioclips(arrayAudioClips);
audioClip = CompositeAudioClip(arrayAudioClips)
print (f"compositeAudioClip duration: {audioClip.duration}")

clip = imageClip.set_audio(audioClip).set_duration(videoDuration)
# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip])

# Write the result to a file (many options available !)
video.write_videofile("movies\\" + audioName + ".mp4", fps=12)

