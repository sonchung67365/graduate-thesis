from flask import Blueprint, request, render_template




control = Blueprint("control", __name__)

@control.route('/control-motor', methods=['GET', 'POST'])
def control_motor():
    # Get speed value
    speed = request.form['speed']
    # Print value
    print(int(speed))

    # Get direction value
    dir = request.form['dir']
    # Print
    print("Chiều quay " + dir)

    return render_template('user.html')

@control.route('/stop-motor')
def stop_motor():
    print("Stop Motor")
    
    return render_template('user.html')

@control.route('/1')
def forward():
    print("Forward")
    #motor.move()
    return render_template('home.html')


@control.route('/2')
def reverse():
    print("Reverse")
    #motor.move(-50)
    return render_template('home.html')


@control.route('/3')
def left():
    print("Left")
    #motor.move(100,50)
    return render_template('home.html')


@control.route('/4')
def right():
    print("Right")
    #motor.move(100,-50)
    return render_template('home.html')


@control.route('/5')
def stop():
    print("Stop")
    #motor.stop()
    return render_template('home.html')