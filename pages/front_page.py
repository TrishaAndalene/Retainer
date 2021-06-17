#----Import system----
import tkinter as tk
from PIL import Image, ImageTk
import pygame

#----Front Page----
class FrontPage(tk.Frame):

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
		self.main_frame = tk.Frame(self, bg='pink', width=self.settings.width)
		self.main_frame.grid(column=0, row=0, sticky='nesw')

		self.create_front_frame()
		self.create_background()
		self.create_title_text()
		self.create_button()
		self.with_without_audio()

	def create_front_frame(self):
		self.front_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.front_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

	def create_background(self):

		image = Image.open(self.settings.menu_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.menu_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.front_canvas = tk.Canvas(self.front_frame, width=960, height=510)
		self.front_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.front_canvas.create_image(0, 0, image=self.menu_background, anchor="nw")

	def create_title_text(self):
		self.front_canvas.create_text(480, 100, text="Retainer", font=("Times", 60), fill="#6c78a7")

	def create_button(self):
		continue_ = ""
		button1 = tk.Button(self.front_frame, text="View", font=("Helvetica", 20), bg="#6c78a7", fg="#363d59", padx=85, command=self.app.change_to_view)
		button2 = tk.Button(self.front_frame, text="Add", font=("Helvetica", 20), bg="#6c78a7", fg="#363d59", padx=89.5, command=self.app.change_to_add)
		button3 = tk.Button(self.front_frame, text="Delete", font=("Helvetica", 20), bg="#6c78a7", fg="#363d59", padx=74, command=self.app.change_to_delete)
		button4 = tk.Button(self.front_frame, text="Rentalist", font=("Helvetica", 20), bg="#6c78a7", fg="#363d59", padx=60, command=self.app.go_to_rental)
		button5 = tk.Button(self.front_frame, text="Logout", font=("Helvetica", 20), bg="#6c78a7", fg="#363d59", padx=72, command=self.app.exit)

		button1_win = self.front_canvas.create_window(360, 200, anchor="nw", window=button1)
		button2_win = self.front_canvas.create_window(360, 260, anchor="nw", window=button2)
		button3_win = self.front_canvas.create_window(360, 320, anchor="nw", window=button3)
		button4_win = self.front_canvas.create_window(360, 380, anchor="nw", window=button4)
		button5_win = self.front_canvas.create_window(360, 440, anchor="nw", window=button5)

	def with_without_audio(self):
		no_sound = Image.open(self.settings.no_sound)
		iW, iH = no_sound.size 
		newSize = (int(30), int(30))
		no_sound = no_sound.resize(newSize)

		sound = Image.open(self.settings.sound)
		iW, iH = sound.size
		newSize = (int(30), int(30))
		sound = sound.resize(newSize)

		#---Define Image---
		self.sound_background = ImageTk.PhotoImage(sound)
		self.no_sound_background = ImageTk.PhotoImage(no_sound)

		self.button_audio = tk.Button(self.front_frame, image=self.sound_background, command=self.app.stop_audio)
		button_audio = self.front_canvas.create_window(900, 460, anchor='nw', window=self.button_audio)

	def notification(self):
		notif = Image.open(self.settings.notif)

		self.notif_available = ImageTk.PhotoImage(notif)
		if self.settings.update_available == 1:
			self.front_canvas.create_image(500, 200, image=self.notif_available, anchor="nw")