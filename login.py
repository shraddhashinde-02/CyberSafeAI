import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Please enter Username and Password.")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        subprocess.Popen(["python", "app.py"])
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def open_register():
    subprocess.Popen(["python", "register.py"])


# ---------------- GUI ----------------

root = tk.Tk()
root.title("CyberSafe AI - Login")
root.geometry("400x350")
root.configure(bg="#1E1E1E")

title = tk.Label(
    root,
    text="CyberSafe AI",
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

login_btn = tk.Button(
    root,
    text="Login",
    width=15,
    command=login,
    bg="cyan"
)
login_btn.pack(pady=10)

register_btn = tk.Button(
    root,
    text="Register",
    width=15,
    command=open_register
)
register_btn.pack()

root.mainloop()