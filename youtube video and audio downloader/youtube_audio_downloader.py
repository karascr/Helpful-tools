import argparse
import re

from pytube import YouTube
from time import time
import os
import moviepy.editor as mp

ap = argparse.ArgumentParser()
ap.add_argument("--url", required=True, help="Enter video url.")
args = vars(ap.parse_args())

output_folder_name = "downloaded_audios"

cwd = os.getcwd()

outout_folder_path = os.path.join(cwd, output_folder_name)

if not os.path.exists(outout_folder_path):
    os.mkdir(outout_folder_path)


url = args["url"]

x = YouTube(url)

title = x.title

if title == "YouTube":
    title = x.author + " " + str(time())

audio = x.streams.filter(only_audio=True).first()

if audio == None:
    print("This video is not available.")
else:
    audio.download(outout_folder_path, title)
    tgt_folder = "downloaded_audios"

    for file in [n for n in os.listdir(tgt_folder) if re.search('mp4', n)]:
        full_path = os.path.join(tgt_folder, file)
    output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path)
    clip.write_audiofile(output_path)
    os.remove(full_path)
    print("Downloaded!")