import cv2

#No grayscale at all, just grabbing pure raw frames from camera
print("Starting")
cv2.namedWindow('window', cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully")

while True:
    ret, frame = cap.read()
    print("test")
    if ret:
        cv2.imshow('Frame', frame)
        print("Frame detected!")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
