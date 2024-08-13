from tkinter import*
import math 

import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.resizable(width=False, height=False)
root.geometry("400x492+460+40")

MainFrame = Frame(root, pady=2, relief=RIDGE)
MainFrame.grid()
calcFrame = Frame(MainFrame, bd=20 , pady=2, relief=RIDGE)
calcFrame.grid()

##############################################################################################
class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def EnterNumber(self, num):
        self.result = False
        firstnum = txtResult.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.validFunction()
        else:
            self.total = float(txtResult.get())

    def display(self, value):
        txtResult.delete(0, END)
        txtResult.insert(0, value)

    def validFunction(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mult":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.validFunction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtResult.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtResult.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtResult.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtResult.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtResult.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtResult.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtResult.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtResult.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtResult.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtResult.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtResult.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtResult.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtResult.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtResult.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtResult.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtResult.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtResult.get()))
        self.display(self.current)

    def backspace(self):
        numLen = len(txtResult.get())
        txtResult.delete(numLen - 1, 'end')
        if numLen == 1:
            txtResult.insert(0, "0")

##############################################################################################

added_value = Calc()

txtResult = Entry(calcFrame, font=('arial', 16, 'bold'), bg="cadetblue", bd=30, width=26, justify=RIGHT)
txtResult.grid(row=0, column=0, columnspan=4, pady=1)
txtResult.insert(0, "0")

##############################################################################################
numericButton = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for q in range(3):
        btn.append(Button(calcFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=numericButton[i],
                          command=lambda x=numericButton[i]: added_value.EnterNumber(x)))
        btn[i].grid(row=j, column=q, pady=1)
        i += 1
##############################################################################################

btn0 = Button(calcFrame, text="0", width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
              command=lambda: added_value.EnterNumber(0)).grid(row=5, column=0, pady=1)

btnDiv = Button(calcFrame, text=chr(247), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                command=lambda: added_value.operation("divide")).grid(row=5, column=3, pady=1)

btnMult = Button(calcFrame, text=chr(42), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                 command=lambda: added_value.operation("mult")).grid(row=4, column=3, pady=1)

btnSub = Button(calcFrame, text=chr(45), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                command=lambda: added_value.operation("sub")).grid(row=3, column=3, pady=1)

btnDot = Button(calcFrame, text=chr(183), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                command=lambda: added_value.EnterNumber(".")).grid(row=5, column=1, pady=1)

btnAdd = Button(calcFrame, text=chr(43), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                command=lambda: added_value.operation("add")).grid(row=2, column=3, pady=1)

btnPM = Button(calcFrame, text=chr(177), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
               command=added_value.mathsPM).grid(row=1, column=3, pady=1)

btnBackspace = Button(calcFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="⌫", bg="cadetblue",
                      command=added_value.backspace).grid(row=1, column=0, pady=1)

btnClearEntry = Button(calcFrame, text=chr(67) + chr(69), width=6, height=2, font=('arial', 16, 'bold'), bd=4,
                       bg="cadetblue", command=added_value.Clear_Entry).grid(row=1, column=1, pady=1)

btnClear = Button(calcFrame, text=chr(67), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                  command=added_value.all_Clear_Entry).grid(row=1, column=2, pady=1)

btnequals = Button(calcFrame, text=chr(61), width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg="cadetblue",
                   command=added_value.sum_of_total).grid(row=5, column=2, pady=1)


##############################################################################################

btnsin= Button(calcFrame, text= "sin", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.sin).grid(row=1,column=4,padx=5,pady=1)

btntan= Button(calcFrame, text= "tan", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.tan).grid(row=1,column=5,pady=1)

btncos= Button(calcFrame, text= "cos", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.cos).grid(row=1,column=6,pady=1)

btnPi= Button(calcFrame, text= "π", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.pi).grid(row=1,column=7,pady=1)

##############################################################################################

btnsinh= Button(calcFrame, text= "sinh", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.sinh).grid(row=2,column=4,padx=5,pady=1)

btntanh= Button(calcFrame, text= "tanh", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.tanh).grid(row=2,column=5,pady=1)

btncosh= Button(calcFrame, text= "cosh", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.cosh).grid(row=2,column=6,pady=1)

btn2Pi= Button(calcFrame, text= "2π", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.tau).grid(row=2,column=7,pady=1)

##############################################################################################

btnE= Button(calcFrame, text= "e", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.e).grid(row=3,column=4,padx=5,pady=1)

btnMod= Button(calcFrame, text= "mod", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= lambda: added_value.operation("mod")).grid(row=3,column=5,pady=1)

btnExp= Button(calcFrame, text= "exp", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.exp).grid(row=3,column=6,pady=1)

btnlog= Button(calcFrame, text= "log", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.log).grid(row=3,column=7,pady=1)

##############################################################################################

btnasinh= Button(calcFrame, text= "asinh", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.asinh).grid(row=4,column=4,padx=5,pady=1)

btnacosh= Button(calcFrame, text= "acosh", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.acosh).grid(row=4,column=5,pady=1)

btndeg= Button(calcFrame, text= "deg", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.degrees).grid(row=4,column=6,pady=1)

btnlog2= Button(calcFrame, text= "log2", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.log2).grid(row=4,column=7,pady=1)

##############################################################################################

btnlgamma= Button(calcFrame, text= "lgamma", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.lgamma).grid(row=5,column=4,padx=5,pady=1)

btnexpm1= Button(calcFrame, text= "expm1", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.expm1).grid(row=5,column=5,pady=1)

btnlog1p= Button(calcFrame, text= "log1p", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, command= added_value.log1p).grid(row=5,column=6,pady=1)

btnlog10= Button(calcFrame, text= "log10", width=6, height=2 , font=('arial',16,'bold')
                  , bd=4, bg="cadetblue", command= added_value.log10).grid(row=5,column=7,pady=1)

##############################################################################################
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
    
def scientific():
    root.geometry("796x492+260+40")
    root.resizable(width=False, height=False)
    txtResult.delete(0, END)
    txtResult.delete(0, "0")
    lblDisplay = Label(calcFrame, text="Dynamic Hunter", font=('c39hrp24dhtt', 60),padx= 9,fg= 'cadetblue', justify = CENTER)
    lblDisplay.grid(row=0, column=4, columnspan=4)


def standard():
    root.geometry("400x492+460+40")
    root.resizable(width=False, height=False)
    txtResult.delete(0, END)
    txtResult.delete(0, "0")


menubar = Menu(calcFrame)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=standard)
filemenu.add_command(label="Scientific", command=scientific )
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

root.config(menu= menubar)

root.mainloop()