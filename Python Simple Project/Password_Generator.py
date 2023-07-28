import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_show_password():
    try:
        password = int(length_entry.get())
        uppercase = uppercase_var.get()
        digits = digits_var.get()
        symbols = symbols_var.get()
        password = generate_password(password, uppercase, digits, symbols)
        password_display.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid password length.")
r= tk.Tk()
r.title("Password Generator")
length_label = tk.Label(r, text="Enter the Password Length:",bg="#ADD8E6",font=('Aerial',12,'bold'))
length_label.pack(pady=5)

length_entry = tk.Entry(r, width=30)
length_entry.pack(pady=10)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(r, text="Include Uppercase Letters", variable=uppercase_var,bg="#ADD8E6",font=('Aerial',12,'bold'))
uppercase_check.pack(padx=5)

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(r, text="Include Digits", variable=digits_var,bg="#ADD8E6",font=('Aerial',12,'bold'))
digits_check.pack(padx=25,pady=15)

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(r, text="Include Symbols", variable=symbols_var,bg="#ADD8E6",font=('Aerial',12,'bold'))
symbols_check.pack()

generate_button = tk.Button(r, text="Generate Password", command=generate_and_show_password,font=('Aerial',12,'bold'))
generate_button.pack(pady=10)

password_display = tk.Label(r, text="", font=("Arial", 14, "bold"),bg="#ADD8E6")
password_display.pack()
r.maxsize(300,300)
r.minsize(300, 300)
r['bg']="#ADD8E6"
r.mainloop()
