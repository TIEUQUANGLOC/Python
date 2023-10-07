from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
      
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("INVENTORY")
        self.pack(fill=BOTH, expand=1)
  
        Style().configure("TFrame", background="#333")
  
        bard = Image.open("Z:/2111859_Lab4_LTPython/image/360fx360f.png")
        bard = bard.resize((100,100), Image.LANCZOS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
    
        rot = Image.open("Z:/2111859_Lab4_LTPython/image/360fx360f.png")
        rot = rot.resize((100,100), Image.LANCZOS)
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=20, y=160)
  
        minc = Image.open("Z:/2111859_Lab4_LTPython/image/360fx360f.png")
        minc = minc.resize((100,100), Image.LANCZOS)
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=150, y=20)

root = Tk()
root.geometry("450x350+650+300")
app = Example(root)
root.mainloop()
