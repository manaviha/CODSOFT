from tkinter import *
from tkinter import messagebox
from datetime import datetime
tasks = []
def add_task():
    task_name = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()
    if not task_name:
        messagebox.showwarning("Input Error", "Task cannot be empty")
        return
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date format")
            return
    tasks.append({
        "task": task_name,
        "status": "Pending",
        "priority": priority,
        "due_date": due_date
    })
    update_task_list()
    task_entry.delete(0, END)
    due_date_entry.delete(0, END)
def delete_task():
    try:
        selected = task_list.curselection()[0]
        tasks.pop(selected)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected")
def complete_task():
    try:
        selected = task_list.curselection()[0]
        tasks[selected]["status"] = "Completed"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected")
def search_task():
    keyword = search_entry.get().lower()
    task_list.delete(0, END)
    for t in tasks:
        if keyword in t["task"].lower():
            due = t["due_date"] if t["due_date"] else "N/A"
            task_list.insert(END, f"{t['task']} | {t['status']} | {t['priority']} | {due}")
    search_entry.delete(0, END)
def update_task_list():
    task_list.delete(0, END)
    for idx, t in enumerate(tasks):
        due = t["due_date"] if t["due_date"] else "N/A"
        display = f"{t['task']} | {t['status']} | {t['priority']} | {due}"
        task_list.insert(END, display)
        if t["status"] == "Completed":
            task_list.itemconfig(idx, fg="green")
        elif t["priority"] == "High":
            task_list.itemconfig(idx, fg="red")
        elif t["priority"] == "Medium":
            task_list.itemconfig(idx, fg="orange")
        else:
            task_list.itemconfig(idx, fg="blue")
root = Tk()
root.title("To-Do List")
Label(root, text="Task:").grid(row=0, column=0)
task_entry = Entry(root, width=30)
task_entry.grid(row=0, column=1)
Label(root, text="Priority:").grid(row=1, column=0)
priority_var = StringVar(value="Medium")
OptionMenu(root, priority_var, "High", "Medium", "Low").grid(row=1, column=1)
Label(root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0)
due_date_entry = Entry(root, width=30)
due_date_entry.grid(row=2, column=1)
Button(root, text="Add Task", command=add_task).grid(row=3, column=0, columnspan=2, pady=5)
task_list = Listbox(root, width=60)
task_list.grid(row=4, column=0, columnspan=2, pady=5)
Button(root, text="Complete Task", command=complete_task).grid(row=5, column=0)
Button(root, text="Delete Task", command=delete_task).grid(row=5, column=1)
Label(root, text="Search:").grid(row=6, column=0)
search_entry = Entry(root, width=30)
search_entry.grid(row=6, column=1)
Button(root, text="Search", command=search_task).grid(row=7, column=0, columnspan=2, pady=5)
root.mainloop()