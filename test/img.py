import cv2
import base64

cam = cv2.VideoCapture(0)

# cam.read() returns an array of (status, img_array)
ret, frame = cam.read()
cv2.imwrite('capture.jpg', frame)

print(ret, '\n',frame,'\n\n\n\n\n')
print(len(open('capture.jpg', 'rb').read()), '\n\n\n\n\n\n\n')

print(len(cv2.imencode('.jpg', frame)[1].tobytes()))

# retval, buffer = cv2.imencode('.jpg', frame)
# print(buffer.tostring())

# print(base64.b64encode(frame[0]),'\n\n\n\n\n')


# cam.release()
# ret,frame = cam.read()
# print(frame)