import tkinter as tk
from PIL import Image, ImageTk



class StartPage(tk.Frame):
	def __init__(self, parent, App):
		self.application = App
		self.config = App.config

		super().__init__(parent)
		self.configure(bg="pale violet red")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, height=self.config.height, width=self.config.width, bg="pale violet red")
		self.main_frame.pack(expand=True)

		image = Image.open(self.config.startPage_img)
		image_w, image_h = image.size
		ratio = image_w/self.config.width
		image = image.resize((int(image_w//ratio//2),int(image_h//ratio//2)))

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(pady=5)


		self.btn_start = tk.Button(self.main_frame, text="START", font=("FreeSerif", 18, "bold"), command=lambda:self.application.change_page("loginPage"))
		self.btn_start.pack(pady=5)


