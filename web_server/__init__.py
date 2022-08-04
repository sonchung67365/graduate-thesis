from turtle import distance
from flask import Flask, render_template, jsonify
from flask_basicauth import BasicAuth
import random



def check():
    print("CHECK WEB_SERVER !")


def create_app():
    app = Flask(__name__)

    app.config['BASIC_AUTH_USERNAME'] = 'admin'
    app.config['BASIC_AUTH_PASSWORD'] = 'admin'
    app.config['BASIC_AUTH_FORCE'] = True

    basic_auth = BasicAuth(app)

    @app.route('/')
    @app.route('/home')
    def index():
        return render_template('index.html')



    # sensor update data -----------------------------------------------
    
    @app.route('/_data-sensor')
    def data_sensor():
        temp = random.randrange(1,40)
        humi = random.randrange(1,50)
        light = random.randrange(0,2)
        if light == 0: lamp = "Tắt"
        else : lamp = "Bật"
        pin = random.randrange(1,100)
        distance = random.randrange(1,500)
        goods = random.randrange(0,2)
        if goods == 0: hasgoods = "Có"
        else : hasgoods = "Không"
        return jsonify(
            temp=temp,
            humi=humi, 
            lamp=lamp, 
            pin=pin, 
            distance=distance, 
            hasgoods=hasgoods
        )

    @app.route('/sensor')
    def sensor():
        temp = "lấy giá trị nhiệt độ" #thay bằng hàm lấy giá trị
        humi = "lấy giá trị độ ẩm" #thay bằng hàm lấy giá trị
        lamp = "lấy giá trị độ ẩm" #thay bằng hàm lấy giá trị
        pin = "lấy giá trị độ ẩm" #thay bằng hàm lấy giá trị
        distance = "lấy giá trị độ ẩm" #thay bằng hàm lấy giá trị
        hasgoods = "lấy giá trị độ ẩm" #thay bằng hàm lấy giá trị
        return render_template('sensor.html', temp=temp, humi=humi, lamp=lamp, pin=pin, distance=distance, hasgoods=hasgoods)

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