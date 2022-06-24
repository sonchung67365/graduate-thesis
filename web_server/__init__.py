from flask import Flask, render_template




def check():
    print("CHECK WEB_SERVER !")


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/home')
    def index():
        return render_template('index.html')

    @app.route('/sensor')
    def sensor():
        temp = "lấy giá trị nhiệt độ" #thay bằng hàm lấy giá trị
        humi = "lấy giá trị độ ẩm" #thay bằng hàm lấy giá trị
        return render_template('sensor.html', temp=temp, humi=humi)

    #control -----------------------------------------------------------------
    from module import check
    check()

    @app.route('/control')
    def control():
        return render_template('control.html')

    @app.route('/up')
    def up():
        print("up")
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/back')
    def back():
        print("back")
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/turn-left')
    def turn_left():
        print("turn left")
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/turn-right')
    def turn_right():
        print("turn right")
        # thêm lệnh điều khiển
        return render_template('control.html')

    @app.route('/stop')
    def stop():
        print("stop")
        # thêm lệnh điều khiển
        return render_template('control.html')


    return app