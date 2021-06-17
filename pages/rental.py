#----Import system----
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from json import dump, load

#----Add Page [book index]----
class Rental(tk.Frame):

	def __init__(self, parent, Engine):
		self.engine = Engine
		self.settings = Engine.settings

		#---Path---
		self.horror = self.settings.horrors
		self.comedy = self.settings.comedies
		self.fantasy = self.settings.fantasies
		self.action = self.settings.actions
		self.romance = self.settings.romances
		self.sci_fi = self.settings.sci_fis
		self.drama = self.settings.dramas
		self.education = self.settings.educations

		#---Configuration---
		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")
		self.configure(bg='yellow')

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_main_frame()

	def create_main_frame(self):
		self.main_frame = tk.Frame(self, bg='pink', width=self.settings.width)
		self.main_frame.grid(column=0, row=0, sticky='nesw')

		self.create_base_frame()

	def create_base_frame(self):
		self.base_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.base_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

		self.create_background()
		self.create_back_button()
		self.create_labels()
		self.create_entries()
		self.create_genre_box()
		self.create_buttons()

	def create_background(self):
		image = Image.open(self.settings.delete_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.Rental_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.Rental_canvas = tk.Canvas(self.base_frame, width=960, height=510)
		self.Rental_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.Rental_canvas.create_image(0, 0, image=self.Rental_background, anchor="nw")

	def create_back_button(self):
		self.button_back = tk.Button(self.base_frame, text='   X   ', bg='red', fg='snow', font=("Arial", 12), command=self.clear_entry_and_return)
		self.button_back_window = self.Rental_canvas.create_window(910, 5, anchor="nw", window=self.button_back)

	def create_genre_box(self):
		self.style = ttk.Style()
		self.style.theme_create('combostyle', parent='alt', settings = {'TCombobox':{'configure':{'foreground' : 'white','fieldbackground': 'black','background': 'black'},'selectbackground': 'black'}}) #'selectbackground': 'white'
		self.style.theme_use('combostyle')

		self.Genre_Var = tk.StringVar()
		self.genreCombobox = ttk.Combobox(self.base_frame, textvariable=self.Genre_Var, font=('Times', 15), width=30)
		self.genreCombobox["values"] = ['Horror', 'Romance', 'Sci-Fi', 'Fantasy', 'Action', 'Comedy', 'Education', 'Drama']
		self.genreComboboxWindow = self.Rental_canvas.create_window(70, 180, anchor="nw", window=self.genreCombobox)

	def create_labels(self):
		self.Rental_canvas.create_text(280, 40, text='Rental A Book', font=("Times", 45), fill="goldenrod")
		self.Rental_canvas.create_text(90, 120, text='Title', font=("Times", 20), fill="goldenrod")
		'''
		self.Rental_canvas.create_text(95, 190, text='Note:', font=("Times", 20), fill="red")
		self.Rental_canvas.create_text(242, 220, text='Rentald book would not be able', font=("Times", 20), fill="red")
		self.Rental_canvas.create_text(138, 250, text='to be undone', font=("Times", 20), fill="red")
		'''

		self.Rental_canvas.create_text(110, 240, text='Status :', font=("Times", 20), fill="goldenrod")
		self.status = self.Rental_canvas.create_text(180, 240, text='|||||||||||', font=("Times", 20), fill="black")

	def create_entries(self):
		self.Title_var = tk.StringVar()
		self.entryTitle = tk.Entry(self.base_frame, textvariable=self.Title_var, width=32, font=("Times", 15), bg="black", fg="white")
		self.entryTitleWindow = self.Rental_canvas.create_window(70, 140, anchor="nw", window=self.entryTitle)

	def create_buttons(self):
		self.button_check = tk.Button(self.base_frame, text='Check', font=("Times", 10), bg='goldenrod', fg='black', command=self.check_function)
		self.button_check_window = self.Rental_canvas.create_window(400, 180, anchor='nw', window=self.button_check)

		self.button_Rental = tk.Button(self.base_frame, text='Rental', font=("Times", 15), bg='goldenrod', fg='black', command=self.haha)
		self.button_Rental_window = self.Rental_canvas.create_window(65, 390, anchor='nw', window=self.button_Rental)

	def check_function(self):
		self.title = self.Title_var.get()
		genre = self.Genre_Var.get()

		if genre == 'Horror':
			self.path = 'Library/horrors.json'
			self.contex = self.horror
		elif genre == 'Romance':
			self.path = 'Library/romance.json'
			self.contex = self.romance
		elif genre == 'Sci-Fi':
			self.path = 'Library/sci-fi.json'
			self.contex = self.sci_fi
		elif genre == 'Fantasy':
			self.path = 'Library/fantasy.json'
			self.contex = self.fantasy
		elif genre == 'Comedy':
			self.path = 'Library/comedy.json'
			self.contex = self.comedy
		elif genre == 'Action':
			self.path = 'Library/action.json'
			self.contex = self.action
		elif genre == 'Drama':
			self.path = 'Library/drama.json'
			self.contex = self.drama
		elif genre == 'Education':
			self.path = 'Library/education.json'
			self.contex = self.education

		trigger = True
		for content in self.contex:
			for key, value in content.items():
				if self.title == key and value['status'] == 'available':
					self.show_checked()
					trigger = False
					break
				elif self.title == key and value['status'] == 'rented':
					self.show_rented()
					trigger = False
					break
				else:
					self.show_unable()
					break
			if trigger == False:
				break

		print('ok')

	def haha(self):
		pass

	def rented(self):
		confirmation = messagebox.askquestion("Rental confirmation", "If you rent this book, make sure it returned in good situation.\n Are you sure with your rentalment?")

		if confirmation == "yes":
			self.rentaling()
			finish = messagebox.showinfo("Completion", "Book Rentaled")


	def returned(self):
		confirmation = messagebox.askquestion("Returning confirmation", "If you return this book, other can rent this book.\n Are you sure with your returnment?")

		if confirmation == "yes":
			self.rentaling()
			finish = messagebox.showinfo("Completion", "Book Returned")

	def show_checked(self):
		self.Rental_canvas.itemconfigure(self.status, fill="springgreen1")
		self.button_Rental.configure(text='Rent', command=self.rented)

	def show_rented(self):
		self.Rental_canvas.itemconfigure(self.status, fill='firebrick1')
		self.button_Rental.configure(text='Return', command=self.returned)

	def show_unable(self):
		self.Rental_canvas.itemconfigure(self.status, fill="blue")
		self.button_Rental.configure(text='No Book', command=self.haha)

	def rentaling(self):
		counter = 0
		for content in self.contex:
			for key, value in content.items():
				if self.title == key:
					if value['status'] == 'available':
						value['status'] = 'rented'
					elif value['status'] == 'rented':
						value['status'] = 'available'
				
		with open(self.path, "w") as file_json:
			dump(self.contex, file_json)

		self.settings.load_data()

	def clear_entry_and_return(self):
		self.entryTitle.delete(0, len(self.Title_var.get()))
		self.genreCombobox.delete(0, len(self.genreCombobox.get()))
		self.Rental_canvas.itemconfigure(self.status, fill="black")
		self.engine.return_to_menu()

	def clear_entry(self):
		self.entryTitle.delete(0, len(self.Title_var.get()))
		self.genreCombobox.delete(0, len(self.genreCombobox.get()))
		self.Rental_canvas.itemconfigure(self.status, fill="black")