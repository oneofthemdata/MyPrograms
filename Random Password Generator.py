import random
from tkinter import *
import string
from tkinter.font import Font


def generate_password():
    password = []
    for i in range(2):
        alpha_upper = random.choice(string.ascii_uppercase)
        alpha_lower = random.choice(string.ascii_lowercase)
        numbers = random.choice(string.digits)
        password.append(alpha_upper)
        password.append(alpha_lower)
        password.append(numbers)
        if i == 1:
            symbol = random.choice(string.punctuation)
            password.append(symbol)
    y = "".join(str(x) for x in password)
    lbl.config(text=y)


root = Tk()
root.geometry("350x300")
btn = Button(root, text="Generate Password", command=generate_password, width=20, height=2)
btn.place(relx=0.5, rely=0.2, anchor=N)
myFont = Font(family="Consolas", size=18)
lbl = Label(root, font=myFont)
lbl.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()
