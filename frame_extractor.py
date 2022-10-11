import os
import cv2

def extract_frames(video, folder_name):
    # create a new folder for the frames
    try:
        os.mkdir(folder_name)
    except OSError:
        print ("Creation of the directory %s failed" % folder_name)
        return

    vidcap = cv2.VideoCapture(video)
    # print("loaded video")
    success,image = vidcap.read()
    # print(success)
    count = 0
    while success:
        cv2.imwrite(folder_name + "/frame_%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1

vid_title = str(input("Enter the file name of the video with the extension: "))

extract_frames(vid_title, vid_title[:-4] + "_frames/")