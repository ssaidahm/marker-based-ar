# Saidahmed Saidahmed
# Create new marker ids

import cv2 as cv
import numpy as np

# Load the predefined dictionary
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Generate the marker
markerImage = np.zeros((200, 200), dtype=np.uint8)
markerImage33 = cv.aruco.drawMarker(dictionary, 25, 200, markerImage, 1)

markerImage1 = np.zeros((200, 200), dtype=np.uint8)
markerImage25 = cv.aruco.drawMarker(dictionary, 33, 200, markerImage1, 1)

markerImage2 = np.zeros((200, 200), dtype=np.uint8)
markerImage30 = cv.aruco.drawMarker(dictionary, 30, 200, markerImage2, 1)

markerImage3 = np.zeros((200, 200), dtype=np.uint8)
markerImage23 = cv.aruco.drawMarker(dictionary, 23, 200, markerImage3, 1)

cv.imwrite("25.jpg", markerImage25)
cv.imwrite("33.jpg", markerImage33)
cv.imwrite("30.jpg", markerImage30)
cv.imwrite("23.jpg", markerImage23)