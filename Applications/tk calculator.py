from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title('Calculator v.001')
root.resizable(0,0)

class Application(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.createWidgets()


    def appendDisplay(self,text):
        self.append = self.display.get()
        self.textLength = len(self.append)

        if self.append =='0':
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0,text)

    def clearText(self):
        self.replaceText('0')
        
        
    def calcExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace('%', '/100')
        try:
            self.result =eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo('Error', 'Invalid Input')






    

    def createWidgets(self):
        self.display = Entry(self, font=('Helvectica', 16), relief=RAISED, justify=RIGHT)
        self.display.insert(0,'0')
        self.display.grid(row=0, column=0, columnspan=5, sticky='NSEW')

        self.sevenButton= Button(self, font=('Helvetica', 11), text='7', command=lambda: self.appendDisplay('7'))
        self.sevenButton.grid(row=1, column=0, sticky='NSEW')

        self.eightButton =Button(self, font=('Helvetica', 11), text='8', command =lambda: self.appendDisplay('8'))
        self.eightButton.grid(row=1, column=1, sticky='NSEW')

        self.nineButton = Button(self, font=('Helvetica',11), text='9', command = lambda: self.appendDisplay('9'))
        self.nineButton.grid(row=1, column=2, sticky='NSEW')

        self.mulButton = Button(self, font=('Helvetica', 11),text='*', command = lambda: self.appendDisplay('*'))
        self.mulButton.grid(row=1, column=3,sticky='NSEW')

        self.clsButton = Button(self, font=('Helvetica',11),text='C', command = lambda: self.clearText())
        self.clsButton.grid(row=1,column=4, sticky='NSEW')

        self.fourButton = Button(self, font=('Helvetica',11), text='4', command = lambda: self.appendDisplay('4'))
        self.fourButton.grid(row=2, column=0, sticky='NSEW')

        self.fiveButton = Button(self, font=('Helvetica',11), text='5', command = lambda: self.appendDisplay('5'))
        self.fiveButton.grid(row=2, column=1, sticky='NSEW')

        self.sixButton = Button(self, font=('Helvetica',11), text='6', command = lambda: self.appendDisplay('6'))
        self.sixButton.grid(row=2, column=2, sticky='NSEW')

        self.divButton = Button(self, font=('Helvetica',11), text='/', command = lambda: self.appendDisplay('/'))
        self.divButton.grid(row=2, column=3, sticky='NSEW')

        self.oneButton = Button(self,font=('Helvetica',11), text='1', command = lambda: self.appendDisplay('1'))
        self.oneButton.grid(row=3, column=0, sticky='NSEW')

        self.twoButton = Button(self, font=('Helvetica', 11), text='2', command = lambda: self.appendDisplay('2'))
        self.twoButton.grid(row=3, column=1, sticky='NSEW')

        self.threeButton = Button(self, font=('Helvetica',11), text='3', command = lambda: self.appendDisplay('3'))
        self.threeButton.grid(row=3, column=2, sticky='NSEW')

        self.subButton = Button(self, font=('Helvetica',11), text='-', command = lambda: self.appendDisplay('-'))
        self.subButton.grid(row=3, column=3, sticky='NSEW')

        self.zeroButton = Button(self, font=('Helvetica',11), text='0', command = lambda: self.appendDisplay('0'))
        self.zeroButton.grid(row=4, column=0,columnspan=2, sticky='NSEW')

        self.deciButton = Button(self, font=('Helvetica', 11), text='.', command = lambda: self.appendDisplay('.'))
        self.deciButton.grid(row=4, column=2, sticky='NSEW')

        self.percButton = Button(self, font=('Helvetica',11),text='%', command = lambda: self.appendDisplay('%'))
        self.percButton.grid(row=4, column=3, sticky='NSEW')

        self.addButton = Button(self, font=('Helvetica',11), text='+', command = lambda: self.appendDisplay('+'))
        self.addButton.grid(row=2, column=4, sticky='NSEW')

        self.equalButton = Button(self, font=('Helvetica', 11), text='=', command = lambda: self.calcExpression())
        self.equalButton.grid(row=3, column=4, sticky='NSEW', rowspan=2)



        
app=Application(root).grid()


root.mainloop()
