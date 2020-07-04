# Author : Muhammet Kara

import cv2 as cv
import os
from time import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Enter video file path.")
ap.add_argument("-s", "--second", required=True, help="Enter time interval in seconds.")
ap.add_argument("--shrink", required=True, help="Enter a value to shrink frame, default value is 1")
args = vars(ap.parse_args())

file = str(args["file"])

if not os.path.isfile(file):
    print("File not found!")

# images forder name
folder_name = base=os.path.basename(file) + " frames"

# create folder for images in current path if not exists
current_path = os.getcwd()
folder_path = os.path.join(current_path, folder_name)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)

cap = cv.VideoCapture(str(args["file"]))

total_frame = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
# save frame every # seconds
seconds = int(args["second"])
fps = cap.get(cv.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video stream or file")

frame_counter = 1

while frame_counter <= total_frame:

    cap.set(cv.CAP_PROP_POS_FRAMES, frame_counter)

    ret, frame = cap.read()

    if int(args["shrink"]) > 1:
        # shrink frame if height > 600px
        height, width, layers = frame.shape
        if height > 600:
            height = int(height / int(args["shrink"]))
            width = int(width / int(args["shrink"]))
            frame = cv.resize(frame, (width, height))

    # save frame
    # file path
    file_path = os.path.join(folder_path, str(time()) + ".jpg")
    cv.imwrite(file_path, frame)

    frame_counter += multiplier
