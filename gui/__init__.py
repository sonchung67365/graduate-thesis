from msilib.schema import Class
import tkinter as tk

def test():
    top = tk.Tk()
    return top

def check():
    print("CHECK GUI !")

def create_gui():
    root = Gui("Đồ Án Tốt Nghiệp")

    return root




class Gui(tk.Tk):
    font1 = ('Helvetica', 20, "bold")
    font2 = ("Helvetica", 15, "bold")
    font3 = ("Helvetica", 11, "bold")

    a=520
    b=100



    def __init__(self, title=None):
        super().__init__()

        self.title(title)
        self.geometry('1300x700')


        tk.Label(self, text="Hàng", font=self.font2).place(relx=0.5, rely=0.1)
        tk.Label(self, text="Độ ẩm", font=self.font2).place(relx=0.5, rely=0.2)
        tk.Label(self, text="Trạng thái đèn", font=self.font2).place(relx=0.7, rely=0.2)
        tk.Label(self, text="Nhiệt độ", font=self.font2).place(relx=0.5, rely=0.3)
        tk.Label(self, text="Pin", font=self.font2).place(relx=0.7, rely=0.3)
        tk.Label(self, text="Cảnh báo khoảng cách", font=self.font2).place(relx=0.5, rely=0.4)
        tk.Label(self, text="Tốc độ động cơ", font=self.font2).place(relx=0.5, rely=0.5)
        tk.Label(self, text="FPS GUI", font=self.font2).place(relx=0.2, rely=0.7)


        v=tk.IntVar()
        tk.Label(self, text="Các trạng thái hoạt động", font=self.font2).place(relx=0.5, rely=0.6)
        tk.Radiobutton(self, text="Dò line", variable=v, value=1, font=self.font3).place(relx=0.7, rely=0.6)
        tk.Radiobutton(self, text="Điều khiển bằng tay",variable=v, value=2, font=self.font3).place(relx=0.7, rely=0.64)
        tk.Radiobutton(self, text="Khóa",variable=v, value=3,font=self.font3).place(relx=0.7, rely=0.68)


        var = tk.DoubleVar()
        speed_motor_scale = tk.Scale(self, variable=var, orient=tk.HORIZONTAL, length=150).place(relx=0.7, rely=0.48)









class Label(tk.Tk):
    font1 = ('Helvetica', 20, "bold")
    font2 = ("Helvetica", 15, "bold")
    font3 = ("Helvetica", 11, "bold")

    def __init__(self, root, text, x, y):
        tk.Label(root, text=text, font=self.font2).place(relx=x, relxy=y)

