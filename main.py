import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

# load model
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\demir\\Projects\\Drowsiness_Detection\\best.pt', force_reload=True)

"""
# make detection with images
img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Cars_in_traffic_in_Auckland%2C_New_Zealand_-_copyright-free_photo_released_to_public_domain.jpg/800px-Cars_in_traffic_in_Auckland%2C_New_Zealand_-_copyright-free_photo_released_to_public_domain.jpg'

results = model(img)
results.print()

plt.imshow(np.squeeze(results.render()))
plt.show()

results.render()
"""

# real time detection

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()