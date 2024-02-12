import cv2

#Cleans memory leak
cap = cv2.VideoCapture(0)

cap.release()
cv2.destroyAllWindows()