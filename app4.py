import tkinter as tk
from tkinter import messagebox
import json

# ----- List to store all tasks -----
tasks = []

# ----- Add a new task -----
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

# ----- Update the listbox -----
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# ----- Delete a selected task -----
def delete_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        tasks.remove(selected_task)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

# ----- Mark a selected task as complete -----
def complete_task():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if not task.startswith("✔️"):
            tasks[index] = f"✔️ {task}"
            update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to complete")

# ----- Save tasks to a file -----
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    messagebox.showinfo("Saved", "Tasks have been saved successfully!")

# ----- Load tasks from a file -----
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        update_listbox()
    except FileNotFoundError:
        tasks = []

# ----- Main window -----
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

# ----- Entry box -----
entry = tk.Entry(root, width=35)
entry.pack(pady=10)

# ----- Buttons -----
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Complete", command=complete_task)
complete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)

# ----- Listbox -----
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# ----- Load saved tasks when app starts -----
load_tasks()

# ----- Start the app -----
root.mainloop()
