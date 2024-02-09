import cv2
from detect import find_organism


def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Loop to capture frames
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
        # Display the resulting frame
            
            if find_organism(frame) == True:
                cv2.imshow('Frame', frame)
                # Check for key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break



    # Release the VideoCapture object and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "main":
    main()