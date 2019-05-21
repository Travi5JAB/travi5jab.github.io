from tkinter import *
import os
import json
from tkinter import *
import tkinter as tk
from tkinter import ttk, Menu


LARGE_FONT = ("Verdana", 20, 'bold')

class HomePage(tk.Frame):
        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text="Home Page",font= LARGE_FONT)
                label.grid(row = 0, column = 3, pady=10,padx=10)
                self.controller=controller

                self.btn_MQ = ttk.Button(self, text="Make a Quiz",
                                   command = lambda: controller.show_frame(Q1Page))
                self.btn_MQ.grid(row = 1, column = 0, pady=10,padx=10) #button to make quiz page

                self.btn_TQ = ttk.Button(self, text="Take a Quiz",
                                   command = lambda: controller.show_frame(A1Page))
                self.btn_TQ.grid(row = 2, column = 0, pady=10,padx=10) #button to take quiz page

                self.btn_MyQ = ttk.Button(self, text="My Quizzes",
                                   command = lambda: controller.show_frame(MyQuizzes))
                self.btn_MyQ.grid(row = 3, column = 0, pady=10,padx=10) #button to view quizzes

                btn_LI = ttk.Button(self, text="LogIN",
                        command = lambda: controller.show_frame(Login))
                btn_LI.grid(row = 0, column = 5, pady=10,padx=10)


class Q1Page(tk.Frame):

        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text="Question 1",font= LARGE_FONT)
                label.grid(row = 0, column = 1, pady=10,padx=10)
                self.controller=controller


                self.StV_q1 = tk.StringVar()
                self.StV_a1 = tk.StringVar()
                self.StV_b1 = tk.StringVar()
                self.StV_c1 = tk.StringVar()
                self.StV_d1 = tk.StringVar()

                StV_q1 = self.StV_q1
                StV_a1 = self.StV_a1
                StV_b1 = self.StV_b1
                StV_c1 = self.StV_c1
                StV_d1 = self.StV_d1

                labelQ = ttk.Label(self, text = "enter Question") #text before box
                labelQ.grid(row = 1, column = 0)

                userEntry_qq1 = tk.Entry(self, width = 26, textvariable = StV_q1)
                userEntry_qq1.grid(row = 1, column = 1)

                labelPrompt = tk.Label(self, text = "Question...") #input from labelQ
                labelPrompt.grid(row = 1, column = 2)

                labelA = tk.Label(self, text = "enter Option A") #text before box
                labelA.grid(row = 2, column = 0)

                userEntry_aq1 = tk.Entry(self, width = 26, textvariable = StV_a1)
                userEntry_aq1.grid(row = 2, column = 1)

                labelPromptA = tk.Label(self, text = "A is...") #input from labelA
                labelPromptA.grid(row = 2, column = 2)

                labelB = tk.Label(self, text = "enter Option B") #text before box
                labelB.grid(row = 4, column = 0)

                userEntry_bq1 = tk.Entry(self, width = 26, textvariable = StV_b1)
                userEntry_bq1.grid(row = 4, column = 1)

                labelPromptB = tk.Label(self, text = "B is...") #input from labelB
                labelPromptB.grid(row = 4, column = 2)

                labelC = tk.Label(self, text = "enter Option C") #text before box
                labelC.grid(row = 6, column = 0)

                userEntry_cq1 = tk.Entry(self, width = 26, textvariable = StV_c1)
                userEntry_cq1.grid(row = 6, column = 1)

                labelPromptC = tk.Label(self, text = "C is...") #input from labelC
                labelPromptC.grid(row = 6, column = 2)

                labelD = tk.Label(self, text = "enter Option D") #text before box
                labelD.grid(row = 8, column = 0)

                userEntry_dq1 = tk.Entry(self, width = 26, textvariable = StV_d1)
                userEntry_dq1.grid(row = 8, column = 1)

                labelPromptD = tk.Label(self, text = "D is...") #input from labelD
                labelPromptD.grid(row = 8, column = 2)


                def action_all():
                        labelPrompt.configure(text = StV_q1.get())
                        labelPromptA.configure(text = StV_a1.get())
                        labelPromptB.configure(text = StV_b1.get())
                        labelPromptC.configure(text = StV_c1.get())
                        labelPromptD.configure(text = StV_d1.get())
                        controller.show_frame(Q2Page)


                btn_Sub = ttk.Button(self, text = "Submit", command = action_all)
                btn_Sub.grid(row = 10, column = 4)

                btn_GH = ttk.Button(self, text="Go Home",
                        command = lambda: controller.show_frame(HomePage))
                btn_GH.grid(row = 11, column = 4)


