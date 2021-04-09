from tkinter import Button, mainloop, Tk, Pack, Label, Entry, Grid, Button, END

root = Tk()
root.title("Calculator")

input_text = Entry(root, width = 35, borderwidth = 5)
input_text.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):

    current = input_text.get()
    input_text.delete(0, END)
    input_text.insert(0, str(current) + str(number))

def button_add():

    global first_number, math
    math = "addition"
    first_number = int(input_text.get())
    input_text.delete(0,END)

def button_subtract():

    global first_number, math
    math = "subtraction"
    first_number = int(input_text.get())
    input_text.delete(0,END)

def button_divide():

    global first_number, math
    math = "divide"
    first_number = int(input_text.get())
    input_text.delete(0,END)

def button_multiply():

    global first_number, math
    math = "multiplication"
    first_number = int(input_text.get())
    input_text.delete(0,END)

def button_modulus():

    global first_number, math
    math = "modulus"
    first_number = int(input_text.get())
    input_text.delete(0,END)

def button_x():

    global first_number
    first_number = int(input_text.get())
    input_text.delete(0,END)
    input_text.insert(0, 1 / first_number)

def button_square():

    global first_number
    first_number = int(input_text.get())
    input_text.delete(0,END)
    input_text.insert(0, first_number * first_number)

def button_equal():

    global second_number
    second_number = int(input_text.get())
    input_text.delete(0,END)

    if math == "addition":
        input_text.insert(0, first_number + second_number)

    elif math == "subtraction":
        input_text.insert(0, first_number - second_number)

    elif math == "multiplication":
        input_text.insert(0, first_number * second_number)
    
    elif math == "modulus":
        input_text.insert(0, first_number % second_number)

    else:
        input_text.insert(0, first_number / second_number)

def button_clear():

    input_text.delete(0,END)



#Define buttons

button_0 = Button(root, text = "0", padx = 40, pady = 10, command = lambda: button_click(0))
button_1 = Button(root, text = "1", padx = 40, pady = 10, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 10, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 10, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 10, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 10, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 10, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 10, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 10, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 10, command = lambda: button_click(9))
button_add = Button(root, text = "+", padx = 40, pady = 10, command = button_add)
button_x = Button(root, text= "1/x", padx = 40, pady = 10 , command = button_x)
button_square = Button(root, text= "x²", padx = 40, pady = 10 , command = button_square)
button_subtract = Button(root, text="-", padx= 40, pady = 10, command = button_subtract)
button_multiply = Button(root, text="*", padx= 40, pady = 10, command = button_multiply)
button_divide = Button(root, text="/", padx= 40, pady = 10, command = button_divide)
button_modulus = Button(root, text="%", padx= 40, pady = 10, command = button_modulus)
button_equal = Button(root, text = "=", padx = 40, pady = 10, command = button_equal)                  
button_clear = Button(root, text = "Clear", padx = 40, pady = 10, command = button_clear)

# Put buttons on screen

button_multiply.grid(row = 5, column = 0)
button_divide.grid(row = 5, column = 1)
button_subtract.grid(row = 5, column = 2)


button_0.grid(row = 4, column = 0)
button_add.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_x.grid(row = 6, column = 1)
button_square.grid(row = 6, column = 0)
button_modulus.grid(row = 6, column = 2)


button_clear.grid(row = 5, column = 1)

root.mainloop()