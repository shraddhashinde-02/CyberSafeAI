import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from password import check_password
from phishing import check_url
from malware import scan_file


# ---------------------- Functions ----------------------

def password_checker():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    result = check_password(password)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def url_checker():
    url = url_entry.get()

    if url == "":
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

    result = check_url(url)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def malware_checker():
    file_path = filedialog.askopenfilename()

    if file_path == "":
        return

    result = scan_file(file_path)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def clear_all():
    password_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)

    output_box.delete("1.0", tk.END)


# ---------------------- Main Window ----------------------

root = tk.Tk()

root.title("CyberSafe AI")
root.geometry("700x650")
root.configure(bg="#1E1E1E")

title = tk.Label(
    root,
    text="CyberSafe AI",
    font=("Arial", 22, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)

title.pack(pady=15)


# ---------------- Password ----------------

password_label = tk.Label(
    root,
    text="Enter Password",
    bg="#1E1E1E",
    fg="white",
    font=("Arial", 12)
)

password_label.pack()

password_entry = ttk.Entry(
    root,
    width=45,
    show="*"
)

password_entry.pack(pady=5)

password_button = ttk.Button(
    root,
    text="Check Password",
    command=password_checker
)

password_button.pack(pady=10)


# ---------------- URL ----------------

url_label = tk.Label(
    root,
    text="Enter Website URL",
    bg="#1E1E1E",
    fg="white",
    font=("Arial", 12)
)

url_label.pack()

url_entry = ttk.Entry(
    root,
    width=45
)

url_entry.pack(pady=5)

url_button = ttk.Button(
    root,
    text="Check URL",
    command=url_checker
)

url_button.pack(pady=10)


# ---------------- Malware ----------------

file_button = ttk.Button(
    root,
    text="Scan File",
    command=malware_checker
)

file_button.pack(pady=15)


# ---------------- Output ----------------

output_label = tk.Label(
    root,
    text="Result",
    bg="#1E1E1E",
    fg="white",
    font=("Arial", 12)
)

output_label.pack()

output_box = tk.Text(
    root,
    width=70,
    height=15,
    font=("Consolas", 10)
)

output_box.pack(pady=10)


# ---------------- Clear ----------------

clear_button = ttk.Button(
    root,
    text="Clear",
    command=clear_all
)

clear_button.pack(pady=10)


# ---------------- Footer ----------------

footer = tk.Label(
    root,
    text="CyberSafe AI | Developed in Python",
    bg="#1E1E1E",
    fg="gray"
)

footer.pack(side="bottom", pady=10)


root.mainloop()