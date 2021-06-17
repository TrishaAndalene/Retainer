#----Import system----
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from json import dump, load

#----Add Page [book index]----
class Add(tk.Frame):

	def __init__(self, parent, Engine):
		self.engine = Engine
		self.settings = Engine.settings

		self.counter = 1

		#---Path---
		self.horror = self.settings.horrors
		self.comedy = self.settings.comedies
		self.fantasy = self.settings.fantasies
		self.action = self.settings.actions
		self.romance = self.settings.romances
		self.sci_fi = self.settings.sci_fis
		self.education = self.settings.educations
		self.drama = self.settings.dramas

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
		self.create_button()

	def create_background(self):
		image = Image.open(self.settings.add_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.add_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.add_canvas = tk.Canvas(self.base_frame, width=960, height=510)
		self.add_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.add_canvas.create_image(0, 0, image=self.add_background, anchor="nw")

	def create_back_button(self):
		self.button_back = tk.Button(self.base_frame, text='   X   ', bg='red', fg='snow', font=("Arial", 12), command=self.clear_entry_and_return)
		self.button_back_window = self.add_canvas.create_window(910, 5, anchor="nw", window=self.button_back)

	def create_genre_box(self):
		self.style = ttk.Style()
		#self.style.theme_create('combostyle', parent='alt', settings = {'TCombobox':{'configure':{'foreground' : 'white','fieldbackground': 'black','background': 'black'},'selectbackground': 'black'}}) #'selectbackground': 'white'
		self.style.theme_use('combostyle')

		self.variable = tk.StringVar()
		self.genreCombobox = ttk.Combobox(self.base_frame, textvariable=self.variable, font=('Times', 15), width=30)
		self.genreCombobox["values"] = ['Horror', 'Romance', 'Sci-Fi', 'Fantasy', 'Action', 'Comedy', 'Education', 'Drama']
		self.genreComboboxWindow = self.add_canvas.create_window(70, 400, anchor="nw", window=self.genreCombobox)

	def create_labels(self):
		self.add_canvas.create_text(280, 40, text='New Book', font=("Times", 45), fill="goldenrod")
		self.add_canvas.create_text(90, 100, text='Title', font=("Times", 20), fill="goldenrod")

		#self.add_canvas.create_text(130, 190, text='Category', font=("Times", 25), fill="goldenrod")

		self.add_canvas.create_text(160, 170, text='Publication Year', font=("Times", 20), fill="goldenrod")
		self.add_canvas.create_text(122, 240, text='Publisher', font=("Times", 20), fill="goldenrod")
		self.add_canvas.create_text(109, 310, text='Author', font=("Times", 20), fill='goldenrod')
		self.add_canvas.create_text(100, 380, text='Genre', font=("Times", 20), fill='goldenrod')

	def create_entries(self):
		self.Title_var = tk.StringVar()
		self.entryTitle = tk.Entry(self.base_frame, textvariable=self.Title_var, width=32, font=("Times", 15), bg="black", fg="white")
		self.entryTitleWindow = self.add_canvas.create_window(70, 120, anchor="nw", window=self.entryTitle)

		#self.textTitle = tk.Text(self.base_frame, width=30, height=1, font=("Times", 20), bg="black", fg="goldenrod")
		#self.textTitleWindow = self.add_canvas.create_window(70, 120, anchor="nw", window=self.textTitle)
	
		self.Year_var = tk.StringVar()
		self.entryYear = tk.Entry(self.base_frame, textvariable=self.Year_var, width=32, font=("Times", 15), bg="black", fg="white")
		self.entryYearWindow = self.add_canvas.create_window(70, 190, anchor="nw", window=self.entryYear)

		self.Publish_var = tk.StringVar()
		self.entryPublish = tk.Entry(self.base_frame, textvariable=self.Publish_var, width=32, font=("Times", 15), bg="black", fg="white")
		self.entryPublishWindow = self.add_canvas.create_window(70, 260, anchor="nw", window=self.entryPublish)

		self.Author_var = tk.StringVar()
		self.entryAuthor = tk.Entry(self.base_frame, textvariable=self.Author_var, width=32, font=("Times", 15), bg="black", fg="white")
		self.entryAuthorWindow = self.add_canvas.create_window(70, 330, anchor="nw", window=self.entryAuthor)

	def confirm_saving(self):
		confirmation = messagebox.askquestion("Saving confirmation", "Once the book is saved, it can't be change again.\n Are you sure with your change?")
		print(confirmation)

		if confirmation == "yes":
			self.saving()
			finish = messagebox.showinfo("Completion", "Saving Complete")
			self.clear_entry()
			self.settings.update_available = 1

	def create_button(self):
		self.button_save = tk.Button(self.base_frame, text='Save', font=("Times", 15), bg='goldenrod', fg='black', command=self.confirm_saving)
		self.button_save_window = self.add_canvas.create_window(440, 390, anchor='nw', window=self.button_save)

	def saving(self):
		genre = self.genreCombobox.get()
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

		title = self.Title_var.get()
		year = self.Year_var.get()
		publish = self.Publish_var.get()
		author = self.Author_var.get() 

		self.content = {
			title : {
				"tahun" : year,
				"penerbit" : publish,
				"pencipta" : author,
				"status" : 'available'
				}
		}
		self.contex.append(self.content)
		self.sorting()

		with open(self.path, "w") as file_json:
			dump(self.contex, file_json)

	def clear_entry(self):
		self.entryTitle.delete(0, len(self.Title_var.get()))
		self.entryYear.delete(0, len(self.Year_var.get()))
		self.entryPublish.delete(0, len(self.Publish_var.get()))
		self.entryAuthor.delete(0, len(self.Author_var.get()))
		self.genreCombobox.delete(0, len(self.genreCombobox.get()))

	def clear_entry_and_return(self):
		self.entryTitle.delete(0, len(self.Title_var.get()))
		self.entryYear.delete(0, len(self.Year_var.get()))
		self.entryPublish.delete(0, len(self.Publish_var.get()))
		self.entryAuthor.delete(0, len(self.Author_var.get()))
		self.genreCombobox.delete(0, len(self.genreCombobox.get()))
		self.engine.return_to_menu()

	def sorting(self):
		temps = []
		contemp = []
		for content in self.contex:
			for key, value in content.items():
				temps.append(key)
		temps.sort()
		print(temps)

		a = len(self.contex)
		for i in range(a):
			counter = 0
			cont = 0
			for content in self.contex:
				for key, value in content.items():
					if temps[i] == key:
						contemp.append(self.contex[cont])
					cont += 1

		self.contex = contemp
