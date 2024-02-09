import cv2


cap = cv2.VideoCapture(0)



if not cap.isOpened():
    print("error: could not open camera")
    exit()

print("Hello world!")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow()
        print("frame detected!")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()