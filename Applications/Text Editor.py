from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
    global filename
    filename = "untitled"
    text.delete(0, END)

def saveFile():
    global filename
    t = text.get(0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0,END)
    try:
        f.write(trstrip())
    except:
        showerror(title="Error", message="File was unable to be saved")

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0,END)
    text.insert(0,t)

root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' %(w,h))


text = Text(root, width=w, height= h)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()



 
 
