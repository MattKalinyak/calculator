from tkinter import *
import parser
from math import factorial

#VARIABLES
textLocation = 0
buttonHeight = 3
buttonWidth = 6
displayHeight = 15
fontSize = '19'
windowSize = '382x402'
title = 'Calculator'

root = Tk() #New window
root.option_add('*Font', fontSize) #text Size
root.title(title) #Window Title
root.geometry(windowSize)

display = Entry(root)
display.grid(row = 1, columnspan = 6, sticky = N+S+E+W, ipady = displayHeight)

#FUNCTIONS
#Displays the selected variable in the text box
def get_variables(num):
    global textLocation
    display.insert(textLocation, num)
    textLocation += 1

#Clears the text box
def clear_all():
    display.delete(0, END)

#removes the most recent entry
def backspace():
    str = display.get()
    if len(str):
        newStr = str[:-1]
        clear_all()
        display.insert(0, newStr)
    else:
        clear_all
        display.insert(0, "ERROR")

#runs the formula that is being displayed
def calculate():
    str = display.get()
    try:
        equation = parser.expr(str).compile()
        result = eval(equation)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all
        display.insert(0, "ERROR")

#Factorial button
def factorialFunction():
    str = display.get()
    try:
        value = factorial(int(str))
        clear_all()
        display.insert(0, value)
    except Exception:
        clear_all()
        display.insert(0, "ERROR")

#Displays the operator that was selected
def get_operation(operator):
    global textLocation
    length = len(operator)
    display.insert(textLocation, operator)
    textLocation += length

#BUTTONS
#Number buttons
Button(root, text = "1", command = lambda :get_variables(1), width = buttonWidth, height = buttonHeight).grid(row=2, column=0, sticky=N+S+E+W)
Button(root, text = "2", command = lambda :get_variables(2), width = buttonWidth, height = buttonHeight).grid(row=2, column=1, sticky=N+S+E+W)
Button(root, text = "3", command = lambda :get_variables(3), width = buttonWidth, height = buttonHeight).grid(row=2, column=2, sticky=N+S+E+W)
Button(root, text = "4", command = lambda :get_variables(4), width = buttonWidth, height = buttonHeight).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text = "5", command = lambda :get_variables(5), width = buttonWidth, height = buttonHeight).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text = "6", command = lambda :get_variables(6), width = buttonWidth, height = buttonHeight).grid(row=3, column=2, sticky=N+S+E+W)
Button(root, text = "7", command = lambda :get_variables(7), width = buttonWidth, height = buttonHeight).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text = "8", command = lambda :get_variables(8), width = buttonWidth, height = buttonHeight).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text = "9", command = lambda :get_variables(9), width = buttonWidth, height = buttonHeight).grid(row=4, column=2, sticky=N+S+E+W)
Button(root, text = "0", command = lambda :get_variables(0), width = buttonWidth, height = buttonHeight).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text = ".", command = lambda :get_variables("."), width = buttonWidth, height = buttonHeight).grid(row=5, column=2, sticky=N+S+E+W)

#Operators
Button(root, text = "+", command = lambda :get_operation("+"), width = buttonWidth, height = buttonHeight).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text = "-", command = lambda :get_operation("-"), width = buttonWidth, height = buttonHeight).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text = "*", command = lambda :get_operation("*"), width = buttonWidth, height = buttonHeight).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text = "/", command = lambda :get_operation("/"), width = buttonWidth, height = buttonHeight).grid(row=5, column=3, sticky=N+S+E+W)
Button(root, text = "%", command = lambda :get_operation("%"), width = buttonWidth, height = buttonHeight).grid(row=3, column=4, sticky=N+S+E+W)
Button(root, text = "(", command= lambda :get_operation("("), width = buttonWidth, height = buttonHeight).grid(row=4, column=4, sticky=N+S+E+W)
Button(root, text = "exp", command= lambda :get_operation("**"), width = buttonWidth, height = buttonHeight).grid(row=5, column=4, sticky=N+S+E+W)
Button(root, text = ")", command= lambda :get_operation(")"), width = buttonWidth, height = buttonHeight).grid(row=4, column=5, sticky=N+S+E+W)
Button(root, text = "^2", command= lambda :get_operation("**2"), width = buttonWidth, height = buttonHeight).grid(row=5, column=5, sticky=N+S+E+W)
Button(root, text = "^2", command= lambda :get_operation("**2"), width = buttonWidth, height = buttonHeight).grid(row=5, column=5, sticky=N+S+E+W)
Button(root, text = "pi", command= lambda :get_operation("*3.14"), width = buttonWidth, height = buttonHeight).grid(row=2, column=4, sticky=N+S+E+W)

# Different Operations
Button(root, text = "=", command= lambda :calculate(), height = buttonHeight).grid(columnspan=6, sticky=N+S+E+W)
Button(root, text = "<", command= lambda :backspace(), width = buttonWidth, height = buttonHeight).grid(row=2, column=5, sticky=N+S+E+W)
Button(root, text = "AC", command = lambda :clear_all(), width = buttonWidth, height = buttonHeight).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text = "x!", command= lambda: factorialFunction(), width = buttonWidth, height = buttonHeight).grid(row=3, column=5, sticky=N+S+E+W)

root.mainloop()


