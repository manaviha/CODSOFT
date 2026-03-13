import tkinter as tk
import random
import string
def generate_password():
    length = int(length_entry.get())
    characters = ""
    if var_letters.get():
        characters += string.ascii_letters
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    check_strength(password)
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
def check_strength(password):
    strength = "Weak"
    if len(password) >= 8:
        strength = "Medium"
    if len(password) >= 12 and any(c in string.punctuation for c in password):
        strength = "Strong"
    strength_label.config(text="Strength: " + strength)
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
title = tk.Label(root, text="PASSWORD GENERATOR", font=("Arial",16,"bold"))
title.pack(pady=10)
tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()
var_letters = tk.IntVar(value=1)
var_numbers = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=1)
tk.Checkbutton(root, text="Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Symbols", variable=var_symbols).pack()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Button(root, text="Copy Password", command=copy_password).pack()
result_entry = tk.Entry(root, font=("Arial",12), justify="center")
result_entry.pack(pady=10)
strength_label = tk.Label(root, text="Strength: ")
strength_label.pack()
root.mainloop()