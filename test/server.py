from flask import Flask,render_template, Response
import cv2

cam = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(): 
    while True: 
        ret, frame = cam.read() 
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n')
        # cv2.imwrite('capture.jpg', frame) 
        # yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + open('capture.jpg', 'rb').read() + b'\r\n')

@app.route('/videoFeed') 
def video_feed(): 
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True, threaded=True)