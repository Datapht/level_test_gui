import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Home Page")
        label.pack()

        logout_button = tk.Button(self, text="Logout", command=lambda: self.controller.show_frame("LoginPage"))
        logout_button.pack()