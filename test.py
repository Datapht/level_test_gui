import tkinter as tk
from tkinter import PhotoImage

def verify_login():
    # Fetch the username and password from the input fields
    username = username_entry.get()
    password = password_entry.get()

    # Dummy verification logic, replace it with your actual verification process
    if username == "admin" and password == "password":
        print("Login successful")
    else:
        print("Invalid username or password")

root = tk.Tk()
root.title("Device Stability Testing")  
root.resizable(False, False)
root.geometry("810x490")

# Background image
image_path = PhotoImage(file="data/img.png")
bg_image = tk.Label(root, image=image_path)
bg_image.place(relwidth=1, relheight=1)


username_entry = tk.Entry(root)
username_entry.place(relx=0.73, rely=0.365, anchor=tk.CENTER)


password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.73, rely=0.5, anchor=tk.CENTER)

# Login button
login_button = tk.Button(root, text="Login", command=verify_login)
login_button.place(relx=0.73, rely=0.595, anchor=tk.CENTER)

root.mainloop()
