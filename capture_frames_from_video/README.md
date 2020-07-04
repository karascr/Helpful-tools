# Capture Frames From A Video #
This script gets a video file and saves frames from it.
Script creates a folder with the same name as the video and saves captured images in to this folder.

## How to use? ##
Open terminal in directory of script.
'opencv-python' module must be installed in your env.
Use this command to install opencv-python
'''
pip install opencv-python
'''
Once opencv is installed, use this command to execute script.
'''
python capture_frames_from_video.py -f file_path  -s second --shrink 1
'''

### parameters ###
-f is path of video you want to process.

second is time interval. For example if second parameter is 2, script will capture frames every 2 seconds.

--shrink is a value to shrink frame, default value is 1. If shrink is 2, frame's sizes will multiplied by 1/2 before capturing.
If video's resolution is 800x600, setting parameter shrink = 2, captured frames' resolution will be 400x300. 


## sample commands ##
'''
python capture_frames_from_video.py -f videos\5.MOV -s 1 --shrink 1
'''
Captures frames every second with original size.
'''
python capture_frames_from_video.py -f videos\5.MOV -s 1 --shrink 2
'''
Captures frames every 2 seconds with half sized.

### Note ###
if you get an error like: cv2 module not found, install opencv module like that;
pip install opencv-python or pip3 install opencv-python 
