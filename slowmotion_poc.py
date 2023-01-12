# Import everything needed to edit video clips
import datetime
from moviepy.editor import *

verbose = True
file_path = "movies/overlays/River-44509.mp4"

   
# loading video dsa gfg intro video
clip = VideoFileClip(file_path)
   
# getting only first 5 seconds
# clip = clip.subclip(0, 5)
   
# applying speed effect
final = clip.fx( vfx.speedx, 0.1)

today = datetime.date.today()

final_clip_path = "movies/final_" + str(today) + ".mp4"

final.write_videofile(final_clip_path, threads=64, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", logger="bar" if verbose else None)
command = "open"
if sys.platform == 'win32':
    command = "start"


command = command + " " + final_clip_path
print(command)
os.system(command=command)