from tkinter import Button, mainloop, Tk, Pack, Label, Entry, Grid, Button, PhotoImage, END
from math import sqrt

root = Tk()
root.title("Calculator")
root.configure(background='#282828')
p1 = PhotoImage(file = 'icon.png')
root.iconphoto(True, p1)

input_text = Entry(root, width = 45, borderwidth = 5)
input_text.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def button_click(number):

    current = input_text.get()
    input_text.delete(0, END)
    input_text.insert(0, str(current) + str(number))

def button_add():

    global first_number, math
    math = "addition"
    first_number = float(input_text.get())
    input_text.delete(0,END)

def button_subtract():

    global first_number, math
    math = "subtraction"
    first_number = float(input_text.get())
    input_text.delete(0,END)

def button_divide():

    global first_number, math
    math = "divide"
    first_number = float(input_text.get())
    input_text.delete(0,END)

def button_multiply():

    global first_number, math
    math = "multiplication"
    first_number = float(input_text.get())
    input_text.delete(0,END)

def button_modulus():

    global first_number, math
    math = "modulus"
    first_number = float(input_text.get())
    input_text.delete(0,END)

def button_x():

    global first_number
    first_number = float(input_text.get())
    input_text.delete(0,END)
    input_text.insert(0, 1 / first_number)

def button_square():

    global first_number
    first_number = float(input_text.get())
    input_text.delete(0,END)
    input_text.insert(0, first_number * first_number)

def button_square_root():
    global first_number
    first_number = float(input_text.get())
    input_text.delete(0,END)
    input_text.insert(0, sqrt(first_number))

def button_equal():

    global second_number
    second_number = float(input_text.get())
    input_text.delete(0,END)

    if math == "addition":
        input_text.insert(0, first_number + second_number)

    if math == "subtraction":
        input_text.insert(0, first_number - second_number)

    if math == "multiplication":
        input_text.insert(0, first_number * second_number)
    
    if math == "modulus":
        input_text.insert(0, first_number % second_number)

    if math == "divide":
        input_text.insert(0, first_number / second_number)

def button_add_sub():

    input_text.insert(0,"-")

def button_dot():

    input_text.insert(END,".")

def button_clear_backspace():

    number = input_text.get()[:-1]
    input_text.delete(0, END)
    input_text.insert(0, number)
    # input_text.insert(input_text)

def button_clear_ce():

    input_text.delete(0, END)

def button_clear_c():

    input_text.delete(0, END)



#Define buttons

button_0 = Button(root, text = "0", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(0))
button_1 = Button(root, text = "1", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 32, pady = 10, fg = "white", bg="black", command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 32, pady = 10, fg = "white", bg="black", command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 30, pady = 10, fg = "white", bg="black", command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 32, pady = 10, fg = "white", bg="black", command = lambda: button_click(9))
button_add = Button(root, text = "+", padx = 30, pady = 10, fg = "white", bg = "#282828",  command = button_add)
button_x = Button(root, text= "1/x", padx = 24, pady = 10 , fg = "white", bg = "#282828", command = button_x)
button_square = Button(root, text= "x²", padx = 28, pady = 10 , fg = "white", bg = "#282828", command = button_square)
button_square_root = Button(root, text= "√x", padx = 28, pady = 10 , fg = "white", bg = "#282828", command = button_square_root)
button_subtract = Button(root, text="-", padx= 31.45, pady = 10, fg = "white", bg = "#282828", command = button_subtract)
button_multiply = Button(root, text="*", padx= 31.45, pady = 10, fg = "white", bg = "#282828", command = button_multiply)
button_divide = Button(root, text="/", padx= 30, pady = 10, fg = "white", bg = "#282828", command = button_divide)
button_modulus = Button(root, text="%", padx = 27, pady = 10, fg = "white", bg = "#282828", command = button_modulus)
button_equal = Button(root, text = "=", padx = 30, pady = 10, fg = "white", bg = "blue", command = button_equal)                  
button_add_sub = Button(root, text = "+/-", padx = 24, pady = 10, fg = "white", bg="black",  command = button_add_sub)
button_dot = Button(root, text = ".", padx = 33, pady = 10, fg = "white", bg="black", command = button_dot)
button_clear_backspace = Button(root, text = "←", padx = 28, pady = 10, fg = "white", bg = "#282828", command = button_clear_backspace)
button_clear_c = Button(root, text = "C", padx = 31, pady = 10, fg = "white", bg = "#282828", command = button_clear_c)
button_clear_ce = Button(root, text = "CE", padx = 26, pady = 10, fg = "white", bg = "#282828", command = button_clear_ce)

# Put buttons on screen

button_add_sub.grid(row = 6, column = 0)
button_0.grid(row = 6, column = 1)
button_dot.grid(row = 6, column = 2)
button_equal.grid(row = 6, column = 3)

button_1.grid(row = 5, column = 0)
button_2.grid(row = 5, column = 1)
button_3.grid(row = 5, column = 2)
button_add.grid(row = 5, column = 3)

button_4.grid(row = 4, column = 0)
button_5.grid(row = 4, column = 1)
button_6.grid(row = 4, column = 2)
button_subtract.grid(row = 4, column = 3)

button_7.grid(row = 3, column = 0)
button_8.grid(row = 3, column = 1)
button_9.grid(row = 3, column = 2)
button_multiply.grid(row = 3, column = 3)

button_x.grid(row = 2, column = 0)
button_square.grid(row = 2, column = 1)
button_square_root.grid(row = 2, column = 2)
button_divide.grid(row = 2, column = 3)

button_modulus.grid(row = 1, column = 0)
button_clear_ce.grid(row = 1, column = 1)
button_clear_c.grid(row = 1, column = 2)
button_clear_backspace.grid(row = 1, column = 3)

root.mainloop()