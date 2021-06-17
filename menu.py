#----Import system----
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import pygame

#----Import resources----
from settings.settings import Settings
from login_page import Login
from pages.front_page import FrontPage
from pages.view_book import Categories
from pages.rental import Rental
from pages.view_book_detail import BookDetail
from pages.add_book import Add
from pages.delete_book import Delete

#----Machine----
class Machine(tk.Tk):

	#---Primary configuration---
	def __init__(self, Engine):
		self.engine = Engine
		self.settings = Engine.settings

		self.x = 0

		#---About machine---
		super().__init__()
		self.title(self.settings.title)
		self.iconbitmap(self.settings.window_icon)
		self.geometry(self.settings.screen)
		self.resizable(False, False)

		self.music()

		self.pages = {}

		#---Calling all function available for the screen---
		self.create_container()
		self.create_rental()
		self.create_add_page()
		self.create_delete_page()
		self.create_view_book()
		self.create_view_page()
		self.create_front_page()

	def music(self):
		pygame.mixer.init()
		pygame.mixer.music.load("image/MoonlikeSmile.mp3")
		pygame.mixer.music.set_volume(0.3)
		pygame.mixer.music.play(-1, 0.0)

	def play_audio(self):
		pygame.mixer.music.unpause()
		self.pages['front_page'].button_audio.configure(image=self.pages['front_page'].sound_background, command=self.stop_audio)

	def stop_audio(self):
		pygame.mixer.music.pause()
		self.pages['front_page'].button_audio.configure(image=self.pages['front_page'].no_sound_background, command=self.play_audio)

	#---Container & pages---
	def create_container(self):
		self.container = tk.Frame(bg="white")
		self.container.pack(side='top', fill='both', expand=True)

	def create_front_page(self):
		self.pages['front_page'] = FrontPage(self.container, self)

	def create_view_page(self):
		self.pages['view_page'] = Categories(self.container, self)

	def create_view_book(self):
		self.pages['book_page'] = BookDetail(self.container, self)

	def create_add_page(self):
		self.pages['add_page'] = Add(self.container, self)

	def create_delete_page(self):
		self.pages['delete_page'] = Delete(self.container, self)

	def create_rental(self):
		self.pages['rental'] = Rental(self.container, self)

	def change_to_view(self):
		if self.x >= 1:
			self.pages['book_page'].listBox.delete(0, len(self.pages['book_page'].contents))
			self.pages['book_page'].view_canvas.itemconfigure(self.pages['book_page'].title_book, text="")
			self.pages['book_page'].view_canvas.itemconfigure(self.pages['book_page'].year_book, text="")
			self.pages['book_page'].view_canvas.itemconfigure(self.pages['book_page'].publish_book, text="")
			self.pages['book_page'].view_canvas.itemconfigure(self.pages['book_page'].creator_book, text="")
		else :
			pass
		self.settings.update_available = 0
		self.notification()
		self.pages['view_page'].tkraise()

	def return_to_menu(self):
		self.pages['front_page'].tkraise()
		self.checking_update()

	def change_to_add(self):
		self.pages['add_page'].tkraise()

	def go_to_rental(self):
		self.pages['rental'].tkraise()

	def change_to_delete(self):
		self.pages['delete_page'].tkraise()

	def change_to_view_book(self, genre):
		self.settings.load_data()
		if genre == "horror":
			self.pages['book_page'].create_contents('horror')
			self.x += 1
		elif genre == "fantasy":
			self.pages['book_page'].create_contents('fantasy')
			self.x += 1
		elif genre == "comedy":
			self.pages['book_page'].create_contents('comedy')
			self.x += 1
		elif genre == "action":
			self.pages['book_page'].create_contents('action')
			self.x += 1
		elif genre == "romance":
			self.pages['book_page'].create_contents('romance')
			self.x += 1
		elif genre == "drama":
			self.pages['book_page'].create_contents('drama')
			self.x += 1
		elif genre == "sci-fi":
			self.pages['book_page'].create_contents('sci-fi')
			self.x += 1
		elif genre == "education":
			self.pages['book_page'].create_contents('education')
			self.x += 1
		else :
			pass
		self.pages['book_page'].tkraise()

	#---Secondary function---
	def notification(self):
		notif = Image.open(self.settings.notif)
		iW, iH = notif.size 
		newSize = (int(30), int(25))
		notif = notif.resize(newSize)

		self.notif_available = ImageTk.PhotoImage(notif)
		if self.settings.update_available == 1:
			self.pages['front_page'].front_canvas.create_image(610, 200, image=self.notif_available, anchor="nw")
		else :
			self.pages['front_page'].front_canvas.delete("all")
			self.create_front_page()

	def checking_update(self):
		if self.settings.update_available == 1:
			self.notification()
			update_add = messagebox.showinfo("Update available", "New book has been added, let's check it out!")
		else:
			pass

	def exit(self):
		exit()

#----Engine----
class Engine:

	#---Primary configuration---
	def __init__(self):
		self.settings = Settings()

		self.login = Login(self)

	def run(self):
		self.login.mainloop()

	def continue_to_app(self):
		self.login.destroy()
		self.machine = Machine(self)
		self.machine.mainloop()

#----Runner----
if __name__ == '__main__':
	Project = Engine()
	Project.run()