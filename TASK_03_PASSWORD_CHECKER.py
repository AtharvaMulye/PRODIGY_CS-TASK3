import tkinter as tk
from tkinter import messagebox

def load_common_passwords(file_path):
    with open(file_path, 'r') as file:
        return {line.strip() for line in file}

COMMON_PASSWORD_FILE_PATH = 'C:/Users/Atharv/Desktop/CYBERSEC INTERN/TASKS/TASK_3(PASSWORD_CHECKER)/common_password.txt'

def check_password_complexity(password, common_passwords):
    if password in common_passwords:
        return "weak"
    if len(password) < 8:
        return "weak"
    if len(password) < 12:
        return "medium"
    return "strong"

def validate_password():
    password = password_entry.get().strip()
    common_passwords = load_common_passwords(COMMON_PASSWORD_FILE_PATH)
    try:
        if len(password) < 6:
            raise ValueError("Password should be at least 6 characters long!")
        has_special_char = any(not char.isalnum() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_num = any(char.isnumeric() for char in password)
        if not has_upper:
            raise ValueError("Password must contain at least 1 uppercase character!")
        if not has_lower:
            raise ValueError("Password must contain at least 1 lowercase character!")
        if not has_num:
            raise ValueError("Password must contain at least 1 number!")
        if not has_special_char:
            raise ValueError("Password must contain at least 1 special character!")
        complexity = check_password_complexity(password, common_passwords)
        complexity_label.config(text=f"Password complexity: {complexity.capitalize()}", fg="green")
    except ValueError as ve:
        complexity_label.config(text=f"Error: {ve}", fg="red")
        
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
        
root = tk.Tk()
root.title("Password Checker")
root.geometry("400x280")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

header_label = tk.Label(root, text="Password Checker", bg="#1E1E1E", fg="#03a9f4", font=("Arial", 24, "bold"))
header_label.pack(pady=10)

password_label = tk.Label(root, text="Enter your password:", bg="#1E1E1E", fg="#ffffff", font=("Arial", 12))
password_label.pack()
password_entry = tk.Entry(root, show="*", bg="#ffffff", fg="#333333", font=("Arial", 12), bd=2, relief="solid", highlightbackground="#03a9f4")
password_entry.pack(pady=5, padx=10, ipadx=50, ipady=5) 

show_password_var = tk.BooleanVar()
show_password_var.set(False)
show_password_button = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password_visibility, bg="#1E1E1E", fg="#ffffff", font=("Arial", 10))
show_password_button.pack(pady=5)

check_button = tk.Button(root, text="Check", command=validate_password, bg="#03a9f4", fg="#ffffff", font=("Arial", 12), bd=2, relief="raised", highlightbackground="#03a9f4", activebackground="#0288d1")
check_button.pack(pady=10)

complexity_label = tk.Label(root, text="", bg="#1E1E1E", fg="#ffffff", font=("Arial", 12), wraplength=350)
complexity_label.pack()

root.mainloop()