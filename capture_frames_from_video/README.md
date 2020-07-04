This code gets a video file and saves frames from it.
Frames will be saved in to a file named as video file's name.

### parameters ###

-f / --file = video file path
-s / -seconds = program will save frames every # seconds, # is second parameter
--shrink = Enter a value to shrink frame, default value is 1. If shrink is 2, frame's sizes will multiplied by 1/2.

### Usage ###

python capture_frames_from_video.py -f file_path  -s second


sample commands:
python capture_frames_from_video.py -f videos\5.MOV -s 1
python capture_frames_from_video.py -f videos\5.MOV -s 1 --shrink 2

### Note ###
if you get an error like: cv2 module not found, install opencv module like that;
pip install opencv-python or pip3 install opencv-python 