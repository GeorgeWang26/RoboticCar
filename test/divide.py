import cv2

img = cv2.imread("capture.jpg")
cv2.imshow("original", img)
height, width, channels = img.shape

print(height, width, channels)
print(img,"\n\n----------------------------------------")
print(img[0],"\n\n----------------------------------------")
print(img[0][0],"\n\n----------------------------------------")
print(img[0][0][0],"\n\n----------------------------------------")



# h720 * w1280
# crop_img = img[y:y+h, x:x+w]
left = img[0: , 0:-300].copy()
cv2.imshow("left", left)

right = img[0: , 300: ].copy()
cv2.imshow("right", right)
cv2.waitKey(0)