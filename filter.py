import numpy as np
import cv2
import random

cap = cv2.VideoCapture(0)

frames_per_seconds = 20
save_path='saved-media/filter.mp4'
config = CFEVideoConf(cap, filepath=save_path, res='480p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)


def verify_alpha_channel(frame):
    try:
        frame.shape[3] # looking for the alpha channel
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame
    
    def apply_hue_saturation(frame, alpha, beta):
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    s.fill(199)
    v.fill(255)
    hsv_image = cv2.merge([h, s, v])

    out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    frame = verify_alpha_channel(frame)
    out = verify_alpha_channel(out)
    cv2.addWeighted(out, 0.25, frame, 1.0, .23, frame)
    return frame
