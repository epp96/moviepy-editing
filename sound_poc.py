# Plays the note A (a sine wave of frequency 440HZ)
import numpy as np
from moviepy.editor import *
make_frame_sin = lambda t: 2*[ np.sin(440 * 2 * np.pi * t) ]
make_frame_cos = lambda t: 2*[ np.cos(440 * 2 * np.pi * t) ]

clip_sin = AudioClip(make_frame_sin, duration=20, fps=60)
clip_cos = AudioClip(make_frame_cos, duration=20, fps=60)
composite_clip = CompositeAudioClip([clip_sin, clip_cos]).set_fps(60)
# clip = CompositeVideoClip([clip])
composite_clip.write_audiofile("audio\\temp\\helloworld.wav")