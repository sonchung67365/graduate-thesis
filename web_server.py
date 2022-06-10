from flask import Flask, render_template, redirect, url_for, request, session, flash, make_response
from datetime import timedelta, datetime
from time import sleep
import test_l298 as L298
import RPi.GPIO as GPIO

IN_1 = 17
IN_2 = 27
IN_3 = 22
IN_4 = 23

app = Flask(__name__)
app.config['SECRET_KEY'] = "batchedobaylen"
app.permanent_session_lifetime = timedelta(minutes=5)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor = L298.MotorRobot(IN_1, IN_2, IN_3, IN_4)

 
@app.route('/')
def welcome():
    now = datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
    'title' : 'HELLO!',
    'time' : timeString
    }
    return render_template('home.html', **templateData)
 
 
@app.route('/home')
def home():
    return render_template('home.html', tem=50, humi=20, status="Tự động")


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Thông tin không hợp lệ. Vui lòng thử lại.'
        else:
            session.permanent = True
            # Get username value
            user_name = request.form['username']
            session["user"] = user_name
            return redirect(url_for('user'))
    if "user" in session:
        name = session["user"]
        flash("Bạn đã đăng nhập!", 'info')
        return render_template('user.html', name=name)
    return render_template('login.html', error=error)


@app.route('/user')
def user(name=None):
    if "user" in session:
        name = session["user"]
        return render_template('user.html', name=name)
        
    else:
        flash("Bạn chưa đăng nhập!", 'danger')
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop("user", None)
    return render_template('home.html')


@app.route('/control-motor', methods=['GET', 'POST'])
def control_motor():
    # Get speed value
    speed = request.form['speed']
    # Print value
    print(int(speed))
    motor.move(speed=int(speed), t=0)


    # Get direction value
    dir = request.form['dir']
    # Print
    print("Chiều quay " + dir)

    return render_template('user.html')

@app.route('/stop-motor')
def stop_motor():
    print("Stop Motor")
    motor.stop()
    return render_template('user.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int
    if changePin == 1:
        print ("Left")
        
    elif changePin == 2:
        print ("Forward")
        
    elif changePin == 3:
        print ("Right")
        
    elif changePin == 4:
        print ("Reverse")
        
    else:
        pass
    response = make_response(redirect(url_for('index')))
    return(response)

# Run the app on the local development server
if __name__ == '__main__':
    app.run(host="192.168.1.170", port="2000" ,debug=True)