class Q2Page(tk.Frame):
        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text="Question 2",font= LARGE_FONT)
                label.grid(row = 0, column = 1, pady=10,padx=10)
                self.controller=controller

                self.StV_q = tk.StringVar()
                self.StV_a = tk.StringVar()
                self.StV_b = tk.StringVar()
                self.StV_c = tk.StringVar()
                self.StV_d = tk.StringVar()

                StV_q = self.StV_q
                StV_a = self.StV_a
                StV_b = self.StV_b
                StV_c = self.StV_c
                StV_d = self.StV_d


                labelQ = tk.Label(self, text = "enter Question") #text before box
                labelQ.grid(row = 1, column = 0)

                userEntry = tk.Entry(self, width = 26, textvariable = StV_q)
                userEntry.grid(row = 1, column = 1)

                labelPrompt = tk.Label(self, text = "Question...") #input from labelQ
                labelPrompt.grid(row = 1, column = 2)

                labelA = tk.Label(self, text = "enter Option A") #text before box
                labelA.grid(row = 2, column = 0)

                userEntry = tk.Entry(self, width = 26, textvariable = StV_a)
                userEntry.grid(row = 2, column = 1)

                labelPromptA = tk.Label(self, text = "A is...") #input from labelA
                labelPromptA.grid(row = 2, column = 2)

                labelB = tk.Label(self, text = "enter Option B") #text before box
                labelB.grid(row = 4, column = 0)

                userEntry = tk.Entry(self, width = 26, textvariable = StV_b)
                userEntry.grid(row = 4, column = 1)

                labelPromptB = tk.Label(self, text = "B is...") #input from labelB
                labelPromptB.grid(row = 4, column = 2)

                labelC = tk.Label(self, text = "enter Option C") #text before box
                labelC.grid(row = 6, column = 0)

                userEntry = tk.Entry(self, width = 26, textvariable = StV_c)
                userEntry.grid(row =6, column = 1)

                labelPromptC = tk.Label(self, text = "C is...") #input from labelC
                labelPromptC.grid(row = 6, column = 2)

                labelD = tk.Label(self, text = "enter Option D") #text before box
                labelD.grid(row = 8, column = 0)

                userEntry = tk.Entry(self, width = 26, textvariable = StV_d)
                userEntry.grid(row = 8, column = 1)

                labelPromptD = tk.Label(self, text = "D is...") #input from labelD
                labelPromptD.grid(row = 8, column = 2)


                def action_all():
                        labelPrompt.configure(text = StV_q.get())
                        labelPromptA.configure(text = StV_a.get())
                        labelPromptB.configure(text = StV_b.get())
                        labelPromptC.configure(text = StV_c.get())
                        labelPromptD.configure(text = StV_d.get())
                        controller.show_frame(A1Page)

                btn_Sub = ttk.Button(self, text = "Submit", command = action_all)
                btn_Sub.grid(row = 10, column = 3)

                btn_PrevP = ttk.Button(self, text="Previous Page",
                        command = lambda: controller.show_frame(Q1Page))
                btn_PrevP.grid(row = 12, column = 2)

                btn_GH = ttk.Button(self, text="Go Home",
                        command = lambda: controller.show_frame(HomePage))
                btn_GH.grid(row = 12, column = 3)


