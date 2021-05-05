from tkinter import Tk, Text, TOP,RIGHT, BOTH, X,Y, N, LEFT
from tkinter.ttk import Frame, Label, Entry
 
class Example(Frame):
   def __init__(self, parent):
     Frame.__init__(self, parent)
  
     self.parent = parent
     self.initUI()
  
   def initUI(self):
     self.parent.title("Review")
     self.pack(fill=BOTH, expand=True)
  
     frame1 = Frame(self)
     frame1.pack(side=LEFT )
  
     lbl1 = Label(frame1, text="Title", width=6)
     lbl1.pack(side=TOP, padx=5, pady=5)
  
     entry1 = Entry(frame1)
     entry1.pack(fill=Y, padx=5, expand=True)
    
     frame2 = Frame(self)
     frame2.pack(side=RIGHT)
  
     lbl2 = Label(frame2, text="Author", width=6)
     lbl2.pack(side=TOP, padx=5, pady=5)     

     entry2 = Entry(frame2)
     entry2.pack(fill=Y, padx=5, expand=True)  
  
root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop() 