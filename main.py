# import os
import subprocess

def getDuration(file):
    durationR = subprocess.run(['ffprobe', '-i', file, '-show_entries', 'format=duration', '-of', 'compact=p=0:nk=1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(durationR.stdout.decode('utf-8').strip())
    # , '-v', 'quiet'
    # print('Test1: ' + durationR.stdout.decode('utf-8').strip())
    # print('Test2: ' + durationR.stderr.decode('utf-8').strip())

    # f'ffprobe -i {list[0]} -show_entries format=duration -v quiet -of csv="p=0"'
    # durationR = subprocess.run(['pwd'], stdout=subprocess.PIPE)
    # durationR = subprocess.run(['du', list[0]], stdout=subprocess.PIPE)
    # durationR = subprocess.run(['ffprobe', '-i', 'VID_20200701_110316.mp4', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv="p=0"'], stdout=subprocess.PIPE, shell=True)
    # durationR = subprocess.run(['ffprobe', '-i', list[0], '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv="p=0"'], stdout=subprocess.PIPE, shell=True)
    # durationR = subprocess.run(['echo', list[0]], stdout=subprocess.PIPE, shell=True)


# lese list.txt
list = ['VID_20200701_110316.mp4', 'VID_20200701_105621.mp4']
durations = {e: getDuration(e) for e in list}
print(durations)
# hole Dauer


# getDuration(file)

# ffmpeg concat
# schreibe Index (für YT)
