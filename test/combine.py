import cv2 
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cv2.imshow("original", frame)

left = frame[0: , 0: -300]
cv2.imshow("left", left)

right = frame[0: , 300: ]
cv2.imshow("right", right)

cv2.waitKey(0)