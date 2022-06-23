from web_server import create_app


app = create_app()



if __name__ == '__main__':
    app.run(host="192.168.33.105", port="7022", debug=True)