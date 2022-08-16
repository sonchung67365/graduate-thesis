from sqlalchemy import true
from web_server import create_app
from gui import test, create_gui
import threading
from time import sleep





host_name = "localhost"
port = 8000

app = create_app()


def gui_test():
    top = test()
    top.mainloop()

def gui():
    w = create_gui()
    w.mainloop()



if __name__ == '__main__':
    
    app.run(host=host_name, port=port, debug=True)
