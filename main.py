from tkinter import*
expression = ""

root = Tk()
root.configure(background= "AntiqueWhite3")
root.title("simple calculator")
root.geometry("400x200")
mymath = StringVar()
mathbox = Entry(root,textvariable=mymath)
mathbox.grid(columnspan =5, ipadx=70)


def keypress(number):
    global expression
    expression = expression + str(number)
    print(expression)
    mymath.set(expression)


def total():
    global expression
    total2 = str(eval(expression))
    mymath.set(total2)
    expression=""
def clear():
    global expression
    expression = ""
    mymath.set("")
button_1 = Button(root, text = "1", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(1), height = 1, width = 5)
button_1.grid(row = 3, column = 1)
button_2 = Button(root, text = "2", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(2), height = 1, width = 5)
button_2.grid(row = 3, column = 2)
button_3 = Button(root, text = "3", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(3), height = 1, width = 5)
button_3.grid(row = 3, column = 3)
button_4 = Button(root, text = "4", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(4), height = 1, width = 5)
button_4.grid(row = 2, column = 1)
button_5 = Button(root, text = "5", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(5), height = 1, width = 5)
button_5.grid(row = 2, column = 2)
button_6 = Button(root, text = "6", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(6), height = 1, width = 5)
button_6.grid(row = 2, column = 3)
button_7 = Button(root, text = "7", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(7), height = 1, width = 5)
button_7.grid(row = 1, column = 1)
button_8 = Button(root, text = "8", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(8), height = 1, width = 5)
button_8.grid(row = 1, column = 2)
button_9 = Button(root, text = "9", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(9), height = 1, width = 5)
button_9.grid(row = 1, column = 3)
button_0 = Button(root, text = "0", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress(0), height = 1, width = 5)
button_0.grid(row = 4, column = 2)
button_equals = Button(root, text = "=", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: total(), height = 1, width = 5)
button_equals.grid(row = 4, column = 3)
button_plus = Button(root, text = "+", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress("+"), height = 1, width = 5)
button_plus.grid(row = 1, column = 5)
button_minus = Button(root, text = "-", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress("-"), height = 1, width = 5)
button_minus.grid(row = 2, column = 5)
button_multiply = Button(root, text = "*", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress("*"), height = 1, width = 5)
button_multiply.grid(row = 3, column = 5)
button_divide = Button(root, text = "/", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress("/"), height = 1, width = 5)
button_divide.grid(row = 4, column = 5)
button_dot = Button(root, text = ".", fg = "Grey18", bg = "AntiqueWhite3", command= lambda: keypress("."), height = 1, width = 5)
button_dot.grid(row = 4, column = 1)
buttonclear = Button(root, text="C", fg="black", bg="ivory4", command = clear, height=1, width=5)
buttonclear.grid(row=5, column=3)




root.mainloop()