class A1Page(tk.Frame):
        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text="Test: Question #1",font= LARGE_FONT)
                label.grid(row = 0, column = 3, pady=10,padx=10)
                self.controller=controller

                def action_wrong(): #wrong answer
                        print("Incorrect")
                        controller.show_frame(A2Page)
                def action_correct():	#right answer
                        print("Correct")
                        controller.show_frame(A2Page)

                labelQ = tk.Label(self, text = "Question: ") #text before box
                labelQ.grid(row = 1, column = 0)

                labelQuestion = tk.Label(self, text = "is..") #input from labelQ
                labelQuestion.grid(row = 1, column = 2)

                labelA = tk.Label(self, text = "A: ") #text before box
                labelA.grid(row = 2, column = 1)

                btn_a = ttk.Button(self, text="A", command=action_correct)
                btn_a.grid(row = 2, column = 0)

                labelAnswerA = tk.Label(self, text = "is...") #input from labelA
                labelAnswerA.grid(row = 2, column = 2)

                labelB = tk.Label(self, text = "B: ") #text before box
                labelB.grid(row = 4, column = 1)

                btn_b = ttk.Button(self, text="B", command=action_wrong)
                btn_b.grid(row = 4, column = 0)

                labelAnswerB = tk.Label(self, text = "is...") #input from labelB
                labelAnswerB.grid(row = 4, column = 2)

                labelC = tk.Label(self, text = "C: ") #text before box
                labelC.grid(row = 6, column = 1)

                btn_c = ttk.Button(self, text="C", command=action_wrong)
                btn_c.grid(row = 6, column = 0)

                labelAnswerC = tk.Label(self, text = "is...") #input from labelC
                labelAnswerC.grid(row = 6, column = 2)

                labelD = tk.Label(self, text = "D: ") #text before box
                labelD.grid(row = 8, column = 1)

                btn_d = ttk.Button(self, text="D", command=action_wrong)
                btn_d.grid(row = 8, column = 0)

                labelAnswerD = tk.Label(self, text = "is...") #input from labelD
                labelAnswerD.grid(row = 8, column = 2)

                btn_GH = ttk.Button(self, text="Go Home",
                        command = lambda: controller.show_frame(HomePage))
                btn_GH.grid(row = 10, column = 3)


class A2Page(tk.Frame):
        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text="Test: Question #2",font= LARGE_FONT)
                label.grid(row = 0, column = 3, pady=10,padx=10)
                self.controller=controller

                def action_wrong(): #wrong answer
                        print("Incorrect")
                        controller.show_frame(A2Page)
                def action_correct():	#right answer
                        print("Correct")
                        controller.show_frame(A2Page)

                labelQ = tk.Label(self, text = "Question") #text before box
                labelQ.grid(row = 1, column = 1)

                labelQuestion = tk.Label(self, text = "Q") #input from labelQ
                labelQuestion.grid(row = 1, column = 2)

                labelA = tk.Label(self, text = "A: ") #text before box
                labelA.grid(row = 2, column = 1)

                btn_a = ttk.Button(self, text="A", command=action_correct)
                btn_a.grid(row = 2, column = 0)

                labelAnswerA = tk.Label(self, text = "is...") #input from labelA
                labelAnswerA.grid(row = 2, column = 2)

                labelB = tk.Label(self, text = "B: ") #text before box
                labelB.grid(row = 4, column = 1)

                btn_b = ttk.Button(self, text="B", command=action_wrong)
                btn_b.grid(row = 4, column = 0)

                labelAnswerB = tk.Label(self, text = "is...") #input from labelB
                labelAnswerB.grid(row = 4, column = 2)

                labelC = tk.Label(self, text = "C: ") #text before box
                labelC.grid(row = 6, column = 1)

                btn_c = ttk.Button(self, text="C", command=action_wrong)
                btn_c.grid(row = 6, column = 0)

                labelAnswerC = tk.Label(self, text = "is...") #input from labelC
                labelAnswerC.grid(row = 6, column = 2)

                labelD = tk.Label(self, text = "D: ") #text before box
                labelD.grid(row = 8, column = 1)

                btn_d = ttk.Button(self, text="D", command=action_wrong)
                btn_d.grid(row = 8, column = 0)

                labelAnswerD = tk.Label(self, text = "is...") #input from labelD
                labelAnswerD.grid(row = 8, column = 2)

                btn_GH = ttk.Button(self, text="Go Home",
                        command = lambda: controller.show_frame(HomePage))
                btn_GH.grid(row = 10, column = 3)


