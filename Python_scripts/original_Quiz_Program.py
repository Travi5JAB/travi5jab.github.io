import tkinter #new window
import tkinter as tk
window = tk.Tk()
window.title("User Input")
window.geometry("750x750") #window size

global userName_q
global userName_a
global userName_b
global userName_c
global userName_d

labelQ = tk.Label(window, text = "enter Question") #text before box
labelQ.grid(row = 0, column = 0)

labelPrompt = tk.Label(window, text = "Question...") #input from labelQ
labelPrompt.grid(row=1, column=1)

labelA = tk.Label(window, text = "enter Option A") #text before box
labelA.grid(row = 2, column = 0)

labelPromptA = tk.Label(window, text = "A is...") #input from labelA
labelPromptA.grid(row=3, column=1)

labelB = tk.Label(window, text = "enter Option B") #text before box
labelB.grid(row = 4, column = 0)

labelPromptB = tk.Label(window, text = "B is...") #input from labelB
labelPromptB.grid(row=5, column=1)

labelC = tk.Label(window, text = "enter Option C") #text before box
labelC.grid(row = 6, column = 0)

labelPromptC = tk.Label(window, text = "C is...") #input from labelC
labelPromptC.grid(row=7, column=1)

labelD = tk.Label(window, text = "enter Option D") #text before box
labelD.grid(row = 8, column = 0)

labelPromptD = tk.Label(window, text = "D is...") #input from labelD
labelPromptD.grid(row=9, column=1)

userName_q = tk.StringVar()
userName_a = tk.StringVar()
userName_b = tk.StringVar()
userName_c = tk.StringVar()
userName_d = tk.StringVar()

#user entry
userEntry = tk.Entry(window, width = 26, textvariable = userName_q)
userEntry.grid(row = 0, column = 1) #textbox

userEntryA = tk.Entry(window, width = 26, textvariable = userName_a)
userEntryA.grid(row = 2, column = 1) #textbox

userEntry = tk.Entry(window, width = 26, textvariable = userName_b)
userEntry.grid(row = 4, column = 1) #textbox

userEntry = tk.Entry(window, width = 26, textvariable = userName_c)
userEntry.grid(row = 6, column = 1) #textbox

userEntry = tk.Entry(window, width = 26, textvariable = userName_d)
userEntry.grid(row = 8, column = 1) #textbox

def action_all():
    labelPrompt.configure(text = userName_q.get())
    labelPromptA.configure(text = userName_a.get())
    labelPromptB.configure(text = userName_b.get())
    labelPromptC.configure(text = userName_c.get())
    labelPromptD.configure(text = userName_d.get())
    print (userName_q.get())
    print (userName_a.get())
    print (userName_b.get())
    print (userName_c.get())
    print (userName_d.get())
def action_q():
    labelPrompt.configure(text = userName_q.get())
    print (userName_q.get())
def action_a():
    labelPromptA.configure(text = userName_a.get())
    print (userName_a.get())
def action_b():
    labelPromptB.configure(text = userName_b.get())
    print (userName_b.get())
def action_c():
    labelPromptC.configure(text = userName_c.get())
    print (userName_c.get())
def action_d():
    labelPromptD.configure(text = userName_d.get())
    print (userName_d.get())
    
    
btn = tk.Button(window, text = "Submit", command = action_all)
btn.grid(row = 10, column = 2) #submit user entry info

window.mainloop()
# end window

#new window
import tkinter
import tkinter as tk
window = tk.Tk()
window.title("Test 1")
window.geometry("600x600") #window size

labelQ = tk.Label(window, text = "Question: ") #text before box
labelQ.grid(row = 0, column = 1)

labelPrompt = tk.Label(window, text = userName_q.get()) #input from labelQ
labelPrompt.grid(row=0, column=2)

labelA = tk.Label(window, text = "A: ") #text before box
labelA.grid(row = 2, column = 1)

labelPromptA = tk.Label(window, text = userName_a.get()) #input from labelA
labelPromptA.grid(row=2, column=2)

labelB = tk.Label(window, text = "B: ") #text before box
labelB.grid(row = 6, column = 1)

labelPromptB = tk.Label(window, text = userName_b.get()) #input from labelB
labelPromptB.grid(row=6, column=2)

labelC = tk.Label(window, text = "C: ") #text before box
labelC.grid(row = 8, column = 1)

labelPromptC = tk.Label(window, text = userName_c.get()) #input from labelC
labelPromptC.grid(row=8, column=2)

labelD = tk.Label(window, text = "D: ") #text before box
labelD.grid(row = 10, column = 1)

labelPromptD = tk.Label(window, text = userName_d.get()) #input from labelD
labelPromptD.grid(row=10, column=2)

def action_wrong(): #wrong answer	
	print("Incorrect")
def action_correct():	#right answer
	print("Correct")
	
btn_A = tk.Button(window, text="A", command=action_correct)
btn_A.grid(row = 2, column = 0, ipadx=20, ipady=20)

btn = tk.Button(window, text="B", command=action_wrong)
btn.grid(row = 6, column = 0, ipadx=20, ipady=20)

btn = tk.Button(window, text="C", command=action_wrong)
btn.grid(row = 8, column = 0, ipadx=20, ipady=20)

btn = tk.Button(window, text="D", command=action_wrong)
btn.grid(row = 10, column = 0, ipadx=20, ipady=20)

window.mainloop()
#end loop

question = input ("Question")
print (question)
root.mainloop()
