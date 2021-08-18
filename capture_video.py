# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:29:05 2021

@author: Bell
"""

import cv2
import os
import pafy

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

url = "https://<add something here>"
video = pafy.new(url)
best = video.getbest(preftype="mp4")
save_all_frames(best.url, 'data/temp/result_png', 'sample_video_img', 'png')