import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150")

tk.Label(root, text="Password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

tk.Button(root, text="Generate", command=generate_password).pack(pady=10)

result_entry = tk.Entry(root, font="Arial 12")
result_entry.pack(pady=5)

root.mainloop()