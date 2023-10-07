from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
      
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("Quit button")
        self.style = Style()
        self.style.theme_use("default")
  
        self.pack(fill=BOTH, expand=1)
  
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=150, y=100)


root = Tk()
root.geometry("350x250+650+300")
app = Example(root)
root.mainloop()
