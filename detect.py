import cv2
import numpy as np

#Gets numpy array of pixels from main.py
def find_organism(arr):
    #Converts to gray scale
    image = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
    #Adds gaussian blur to array
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    #Apply thresholding to identify potential organisms
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)    

    # Find contours in the thresholded image, the contours that are found are potential organisms
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours: #If countours were found
        #Draw contours on the grayscaled image
        result = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
        #Tell console organism detected
        print("Organism Detected!")
        return result
        #cv2.destroyAllWindows()
        
    print("No organism detected!")
    return thresholded