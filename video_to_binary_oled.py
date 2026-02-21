# Video to Binary converter for OLED displays
# This script takes a video file as input and converts it into a binary format suitable for OLED displays.
# Code can be modified to fit specific OLED display requirements, this code is for a 128x64 pixel display with 1-bit color depth (black and white).
# The output will be a binary file where each byte represents 8 pixels (1 bit per pixel).
# STUDENT ID: 20766915

import cv2
import numpy as np
import os

video = "input.mp4"
binary = "output.bin"
fps_target = 15
threshold = 128

cap = cv2.VideoCapture(video)
if not cap.isOpened():
    print("ERROR: Could not open video.")
    exit()

source_fps = cap.get(cv2.CAP_PROP_FPS)
frame_skip = max(1, int(source_fps / fps_target))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Video opened: {video}")
print(f"Frame count: {frame_count}, Width: {cap_width}, Height: {cap_height}")
print(f"Source FPS: {source_fps}, Target FPS: {fps_target}")
print(f"Frame skip: {frame_skip}")

def frame_to_binary(frame):
    # RESIZE (Default: 128x64)
    resized = cv2.resize(frame, (128, 64), interpolation=cv2.INTER_AREA)
    # GREYSCALE
    greyscaled = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # THRESHOLD
    _, thresholded = cv2.threshold(greyscaled, threshold, 255, cv2.THRESH_BINARY)
    # BINARY CONVERSION
    binary_frame = np.packbits(thresholded // 255)

    return binary_frame


