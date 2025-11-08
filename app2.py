import tkinter as tk
from tkinter import messagebox

# ----- List to store all tasks -----
tasks = []

# ----- Function to add a task -----
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

# ----- Function to update the task list on screen -----
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# ----- Main Tkinter window -----
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

# ----- Entry box for typing a new task -----
entry = tk.Entry(root, width=35)
entry.pack(pady=10)

# ----- Button to add a new task -----
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# ----- Listbox to display tasks -----
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# ----- Run the window -----
root.mainloop()
