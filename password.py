import tkinter as tk
import string
import random

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    password_label.config(text=password)

app = tk.Tk()
app.title("Strong Password Generator")
app.configure(bg='green') 

password_label = tk.Label(app, text="", width=50, height=1)
password_label.pack(padx=20, pady=20)

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(padx=20, pady=20)

app.mainloop()