# Video to Binary converter for LED Matrix displays
# This script takes a video file as input and converts it into a binary format suitable for LED Matrix displays.
# Code can be modified to fit specific LED Matrix display requirements, this code is for a 8x8 pixel display with 1-bit color depth.
# The output will be a binary file where each byte represents 8 pixels (1 bit per pixel).
# Yes, the code is a slight modification of the video_to_binary_oled.py script.
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
    resized = cv2.resize(frame, (8, 8), interpolation=cv2.INTER_AREA)
    # GREYSCALE
    greyscaled = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # THRESHOLD
    _, thresholded = cv2.threshold(greyscaled, threshold, 255, cv2.THRESH_BINARY)
    # BINARY CONVERSION
    binary_frame = np.packbits(thresholded // 255)

    return binary_frame

with open(binary, 'wb') as f:
    frame_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_index % frame_skip == 0:
            binary_frame = frame_to_binary(frame)
            f.write(binary_frame.tobytes())
            print(f"Processed frame {frame_index}/{frame_count}")

        frame_index += 1
cap.release()
print(f"Binary file created: {binary}")
print("Conversion complete!")
print("Total frames processed:", frame_index // frame_skip)


