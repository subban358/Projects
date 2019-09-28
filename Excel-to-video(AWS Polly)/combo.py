import subprocess
cmd = 'ffmpeg -y -i voice.mp3  -r 30 -i movie.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
subprocess.call(cmd, shell=True)                                     # "Muxing Done
print('Muxing Done')