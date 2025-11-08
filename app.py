import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Task Management System")
root.geometry("400x400")

# Optional: add a label to confirm it’s working
label = tk.Label(root, text="Hello, this is your Task Manager!", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()

