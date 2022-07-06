import os
import numpy as np
import cv2
import time
import datetime

import glob

frames_per_seconds = 20
save_path='./timelapse.avi'
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('video.avi', fourcc, frames_per_seconds, (2144, 1424))
timelapse_img_dir = r'C:\Users\Tristan\Desktop\timelapses\test'

def images_to_video(video, image_dir, clear_images=False):
    image_list = glob.glob(f"{image_dir}/*")
    sorted_images = sorted(image_list)
    print(sorted_images)
    for file in sorted_images:
        image_frame  = cv2.imread(file)
        video.write(image_frame)
    video.release()

images_to_video(video, timelapse_img_dir)
