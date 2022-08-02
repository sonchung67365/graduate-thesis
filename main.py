from sqlalchemy import true
from web_server import create_app
from gui import test, create_gui
import threading
from time import sleep





host_name = "0.0.0.0"
port = 5027

app = create_app()


def gui_test():
    top = test()
    top.mainloop()

def gui():
    w = create_gui()
    w.mainloop()



if __name__ == '__main__':
    try:
        #threading.Thread(target=gui, daemon=True).start()
        app.run(host=host_name, port=port, debug=True, use_reloader=False)
        #threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()

        #f = open("data/test.txt", "r")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")
        
        #print(f.read())
        while true:
            sleep(1)
