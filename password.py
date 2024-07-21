import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def create_gradient(canvas, width, height, color1, color2, color3):

    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)
    r_ratio1 = float(r2 - r1) / (height / 2)
    g_ratio1 = float(g2 - g1) / (height / 2)
    b_ratio1 = float(b2 - b1) / (height / 2)

    for i in range(int(height / 2)):
        nr = int(r1 + (r_ratio1 * i))
        ng = int(g1 + (g_ratio1 * i))
        nb = int(b1 + (b_ratio1 * i))
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)


    (r3, g3, b3) = canvas.winfo_rgb(color3)
    r_ratio2 = float(r3 - r2) / (height / 2)
    g_ratio2 = float(g3 - g2) / (height / 2)
    b_ratio2 = float(b3 - b2) / (height / 2)

    for i in range(int(height / 2), height):
        nr = int(r2 + (r_ratio2 * (i - height / 2)))
        ng = int(g2 + (g_ratio2 * (i - height / 2)))
        nb = int(b2 + (b_ratio2 * (i - height / 2)))
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

create_gradient(canvas, 400, 300, "#ff7e5f", "#feb47b", "#ff7e5f")


length_label = tk.Label(canvas, text="Enter password length:", bg="#feb47b", fg="#2c3e50", font=("Arial", 14, "bold"))
length_label.pack(pady=10)

length_entry = tk.Entry(canvas, width=20, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
length_entry.pack(pady=10)

password_label = tk.Label(canvas, text="Generated Password:", bg="#feb47b", fg="#2c3e50", font=("Arial", 14, "bold"))
password_label.pack(pady=10)

password_entry = tk.Entry(canvas, width=20, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
password_entry.pack(pady=10)


generate_button = tk.Button(canvas, text="Generate Password", command=lambda: generate_password(int(length_entry.get())), bg="#27ae60", fg="#ecf0f1", font=("Arial", 12, "bold"), activebackground="#2ecc71", activeforeground="#ecf0f1")
generate_button.pack(pady=10)

copy_button = tk.Button(canvas, text="Copy Password", command=copy_password, bg="#2980b9", fg="#ecf0f1", font=("Arial", 12, "bold"), activebackground="#3498db", activeforeground="#ecf0f1")
copy_button.pack(pady=10)

root.mainloop()