import cv2
import numpy as np


def find_organism(arr):

    # Load infrared image
    obj = False
    # image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    image = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to identify potential organisms
    _, thresholded = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        obj = True
        # Draw contours on the original image
        result = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
        # Display the result
        cv2.imshow('Organism Detection', result)
        cv2.waitKey(1)
        #cv2.destroyAllWindows()
        
    return obj