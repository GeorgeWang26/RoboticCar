from flask import Flask,render_template, Response
import cv2

cam = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('rightIndex.html')

def rightStream(): 
    while True: 
        ret, frame = cam.read()
        rightFrame = frame[0: , 700: ]
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', rightFrame)[1].tobytes() + b'\r\n')


@app.route('/rightVideoFeed') 
def rightVideoFeed(): 
    return Response(rightStream(), mimetype='multipart/x-mixed-replace; boundary=frame') 

if __name__ == '__main__': 
    app.run(port = 9000, host='0.0.0.0', debug=True, threaded=True)