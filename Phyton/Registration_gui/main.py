import tkinter as tk
import sqlite3

def register_user():
    def register():
        username = new_username_entry.get()
        password = new_password_entry.get()
        if username and password:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            register_window.destroy()

    register_window = tk.Toplevel(root)
    new_username_label = tk.Label(register_window, text="Username:")
    new_username_label.grid(row=0, column=0)
    new_username_entry = tk.Entry(register_window)
    new_username_entry.grid(row=0, column=1)
    new_password_label = tk.Label(register_window, text="Password:")
    new_password_label.grid(row=1, column=0)
    new_password_entry = tk.Entry(register_window, show="*")
    new_password_entry.grid(row=1, column=1)
    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.grid(row=2, column=0, columnspan=2)


def login():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        success_label.config(text="Login successful!")
    else:
        success_label.config(text="Login failed.")


root = tk.Tk()
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0)
register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=2, column=1)
success_label = tk.Label(root, text="")
success_label.grid(row=3, column=0, columnspan=2)

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Удаляем таблицу, если она существует, чтобы гарантировать правильную структуру
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("CREATE TABLE users (username TEXT, password TEXT)") # Создаем таблицу с нужными столбцами
conn.commit()
conn.close()

root.mainloop()