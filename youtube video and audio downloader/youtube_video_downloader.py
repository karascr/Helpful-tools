import argparse
from pytube import YouTube
from time import time
import os

ap = argparse.ArgumentParser()
ap.add_argument("--url", required=True, help="Enter video url.")
ap.add_argument("--res", required=True, help="Enter resolution like 1080, 720...")
args = vars(ap.parse_args())

output_folder_name = "downloaded videos"

cwd = os.getcwd()

outout_folder_path = os.path.join(cwd, output_folder_name)

if not os.path.exists(outout_folder_path):
    os.mkdir(outout_folder_path)

url = args["url"]

x = YouTube(url)

title = x.title

if title == "YouTube":
    title = x.author + str(time())

video = x.streams.filter(res=args["res"]).first()

if video == None:
    print("This resolution is not available.")
else:
    video.download(outout_folder_path, title)
    print("Downloaded!")