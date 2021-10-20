
from moviepy.editor import *
import datetime




def loop_audio(videoDuration, audioClip=None, audioPath=""):
    if videoDuration == 0 or (len(audioPath) == 0 and audioClip == None):
        raise Exception('videoDuration cannot be 0 nor both audioPath and audioClip empty')
    originalAudio=None
    try:
        # originalAudio = AudioFileClip(audioPath)
        originalAudio = CompositeAudioClip([AudioFileClip(path) for path in audioPath.split(',')])

    except Exception as e:
        if audioClip != None:
            originalAudio = audioClip
        elif len(audioPath) == 0:
            raise Exception('both audioPath and audioClip empty')
        else:
            raise e

    audio = originalAudio.audio_loop(duration=videoDuration)

    patchtimes = []
    timestamp = originalAudio.duration;
    for x in range(int(videoDuration/originalAudio.duration)): 
        patchtimes.append(timestamp - 1)
        timestamp+=originalAudio.duration

    print ("time stamps are " + str([str(datetime.timedelta(seconds = patchtime)) for patchtime in patchtimes]))
    audioList = [audio]
    if (len(patchtimes) > 0):
        patchesClip = CompositeAudioClip([originalAudio.set_start(timestamp).set_end(timestamp + 3) for timestamp in patchtimes]).set_duration(videoDuration)
        audioList.append(patchesClip)
    audio = CompositeAudioClip(audioList)
    return audio