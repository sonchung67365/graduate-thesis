from flask import Flask, render_template
from datetime import timedelta
from time import sleep
#import test_l298 as L298
#import RPiSim.GPIO as GPIO

IN_1 = 17
IN_2 = 27
IN_3 = 22
IN_4 = 23

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/sensor')
def sensor():
    return render_template('index.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/up')
def up():
    print("up")
    return render_template('control.html')

@app.route('/back')
def back():
    print("back")
    return render_template('control.html')

@app.route('/turn-left')
def turn_left():
    print("turn left")
    return render_template('control.html')

@app.route('/turn-right')
def turn_right():
    print("turn right")
    return render_template('control.html')

@app.route('/stop')
def stop():
    print("stop")
    return render_template('control.html')


# Run the app on the local development server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8715", debug=True)