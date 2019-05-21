import tkinter as tk
from tkinter import *


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self, width=800, height=600)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (MainPage, DataEntryForm):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelun = tk.Label(self, text='Username')
        labelun.grid(row=0, column=0)
        labelpw = tk.Label(self, text='Password')
        labelpw.grid(row=1, column=0)

        uname_entry = tk.Entry(self, textvariable=StringVar())
        uname_entry.grid(row=0, column=1, columnspan=2)
        pword_entry = tk.Entry(self, textvariable=StringVar())
        pword_entry.grid(row=1, column=1, columnspan=2)

        butenter = tk.Button(self, text='Enter', padx=22, command=lambda: controller.show_frame(DataEntryForm))
        butenter.grid(row=2, column=1)
        butquit = tk.Button(self, text='Quit', padx=22, command=self.quit)
        butquit.grid(row=2, column=2)


class DataEntryForm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.reglist = []
        self.prelist = []
        self.dieslist = []
        titlelabel = tk.Label(self, text='Sales Data Entry Form', font='Verdana, 16')
        titlelabel.grid(row=0, column=1, columnspan=4)
        datelabel = tk.Label(self, text='Enter Date', font='Verdana, 12')
        datelabel.grid(row=1, column=0)
        self.dateentry = tk.Entry(self, textvariable=StringVar())
        self.dateentry.grid(row=1, column=1, sticky='w')

        openlabel = tk.Label(self, text='Open', font='Verdana, 12')
        openlabel.grid(row=2, column=1)
        deliverylabel = tk.Label(self, text='Delivery', font='Verdana, 12')
        deliverylabel.grid(row=2, column=2)
        totallabel = tk.Label(self, text='Total', font='Verdana, 12')
        totallabel.grid(row=2, column=3)
        saleslabel = tk.Label(self, text='Sales', font='Verdana, 12')
        saleslabel.grid(row=2, column=4)
        closelabel = tk.Label(self, text='Close', font='Verdana, 12')
        closelabel.grid(row=2, column=5)
        reglabel = tk.Label(self, text='Regular', font='Verdana, 12', padx=0, pady=4)
        reglabel.grid(row=3, column=0, sticky='e')
        prelabel = tk.Label(self, text='Premium', font='Verdana, 12', padx=0, pady=4)
        prelabel.grid(row=4, column=0, sticky='e')
        dieslabel = tk.Label(self, text='Diesel', font='Verdana, 12', padx=0, pady=4)
        dieslabel.grid(row=5, column=0, sticky='e')

        self.regopenentry = tk.Entry(self, textvariable=StringVar())
        self.regopenentry.grid(row=3, column=1, padx=3, pady=4)
        self.regdeliveryentry = tk.Entry(self, textvariable=StringVar())
        self.regdeliveryentry.grid(row=3, column=2, padx=3, pady=4)
        self.regtotalentry = tk.Entry(self, textvariable=StringVar())
        self.regtotalentry.grid(row=3, column=3, padx=3, pady=4)
        self.regsalesentry = tk.Entry(self, textvariable=StringVar())
        self.regsalesentry.grid(row=3, column=4, padx=3, pady=4)
        self.regcloseentry = tk.Entry(self, textvariable=StringVar())
        self.regcloseentry.grid(row=3, column=5, padx=3, pady=4)

        self.preopenentry = tk.Entry(self, textvariable=StringVar())
        self.preopenentry.grid(row=4, column=1, padx=3, pady=4)
        self.predeliveryentry = tk.Entry(self, textvariable=StringVar())
        self.predeliveryentry.grid(row=4, column=2, padx=3, pady=4)
        self.pretotalentry = tk.Entry(self, textvariable=StringVar())
        self.pretotalentry.grid(row=4, column=3, padx=3, pady=4)
        self.presalesentry = tk.Entry(self, textvariable=StringVar())
        self.presalesentry.grid(row=4, column=4, padx=3, pady=4)
        self.precloseentry = tk.Entry(self, textvariable=StringVar())
        self.precloseentry.grid(row=4, column=5, padx=3, pady=4)

        self.diesopenentry = tk.Entry(self, textvariable=StringVar())
        self.diesopenentry.grid(row=5, column=1, padx=3, pady=4)
        self.diesdeliveryentry = tk.Entry(self, textvariable=StringVar())
        self.diesdeliveryentry.grid(row=5, column=2, padx=3, pady=4)
        self.diestotalentry = tk.Entry(self, textvariable=StringVar())
        self.diestotalentry.grid(row=5, column=3, padx=3, pady=4)
        self.diessalesentry = tk.Entry(self, textvariable=StringVar())
        self.diessalesentry.grid(row=5, column=4, padx=3, pady=4)
        self.diescloseentry = tk.Entry(self, textvariable=StringVar())
        self.diescloseentry.grid(row=5, column=5, padx=3, pady=4)

        butsavedata = tk.Button(self, text='Save', width=10, command=self.savedata)
        butsavedata.grid(row=6, column=5)
        butquit = tk.Button(self, text='Quit', width=10, command=self.quit)
        butquit.grid(row=6, column=4)

    def savedata(self):
        regulardata = self.regopenentry.get()
        self.reglist.append(regulardata)
        regulardata = self.regdeliveryentry.get()
        self.reglist.append(regulardata)
        regulardata = self.regtotalentry.get()
        self.reglist.append(regulardata)
        regulardata = self.regsalesentry.get()
        self.reglist.append(regulardata)
        regulardata = self.regcloseentry.get()
        self.reglist.append(regulardata)
        premiumdata = self.preopenentry.get()
        self.prelist.append(premiumdata)
        premiumdata = self.predeliveryentry.get()
        self.prelist.append(premiumdata)
        premiumdata = self.pretotalentry.get()
        self.prelist.append(premiumdata)
        premiumdata = self.presalesentry.get()
        self.prelist.append(premiumdata)
        premiumdata = self.precloseentry.get()
        self.prelist.append(premiumdata)
        dieseldata = self.diesopenentry.get()
        self.dieslist.append(dieseldata)
        dieseldata = self.diesdeliveryentry.get()
        self.dieslist.append(dieseldata)
        dieseldata = self.diestotalentry.get()
        self.dieslist.append(dieseldata)
        dieseldata = self.diessalesentry.get()
        self.dieslist.append(dieseldata)
        dieseldata = self.diescloseentry.get()
        self.dieslist.append(dieseldata)
        dateentered = self.dateentry.get()
        open('RegularData.txt', 'a').write(dateentered + '   ' + '   '.join([str(i) for i in self.reglist]) + '\n')
        open('PremiumData.txt', 'a').write(dateentered + '   ' + '   '.join([str(i) for i in self.reglist]) + '\n')
        open('DieselData.txt', 'a').write(dateentered + '   ' + '   '.join([str(i) for i in self.reglist]) + '\n')
        self.reglist = []
        self.prelist = []
        self.dieslist = []


my_gui = Application()
my_gui.mainloop()
