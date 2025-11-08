import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()

# Window title and size
root.title("Task Management System")
root.geometry("400x400")

# A simple label to check the window
label = tk.Label(root, text="Welcome to your Task Manager!", font=("Arial", 14))
label.pack(pady=20)

# Keep window running
root.mainloop()
