import cv2
from detect import find_organism


# Create VideoCapture object
cap = cv2.VideoCapture(0)

#Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

#Loop to capture frames
while True:
    #Grabs frame in numpy array, and grabs if frame was successfully captured
    ret, frame = cap.read()

    if ret:
    #Display the resulting frame
        print("Frame detected!")
        if_contours = find_organism(frame)
        cv2.imshow("Frame", if_contours)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'): #Spam q to break loop, only waits a millisecond 
            break


#Release VideoCapture object and close all windows. It's important this happens else we get memory leaks. Only known solution is rebooting the pi 
cap.release()
cv2.destroyAllWindows()
