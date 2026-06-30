import tkinter as tk
from tkinter import messagebox
import sqlite3

def register():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

    conn.close()


root = tk.Tk()
root.title("CyberSafe AI - Register")
root.geometry("400x300")
root.configure(bg="#1E1E1E")

title = tk.Label(
    root,
    text="Create Account",
    font=("Arial", 20, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)
title.pack(pady=20)

tk.Label(root, text="Username", bg="#1E1E1E", fg="white").pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password", bg="#1E1E1E", fg="white").pack()

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

register_btn = tk.Button(
    root,
    text="Register",
    command=register,
    bg="cyan"
)
register_btn.pack(pady=20)

root.mainloop()