class MyQuizzes(tk.Frame):
        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text="My Quizzes... coming soon",font= LARGE_FONT)
                label.grid(pady=10,padx=10)
                self.controller=controller

                btn_GH = tk.Button(self, text="Go Home",
                        command = lambda: controller.show_frame(HomePage))
                btn_GH.grid()



class Login(tk.Frame):

    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login",font= LARGE_FONT)
        label.grid(row = 0, column = 3, pady=10,padx=10)
        self.controller=controller

        creds = 'ref_docs/User.txt'

        LabelName = Label(self, text='Username: ')
        LabelName.grid(row=1, column = 0)

        LabelPass = Label(self, text='Password: ')
        LabelPass.grid(row=2, column = 0)

        def defaults(event):
            if TxtBoxName != self.focus_get() and TxtBoxName.get() == '':
                TxtBoxName.insert(0, 'Enter UserName')
            elif TxtBoxPass != self.focus_get() and TxtBoxPass.get() == '':
                TxtBoxPass.insert(0, '      ')

        def clear(event):
            if TxtBoxName == self.focus_get() and TxtBoxName.get() == 'Enter UserName':
                TxtBoxName.delete(0, END)
            elif TxtBoxPass == TxtBoxPass.focus_get() and TxtBoxPass.get() == '      ':
                TxtBoxPass.delete(0, END)


        TxtBoxName = Entry(self)
        TxtBoxName.grid(row=1, column=1)
        TxtBoxName.insert(0, "Enter UserName")
        TxtBoxName.bind("<FocusIn>", clear)
        TxtBoxName.bind("<FocusOut>", defaults)

        TxtBoxPass = Entry(self, show='*')
        TxtBoxPass.grid(row=2, column=1)
        TxtBoxPass.insert(0, "      ")
        TxtBoxPass.bind("<FocusIn>", clear)
        TxtBoxPass.bind("<FocusOut>", defaults)

        def CheckLogin():
            with open(creds, "r") as f:
                data = f.readlines()
                count0=0
                count1=1
                while TxtBoxName.get() != (data[count0].rstrip()):
                        wrong_pass = Label(self, text='User Name Invalid',font="bold")
                        wrong_pass.grid(row=2, column = 3)
                        count0 = count0+2

                while TxtBoxPass.get() != (data[count1].rstrip()):
                        wrong_user = Label(self, text='Wrong Password',font="bold")
                        wrong_user.grid(row=2, column = 3)
                        count1 = count1+2
                x = count0
                y = count1

            with open(creds, "r") as f:
                data = f.readlines()
                uname = data[x].rstrip() #error shows up - problem?
                pword = data[y].rstrip()

            if TxtBoxName.get() == uname and TxtBoxPass.get() == pword:
                controller.show_frame(HomePage)

        loginB = ttk.Button(self, text='Login', command=CheckLogin)
        loginB.grid(columnspan=2, sticky=W)

        BtnName = ttk.Button(self, text='Create User', command=lambda: controller.show_frame(RegUser))
        BtnName.grid(columnspan=2, sticky=W)

        BtnName = ttk.Button(self, text='SKIP', command=lambda: controller.show_frame(HomePage))
        BtnName.grid(columnspan=2, sticky=W)



