#loginPage.py
import tkinter as tk
from PIL import Image, ImageTk


class LoginPage(tk.Frame):
    def __init__(self, parent, App):
        self.application = App
        self.config = App.config

        super().__init__(parent)
        self.configure(bg="maroon1")
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        #CREATE MAIN FRAME
        self.main_frame = tk.Frame(self, height=self.config.side, width=self.config.side, bg="maroon1")
        self.main_frame.pack(expand=True)

        image = Image.open(self.config.loginPage_img)
        image_w, image_h = image.size
        ratio = image_w/self.config.width
        image = image.resize((int(image_w//ratio//2),int(image_h//ratio//2)))

        self.logo = ImageTk.PhotoImage(image)
        self.label_logo = tk.Label(self.main_frame, image=self.logo)
        self.label_logo.pack(pady=5)

        self.label_username = tk.Label(self.main_frame, text="username", font=("Times", 18, "bold"), bg="maroon1", fg="white")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(self.main_frame, font=("Times", 16, "bold"))
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.main_frame, text="password", font=("Times", 18, "bold"), bg="maroon1", fg="white")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self.main_frame, font=("Times", 16, "bold"), show="*")
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(self.main_frame, text="LOGIN", font=("Times", 18, "bold"), command=lambda:self.application.change_page("board"))
        self.btn_login.pack(pady=5)

