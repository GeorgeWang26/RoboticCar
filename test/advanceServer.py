from flask import Flask,render_template, Response
import cv2

cam = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('advanceIndex.html')

def left():
    while True:
        ret, frame = cam.read()
        left = frame[0: , 0:-300]
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', left)[1].tobytes() + b'\r\n')

def right():
    while True:
        ret, frame = cam.read()
        right = frame[0: , 300: ]
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', right)[1].tobytes() + b'\r\n')

@app.route('/leftStream')
def leftStream():
    return Response(left(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/rightStream')
def rightStream():
    return Response(right(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)