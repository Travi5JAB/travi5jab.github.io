
from tkinter import *
class Class1:
    def __init__(self):
        obj1= Class2()
        self.root = Tk()
        self.root.title("test window")
        self.can1=Canvas(self.root, width=500, height=510, bg="black")
        self.can1.pack(expand=False, fill=X)
        self.label1 = Label(self.can1, text =obj1.datetimetodayday , bg = 'black',
                       fg= 'red',font=('Arial Black', 14))
        self.can1.create_window(20,20, window=self.label1, anchor= NW)
class Class2:
    import datetime
    def __init__(self):
        pass
    
    def datetimetodayday(self):
        tdate=datetime.datetime.now()
        tdateday = str(tdate.day)
        if len(tdateday)==1:
            tdateday= "0"+tdateday
gui=Class1()
gui.root.mainloop()
