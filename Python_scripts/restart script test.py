import sys
import os
import tkinter as tk
self = tk.Tk()

class repeat():

   def myexcept(t, v, tb):
      import traceback
      ## edit to change max times to restart
      max_times = 5
      ## grabs the exception details
      tbtext = ''.join(traceback.format_exception(t, v, tb))
      print (" ERROR:")
      ## prints exception details
      print (tbtext)
      restarted = int(restarted)+1
      if restarted > max_times:
           ## stops script if restarted more than max_times
           print (" STOPPED!!!")
           exit(0)
      else:
           print (" RESTARTED "+str(restarted)+" times...")
           ## sets new argument list updating last argv
           a = ['python']+sys.argv[:-1]+[str(restarted)]
           ## restarts the script
           os.execv( sys.executable, a)
    
   ## set myexcept as global script exception method
   sys.excepthook = myexcept
    
   ## grabs times the scripts has been restarted (last argument)
   restarted = sys.argv[-1]
   print (" RESTARTED "+restarted+" times :-)" )

   def mycommand():
      os.execv( sys.executable, ['python']+sys.argv[:-1]+[str(restarted)])

   btn = tk.Button(self, text = "Submit", command = mycommand)
   btn.grid(row = 0, column = 0)
