import os
def save():
    os.system("ffmpeg -r 1 -i %d.jpg -vcodec mpeg4 -y movie.mp4")

save()    