import tkinter as tk
from tkinter import PhotoImage
from pages.login_page import LoginPage
from pages.testing_page import HomePage

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Device Stability Testing")  
        self.resizable(False, False)
        self.geometry("810x490")

        # Background image
        image_path = PhotoImage(file="data/img.png")
        bg_image = tk.Label(self, image=image_path)
        bg_image.place(relwidth=1, relheight=1)

        container = tk.Frame(self)
        container.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frames = {}
        for F in (LoginPage, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)
        
        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
