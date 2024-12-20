import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("Генератор паролей")
root.geometry("400x400")
root.resizable(False, False)

def generate_password():
    length = password_length.get()
    chars = ''
    if include_uppercase.get():
        chars += string.ascii_uppercase
    if include_lowercase.get():
        chars += string.ascii_lowercase
    if include_digits.get():
        chars += string.digits
    if include_symbols.get():
        chars += string.punctuation
    if chars == '':
        messagebox.showwarning("Ошибка", "Выберите хотя бы один набор символов!")
        return
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Успех", "Пароль скопирован в буфер обмена!")

password_length = tk.IntVar(value=12)
include_uppercase = tk.BooleanVar(value=True)
include_lowercase = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=False)

settings_frame = tk.LabelFrame(root, text="Настройки пароля", padx=10, pady=10)
settings_frame.pack(pady=10)

length_label = tk.Label(settings_frame, text="Длина пароля:")
length_label.grid(row=0, column=0, sticky="w")
length_scale = tk.Scale(settings_frame, from_=4, to=32, orient=tk.HORIZONTAL, variable=password_length)
length_scale.grid(row=0, column=1, padx=5, pady=5)

uppercase_check = tk.Checkbutton(settings_frame, text="Включить заглавные буквы", variable=include_uppercase)
uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w")
lowercase_check = tk.Checkbutton(settings_frame, text="Включить строчные буквы", variable=include_lowercase)
lowercase_check.grid(row=2, column=0, columnspan=2, sticky="w")
digits_check = tk.Checkbutton(settings_frame, text="Включить цифры", variable=include_digits)
digits_check.grid(row=3, column=0, columnspan=2, sticky="w")
symbols_check = tk.Checkbutton(settings_frame, text="Включить символы", variable=include_symbols)
symbols_check.grid(row=4, column=0, columnspan=2, sticky="w")

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=10)

password_frame = tk.Frame(root)
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Сгенерированный пароль:")
password_label.pack(side=tk.LEFT)

password_entry = tk.Entry(password_frame, width=24)
password_entry.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(password_frame, text="Копировать", command=copy_password)
copy_button.pack(side=tk.LEFT)

root.configure(bg="#f0f0f0")
settings_frame.configure(bg="#f0f0f0")
length_label.configure(bg="#f0f0f0")
uppercase_check.configure(bg="#f0f0f0")
lowercase_check.configure(bg="#f0f0f0")
digits_check.configure(bg="#f0f0f0")
symbols_check.configure(bg="#f0f0f0")
password_label.configure(bg="#f0f0f0")
password_frame.configure(bg="#f0f0f0")

generate_button.configure(bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
copy_button.configure(bg="#2196F3", fg="white")

root.mainloop()
