# Plays the note A (a sine wave of frequency 440HZ)
import numpy as np
from moviepy.editor import *
make_frame = lambda t: 2*[ np.sin(440 * 2 * np.pi * t) ]
clip = AudioClip(make_frame, duration=5, fps=15)
clip.preview()