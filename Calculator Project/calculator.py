import tkinter as tk
def press(key):
    if key == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == "C":
        display.delete(0, tk.END)
    elif key == "⌫":  # Backspace
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current[:-1])
    else:
        display.insert(tk.END, key)
root = tk.Tk()
root.title("Soft Grid Calculator")
root.geometry("360x450")
root.configure(bg="#f0f0f0")
display = tk.Entry(root, font=("Arial", 24), borderwidth=0, relief="ridge", justify="right",
                   bg="#ffffff", fg="#333333", insertbackground="#333333")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we", ipadx=5, ipady=15)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["C", "⌫", "=" , ""]
]
num_color = "#e0e0e0"       
op_color = "#ffd580"
special_color = "#ff9999"   
for r, row in enumerate(buttons, start=1):
    for c, btn in enumerate(row):
        if btn == "":
            continue  
        color = num_color if btn.isdigit() or btn == "." else op_color
        if btn == "C":
            color = special_color
        elif btn == "=":
            color = "#99ff99"  
        elif btn == "⌫":
            color = "#ffcc99" 
        b = tk.Button(root, text=btn, font=("Arial", 20), bg=color, fg="#333333",
                      command=lambda x=btn: press(x), borderwidth=1, relief="raised")
        b.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
root.mainloop()