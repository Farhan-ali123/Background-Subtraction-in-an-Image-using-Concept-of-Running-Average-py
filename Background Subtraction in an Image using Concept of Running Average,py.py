# Python program to illustrate
# Background subtraction using
# concept of Running Averages

# organize imports
import cv2
import numpy as np

# capture frames from a camera
cap = cv2.VideoCapture(0)

# read the frames from the camera
_, img = cap.read()

# modify the data type
# setting to 32-bit floating point
averageValue1 = np.float32(img)

# loop runs if capturing has been initialized.
while (1):
    # reads frames from a camera
    _, img = cap.read()

    # using the cv2.accumulateWeighted() function
    # that updates the running average
    cv2.accumulateWeighted(img, averageValue1, 0.02)

    # converting the matrix elements to absolute values
    # and converting the result to 8-bit.
    resultingFrames1 = cv2.convertScaleAbs(averageValue1)

    # Show two output windows
    # the input / original frames window
    cv2.imshow('InputWindow', img)

    # the window showing output of alpha value 0.02
    cv2.imshow('averageValue1', resultingFrames1)

    # Wait for Esc key to stop the program
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
