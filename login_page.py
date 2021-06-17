#----Import system----
import tkinter as tk
from PIL import Image, ImageTk

#----Import Module----
from pages.login_attribute import LoginPage, Sign_up

#----Screen----
class Login(tk.Tk):
	
	#---Primary configuration---
	def __init__(self, Engine):
		self.engine = Engine
		self.settings = Engine.settings

		#---About machine---
		super().__init__()
		self.title(self.settings.title)
		self.iconbitmap(self.settings.window_icon)
		self.geometry(self.settings.login_screen)
		self.resizable(False, False)

		self.pages = {}

		#---Function for screen preview---
		self.create_container()
		self.create_sign_up_page()
		self.create_login_page()

		#---Container & pages---
	def create_container(self):
		self.container = tk.Frame(bg="white")
		self.container.pack(side='top', fill='both', expand=True)

	def create_login_page(self):
		self.pages['login_page'] = LoginPage(self.container, self)

	def create_sign_up_page(self):
		self.pages['sign_up'] = Sign_up(self.container, self)

	def sign_up(self):
		self.pages['sign_up'].tkraise()

	def change_back_to_login(self):
		self.pages['login_page'].username_entry.insert(0, self.pages['sign_up'].username)
		self.pages['login_page'].password_entry.insert(0, self.pages['sign_up'].password)
		self.pages['login_page'].tkraise()