class RegUser(tk.Frame):

    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Create Account",font= LARGE_FONT)
        label.grid(row = 0, column = 3, pady=10,padx=10)
        self.controller=controller

        creds = 'ref_docs/User.txt'

        LabelName = Label(self, text='New Username: ')
        LabelName.grid(row=1, column=0, sticky=W)

        LabelPass = Label(self, text='New Password: ')
        LabelPass.grid(row=2, column=0, sticky=W)

        def defaults(event):
            if TxtBoxName != self.focus_get() and TxtBoxName.get() == '':
                TxtBoxName.insert(0, 'Enter UserName')
            elif TxtBoxPass != self.focus_get() and TxtBoxPass.get() == '':
                TxtBoxPass.insert(0, '      ')

        def clear(event):
            if TxtBoxName == self.focus_get() and TxtBoxName.get() == 'Enter UserName':
                TxtBoxName.delete(0, END)
            elif TxtBoxPass == TxtBoxPass.focus_get() and TxtBoxPass.get() == '      ':
                TxtBoxPass.delete(0, END)


        TxtBoxName = Entry(self)
        TxtBoxName.grid(row=1, column=1)
        TxtBoxName.insert(0, "Enter UserName")
        TxtBoxName.bind("<FocusIn>", clear)
        TxtBoxName.bind("<FocusOut>", defaults)

        TxtBoxPass = Entry(self, show='*')
        TxtBoxPass.grid(row=2, column=1)
        TxtBoxPass.insert(0, "      ")
        TxtBoxPass.bind("<FocusIn>", clear)
        TxtBoxPass.bind("<FocusOut>", defaults)

        def FSSignup():
            with open(creds, 'a') as f:
                f.write(TxtBoxName.get())
                f.write('\n')
                f.write(TxtBoxPass.get())
                f.write('\n')
                f.close()

            controller.show_frame(Login)

        signupButton = ttk.Button(self, text='Signup', command=FSSignup)
        signupButton.grid(columnspan=2, sticky=W)


class QuizCreator(tk.Tk):

        def __init__(self, *args,  **kwargs):

                tk.Tk.__init__(self, *args,  **kwargs)
                tk.Tk.iconbitmap(self, default="icons/Quizlogo.ico") 
                tk.Tk.wm_title(self,"Quiz Creator") #window title
                container = tk.Frame(self)

                container.pack (side="top", fill="both", expand = True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)
                # self.geometry("500x500")

                self.frames = {}
                
                # keep track of all window(class) names
                for F in (HomePage, Q1Page, Q2Page, A1Page, A2Page, MyQuizzes, Login, RegUser):
                        frame = F(container, self)
                        self.frames[F] = frame
                        frame.grid(row=0, column=0, sticky="nsew")

                #set the startup page
                self.show_frame(Login)

                menu_bar = Menu(self)

                # Create the submenu
                file_menu = Menu(menu_bar, tearoff=1)
                edit_menu = Menu(menu_bar, tearoff=1)

                # Add commands to submenu
                file_menu.add_command(label="Quit!", command=self.destroy)
                file_menu.add_command(label="Save", command=self.save_file)
                file_menu.add_command(label="Load", command=self.load_file)
                #file_menu.add_command(label="Log In", command=self.get_page[Login])


                # Add the "File" drop down sub-menu in the main menu bar
                menu_bar.add_cascade(label="File", menu=file_menu)
                menu_bar.add_cascade(label="Edit", menu=edit_menu)

                self.config(menu=menu_bar)
                self.mainloop()

        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()

        def get_page(self, page_class):
                return self.frames[page_class]

        def save_file(self):
                global save_name
                save = input("savename: ")
                save_name = save
                path = 'path_to_dir{0}.json'.format(save_name)
                data = {
                    'name': save_name
                }
                with open(path, 'w+') as f:
                    json.dump(data, f)

        def load_file(self):
                load_name = save_name  #save_name not recognized NEED to FIX THIS!!!!!
                path_two = 'path_to_dir{0}.json'.format(load_name)
                with open(path_two, 'r') as f:
                    j = json.load(f)
                    name = str(j['name'])


app = QuizCreator()
app.mainloop()



#TO DO
# display username on each page
#input string from Q1 to A1
#Save and Load Quizes
# add more submenu options
# use enter to login/create account
# creat msger between users
