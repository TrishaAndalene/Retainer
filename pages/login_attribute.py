#----Import system----
import tkinter as tk
from PIL import Image, ImageTk
from json import dump
import pygame

#----Login Page----
class LoginPage(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		#---Configuration---
		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_main_frame()

	def create_main_frame(self):
		self.main_frame = tk.Frame(self, bg='pink', width=self.settings.login_width)
		self.main_frame.grid(column=0, row=0, sticky='nesw')

		self.create_base_frame()
		self.create_background()
		self.create_labels()
		self.create_entry()
		self.create_button()
		self.sign_up()

	def create_base_frame(self):
		self.base = tk.Frame(self.main_frame, bg='white', width=self.settings.login_width, height=self.settings.login_height)
		self.base.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

	def create_background(self):
		image = Image.open(self.settings.login_background)
		iW, iH = image.size
		ratio = iW/self.settings.login_width
		newSize = (int(iW/ratio), int(self.settings.login_height))
		image = image.resize(newSize)
		
		#---Define Image---
		self.login_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.login_canvas = tk.Canvas(self.base, width=self.settings.login_width, height=self.settings.login_height)
		self.login_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.login_canvas.create_image(0, 0, image=self.login_background, anchor="nw")

	def create_labels(self):
		self.title = self.login_canvas.create_text(185, 90, text="Log in", font=("Times", 60), fill="RoyalBlue1")
		self.username_label = self.login_canvas.create_text(115, 150, text='Username :', font=("Helvetica", 20, "bold"), fill='white')
		self.password_label = self.login_canvas.create_text(115, 225, text='Password :', font=("Helvetica", 20, "bold"), fill='white')

	def create_entry(self):
		self.username_var = tk.StringVar()
		self.username_entry = tk.Entry(self.base, width=25, font=('Helvetica', 12), textvariable=self.username_var)
		self.username_window = self.login_canvas.create_window(40, 175, anchor='nw', window=self.username_entry)

		self.password_var = tk.StringVar()
		self.password_entry = tk.Entry(self.base, width=25, font=('Helvetica', 12), textvariable=self.password_var, show="*")
		self.password_window = self.login_canvas.create_window(40, 250, anchor="nw", window=self.password_entry)


	def create_button(self):
		self.login_button = tk.Button(self.base, text='Log in', font=('Helvetica', 15), command=self.checking)
		self.login_button_window = self.login_canvas.create_window(150, 350, anchor='nw', window=self.login_button)

	def sign_up(self):
		self.sign_up_button = tk.Button(self.base, text='Sign up', font=('Helvetica', 10), command=self.app.sign_up)
		self.sign_up_button_window = self.login_canvas.create_window(300, 10, anchor='nw', window=self.sign_up_button)

	def checking(self):
		self.password = self.password_var.get()
		self.username = self.username_var.get()

		self.account_list = self.settings.username

		for account in self.account_list:
			for key, value in account.items():
				if key == self.username and value['password'] == self.password:
					self.app.engine.continue_to_app()
				else :
					"[!] Wrong username or password"
		else :
			print("[!] Account has not been added yet")

#----Sign up----
class Sign_up(tk.Frame):
	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		self.account = self.settings.username

		#---Configuration---
		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_main_frame()

	def create_main_frame(self):
		self.main_frame = tk.Frame(self, bg='pink', width=self.settings.login_width)
		self.main_frame.grid(column=0, row=0, sticky='nesw')

		self.create_base_frame()
		self.create_background()
		self.create_labels()
		self.create_entry()
		self.create_button()

	def create_base_frame(self):
		self.base = tk.Frame(self.main_frame, bg='white', width=self.settings.login_width, height=self.settings.login_height)
		self.base.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

	def create_background(self):
		image = Image.open(self.settings.login_background)
		iW, iH = image.size
		ratio = iW/self.settings.login_width
		newSize = (int(iW/ratio), int(self.settings.login_height))
		image = image.resize(newSize)
		
		#---Define Image---
		self.login_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.login_canvas = tk.Canvas(self.base, width=self.settings.login_width, height=self.settings.login_height)
		self.login_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.login_canvas.create_image(0, 0, image=self.login_background, anchor="nw")

	def create_labels(self):
		self.title = self.login_canvas.create_text(185, 90, text="Sign up", font=("Times", 60), fill="RoyalBlue1")
		self.username_label = self.login_canvas.create_text(115, 150, text='Username :', font=("Helvetica", 20, "bold"), fill='white')
		self.password_label = self.login_canvas.create_text(115, 225, text='Password :', font=("Helvetica", 20, "bold"), fill='white')

	def create_entry(self):
		self.new_username = tk.StringVar()
		self.new_username_entry = tk.Entry(self.base, width=25, font=('Helvetica', 12), textvariable=self.new_username)
		self.new_username_window = self.login_canvas.create_window(40, 175, anchor='nw', window=self.new_username_entry)

		self.new_password = tk.StringVar()
		self.new_password_entry = tk.Entry(self.base, width=25, font=('Helvetica', 12), textvariable=self.new_password)
		self.new_password_window = self.login_canvas.create_window(40, 250, anchor="nw", window=self.new_password_entry)

	def create_button(self):
		self.signup_button = tk.Button(self.base, text='Sign up', font=('Helvetica', 15), command=self.add_account)
		self.signup_button_window = self.login_canvas.create_window(150, 350, anchor='nw', window=self.signup_button)

	def add_account(self):
		self.path = 'Library/account.json'
		self.contex = self.account

		self.username = self.new_username.get()
		self.password = self.new_password.get()

		self.content = {
			self.username :{
				"password" : self.password
			}
		}

		self.contex.append(self.content)
		with open(self.path, "w") as file_json:
			dump(self.contex, file_json)

		self.app.change_back_to_login()