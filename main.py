# import the packages 
import math
from tkinter import *


root = Tk()     #begin the instance for tkinter
root.title("Calculator")  #add the title to the UI

e = Entry(root, width=50, borderwidth=5)  #define a text display area called e
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)   # position the text area at 1st row and a first column, spanning 5 columns


# function to pass the number clicked by the representing button 
def button_click(number):
    #e.delete(0, "END")
    current = e.get()
    e.delete(0, "END")
    e.insert(0, str(current) + str(number))

def button_clear():           #function to clear the text area
    e.delete(0, "END")

def button_addition():          #this is to differentiate between float and int
    first_num = e.get()
    global maths
    maths = "addition"
    global f_num
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    # if first_num.count(".") == 1 in first_num:
    #     f_num = float(first_num)
    # elif first_num.count(".") == 0 in first_num:
    #     f_num = int(first_num)
    # else:
    #     e.insert(tk.INSERT, "SYNTAX ERROR")
    e.delete(0, "END")


def button_divison():       #function to divide first number with the second number 
    first_num = e.get()
    global maths
    maths = "divison"
    global f_num
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0, "END")

def button_squrt():       # to calculate square root of a number 
    #first_num = e.get()
    global maths
    maths = "squrt"
    #global f_num
    #if "." in first_num:
    #    f_num = float(first_num)
    #else:
     #   f_num = int(first_num)
    e.delete(0, "END")

def button_multiply():    # function to multiply 
    first_num = e.get()
    global maths
    maths = "multiply"
    global f_num
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0, "END")


def button_square():          #to calculate square 
    first_num = e.get()
    global maths
    maths = "square"
    global f_num
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0, "END")

def button_subtract():      #substractions function 
    first_num = e.get()
    global maths
    maths = "subtract"
    global f_num
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0, "END")


def button_equal():           #activated when pressed equal to button 
    second_num = e.get()
    global s_num
    if "." in second_num:
        s_num = float(second_num)
    else:
        s_num = int(second_num)
    e.delete(0, "END")
    if maths == "addition":
        e.insert(0, f_num + s_num)
    if maths == "divison":
        e.insert(0, f_num / s_num)
    if maths == "squrt":
        e.insert(0, math.sqrt(s_num))
    if maths == "multiply":
        e.insert(0, f_num * s_num)
    if maths == "square":
        e.insert(0, f_num * f_num)
    if maths == "subtract":
        e.insert(0, f_num - s_num)


# buttons for the calculator
button_1 = Button(root, text="1", padx=35, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=35, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=35, pady=20, command=lambda: button_click(3))
button_divison = Button(root, text="/", padx=35, pady=20, command=button_divison)
button_root = Button(root, text="√", padx=33, pady=20, command=button_squrt)

button_4 = Button(root, text="4", padx=35, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=35, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=35, pady=20, command=lambda: button_click(6))
button_multiply = Button(root, text="*", padx=35, pady=20, command=button_multiply)
button_square = Button(root, text="^2", padx=30, pady=20, command=button_square)

button_7 = Button(root, text="7", padx=35, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=35, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=35, pady=20, command=lambda: button_click(9))
button_subtract = Button(root, text="-", padx=35, pady=20, command=button_subtract)
button_equal = Button(root, text="=", padx=33, pady=50, command=button_equal)

button_0 = Button(root, text="0", padx=35, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text="C", padx=35, pady=20, command=button_clear)
button_decimal = Button(root, text=".", padx=36, pady=20, command=lambda: button_click("."))
button_addition = Button(root, text="+", padx=33, pady=20, command=button_addition)





# display buttons on the screen according  to position defined 

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_divison.grid(row=3, column=3)
button_root.grid(row=1, column=4)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)
button_square.grid(row=2, column=4)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_subtract.grid(row=1, column=3)
button_equal.grid(row=3, column=4, rowspan=2)


button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_decimal.grid(row=4, column=2)
button_addition.grid(row=4, column=3)





root.mainloop()       #to keep the UI visible in the screen 
