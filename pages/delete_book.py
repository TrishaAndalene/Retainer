#----Import system----
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from json import dump, load

#----Add Page [book index]----
class Delete(tk.Frame):

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
		self.delete_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.delete_canvas = tk.Canvas(self.base_frame, width=960, height=510)
		self.delete_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.delete_canvas.create_image(0, 0, image=self.delete_background, anchor="nw")

	def create_back_button(self):
		self.button_back = tk.Button(self.base_frame, text='   X   ', bg='red', fg='snow', font=("Arial", 12), command=self.clear_entry_and_return)
		self.button_back_window = self.delete_canvas.create_window(910, 5, anchor="nw", window=self.button_back)

	def create_genre_box(self):
		self.style = ttk.Style()
		#self.style.theme_create('combostyle', parent='alt', settings = {'TCombobox':{'configure':{'foreground' : 'white','fieldbackground': 'black','background': 'black'},'selectbackground': 'black'}}) #'selectbackground': 'white'
		self.style.theme_use('combostyle')

		self.Genre_Var = tk.StringVar()
		self.genreCombobox = ttk.Combobox(self.base_frame, textvariable=self.Genre_Var, font=('Times', 15), width=30)
		self.genreCombobox["values"] = ['Horror', 'Romance', 'Sci-Fi', 'Fantasy', 'Action', 'Comedy', 'Education', 'Drama']
		self.genreComboboxWindow = self.delete_canvas.create_window(70, 180, anchor="nw", window=self.genreCombobox)

	def create_labels(self):
		self.delete_canvas.create_text(280, 40, text='Delete A Book', font=("Times", 45), fill="goldenrod")
		self.delete_canvas.create_text(90, 120, text='Title', font=("Times", 20), fill="goldenrod")
		'''
		self.delete_canvas.create_text(95, 190, text='Note:', font=("Times", 20), fill="red")
		self.delete_canvas.create_text(242, 220, text='Deleted book would not be able', font=("Times", 20), fill="red")
		self.delete_canvas.create_text(138, 250, text='to be undone', font=("Times", 20), fill="red")
		'''

		self.delete_canvas.create_text(110, 240, text='Status :', font=("Times", 20), fill="goldenrod")
		self.status = self.delete_canvas.create_text(180, 240, text='|||||||||||', font=("Times", 20), fill="black")

	def create_entries(self):
		self.Title_var = tk.StringVar()
		self.entryTitle = tk.Entry(self.base_frame, textvariable=self.Title_var, width=32, font=("Times", 15), bg="black", fg="white")
		self.entryTitleWindow = self.delete_canvas.create_window(70, 140, anchor="nw", window=self.entryTitle)

	def confirm_deleting(self):
		confirmation = messagebox.askquestion("Deleting confirmation", "Once the book is deleted, it can't be undone.\n Are you sure with your change?")
		
		print(confirmation)

		if confirmation == "yes":
			self.deleting()
			finish = messagebox.showinfo("Completion", "Deleting Complete")
			self.clear_entry()

	def create_buttons(self):
		self.button_check = tk.Button(self.base_frame, text='Check', font=("Times", 10), bg='goldenrod', fg='black', command=self.check_function)
		self.button_check_window = self.delete_canvas.create_window(400, 180, anchor='nw', window=self.button_check)

		self.button_delete = tk.Button(self.base_frame, text='Delete', font=("Times", 15), bg='goldenrod', fg='black', command=self.confirm_deleting)
		self.button_delete_window = self.delete_canvas.create_window(65, 390, anchor='nw', window=self.button_delete)

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
				if self.title == key:
					self.show_checked()
					trigger = False
				else:
					self.show_unable()
			if trigger == False:
				break

	def show_checked(self):
		self.delete_canvas.itemconfigure(self.status, fill="springgreen1")

	def show_unable(self):
		self.delete_canvas.itemconfigure(self.status, fill="firebrick1")

	def deleting(self):
		counter = 0
		for content in self.contex:
			for key, value in content.items():
				if self.title == key:
					#self.contex.remove(self.content)
					del self.contex[counter]
				counter += 1
				
		with open(self.path, "w") as file_json:
			dump(self.contex, file_json)

		self.settings.load_data()

	def clear_entry_and_return(self):
		self.entryTitle.delete(0, len(self.Title_var.get()))
		self.genreCombobox.delete(0, len(self.genreCombobox.get()))
		self.delete_canvas.itemconfigure(self.status, fill="black")
		self.engine.return_to_menu()

	def clear_entry(self):
		self.entryTitle.delete(0, len(self.Title_var.get()))
		self.genreCombobox.delete(0, len(self.genreCombobox.get()))
		self.delete_canvas.itemconfigure(self.status, fill="black")