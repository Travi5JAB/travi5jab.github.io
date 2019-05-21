"""A GUI with three counter buttons"""
from tkinter import *

myfont = ("Arial", 16, "bold")

window = Tk()
window.title("Three counters")
window.geometry("300x120")

frame = Frame(window)
frame.grid()

# Construct three buttons:
button0 = Button(frame, font = ("Arial", 14, "bold"), text = "0",
                 fg = "blue", bg = "white", width = 4, height = 2)
button0.grid(row = 1, column = 0, padx = 10, pady = 10 )

button1 = Button(frame, font = ("Arial", 14, "bold"), text = "0",
                 fg = "blue", bg = "white", width = 4, height = 2)
button1.grid(row = 1, column = 1, padx = 10, pady = 10 )

button2 = Button(frame, font = ("Arial", 14, "bold"), text = "0",
                 fg = "blue", bg = "white", width = 4, height = 2)
button2.grid(row = 1, column = 2, padx = 10, pady = 10 )

#Construct three event-handling functions for the three buttons:
count0 = 0
def handle0() :
    global count0
    count0 = count0 + 1
    button0.configure(text = str(count0))
button0.configure(text = str(count0), command = handle0)

count1 = 0
def handle1() :
    global count1
    count1 = count1 + 1
    button1.configure(text = str(count1))
button1.configure(text = str(count1), command = handle1)

count2 = 0
def handle2() :
    global count2
    count2 = count2 + 1
    button2.configure(text = str(count2))
button2.configure(text = str(count2), command = handle2)

window.mainloop()
