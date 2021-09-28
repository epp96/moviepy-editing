from PIL import Image
from moviepy.editor import *
from moviepy.video.tools.drawing import color_split
import numpy as np

duration = 6 # duration of the final clip

main_clip = VideoFileClip("movies/practice/rain-on-glass.mp4")
audio = AudioFileClip("audio/Fire.mp3")
W,H = main_clip.size

imagePath = "pictures/Fire.jpg";
image = Image.open(imagePath)
# imageHeight = image.height if image.height % 2 == 0 else image.height - 1
# imageWidth = image.width if image.width % 2 == 0 else image.width -1
im = image.resize([int(W/3), int(H/3)])
imageArray = np.array(im)

def make_rgb(img):
    if len(img.shape) == 3:
        return img
    img3 = np.empty(img.shape + (3,))
    img3[:, :, :] = img[:, :, np.newaxis]
    return img3

X_repaired = make_rgb(imageArray)

maskImage = ImageClip(np.array(imageArray)).set_position(('right', 'bottom')).set_audio(audio).set_duration(main_clip.duration).on_color(col_opacity=0.1)

# piano = (VideoFileClip("../../videos/douceamb.mp4",audio=False).subclip(30,50).resize((w/3,h/3)).    # one third of the total screen
#          margin( 6,color=(255,255,255)).  #white margin
#          margin( bottom=20, right=20, opacity=0). # transparent
#          set_pos(('right','bottom')) )



cc = CompositeVideoClip([main_clip, maskImage])
#cc.preview()
cc.write_videofile("movies/temp/test1.avi",fps=24,codec='libx264')#fps=24) #, codec='mpeg4')