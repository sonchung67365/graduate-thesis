from flask import Flask, render_template




def check():
    print("CHECK WEB_SERVER !")


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/home')
    def index():
        return render_template('index.html')

    #sensor ------------------------------------------------------------------
    from module import uart_arduino
    arduino = uart_arduino.Arduino()

    @app.route('/sensor')
    def sensor():
        data = arduino.get_data_split()
        print(data)
        humi = data[0] #thay bằng hàm lấy giá trị
        temp = data[1] #thay bằng hàm lấy giá trị
        lamp = data[2] #thay bằng hàm lấy giá trị
        pin = data[3] #thay bằng hàm lấy giá trị
        distance = data[4] #thay bằng hàm lấy giá trị
        return render_template('sensor.html', 
            temp=temp, 
            humi=humi, 
            lamp=lamp, 
            pin=pin, 
            distance=distance)

    #control -----------------------------------------------------------------
    from module import l298
    motor1 = l298.Motor(17,27)
    motor2 = l298.Motor(22,23)

    @app.route('/control')
    def control():
        
        return render_template('control.html')

    @app.route('/up')
    def up():
        print("up")
        # thêm lệnh điều khiển
        motor1.moveF()
        motor2.moveF()
        return render_template('control.html')

    @app.route('/back')
    def back():
        print("back")
        motor1.moveB()
        motor2.moveB()
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/turn-left')
    def turn_left():
        print("turn left")
        motor1.moveF()
        motor2.stop()
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/turn-right')
    def turn_right():
        print("turn right")
        motor1.stop()
        motor2.moveF()
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/stop')
    def stop():
        print("stop")
        motor1.stop()
        motor2.stop()
        # thêm lệnh điều khiển
        return render_template('control.html')


    return app