import tkinter as tk
from tkinter import PhotoImage

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Load background image
        image_path = "data/img.png"  # Update with the correct path to your image
        self.bg_image = PhotoImage(file=image_path)
        
        # Create a label to display the background image
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Username entry
        self.username_entry = tk.Entry(self)
        self.username_entry.place(relx=0.73, rely=0.365, anchor=tk.CENTER)

        # Password entry
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.place(relx=0.73, rely=0.5, anchor=tk.CENTER)

        # Login button
        login_button = tk.Button(self, text="Login", command=self.verify_login)
        login_button.place(relx=0.73, rely=0.595, anchor=tk.CENTER)

    def verify_login(self):
        # Fetch the username and password from the input fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy verification logic, replace it with your actual verification process
        if username == "admin" and password == "password":
            print("Login successful")
            # Switch to the home page upon successful login
            self.controller.show_frame("HomePage")
        else:
            print("Invalid username or password")

