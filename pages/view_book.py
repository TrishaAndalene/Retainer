#----Import system----
import tkinter as tk
from PIL import Image, ImageTk

#----View Page [categories]----
class Categories(tk.Frame):

	def __init__(self, parent, Engine):
		self.engine = Engine
		self.settings = Engine.settings

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

		self.create_categories_frame()

	def create_categories_frame(self):
		self.categories_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.categories_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

		self.create_background()
		self.create_title()
		self.create_categories()
		self.create_button()

	def create_background(self):
		image = Image.open(self.settings.view_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.view_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.view_canvas = tk.Canvas(self.categories_frame, width=960, height=510)
		self.view_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.view_canvas.create_image(0, 0, image=self.view_background, anchor="nw")

	def create_title(self):
		self.view_canvas.create_text(500, 80, text='Categories', font=("Times", 60), fill="snow")

	def create_categories(self):
		self.view_canvas.create_text(225, 280, text='H\nO\nR\nR\nO\nR', font=("Times", 20), fill="snow")
		self.view_canvas.create_text(305, 270, text='R\nO\nM\nA\nN\nC\nE', font=("Times", 20), fill="snow")
		self.view_canvas.create_text(385, 280, text='S\nC\nI\n-\nF\nI', font=("Times", 20), fill="snow")
		self.view_canvas.create_text(465, 270, text='F\nA\nN\nT\nA\nS\nY', font=("Times", 20), fill="snow")
		self.view_canvas.create_text(545, 280, text='A\nC\nT\nI\nO\nN', font=("Times", 20), fill="snow")
		self.view_canvas.create_text(625, 280, text='C\nO\nM\nE\nD\nY', font=("Times", 20), fill="snow")
		self.view_canvas.create_text(705, 270, text='E\nD\nU\nC\nA\nT\nI\nO\nN', font=("Times", 16), fill="snow")
		self.view_canvas.create_text(785, 290, text='D\nR\nA\nM\nA', font=("Times", 20), fill="snow")

	def create_button(self):
		passable = ""
		horror = "horror"

		self.button_1 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="horror":self.engine.change_to_view_book(genre))
		self.button_2 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="romance":self.engine.change_to_view_book(genre))
		self.button_3 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="sci-fi":self.engine.change_to_view_book(genre))
		self.button_4 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="fantasy":self.engine.change_to_view_book(genre))
		self.button_5 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="action":self.engine.change_to_view_book(genre))
		self.button_6 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="comedy":self.engine.change_to_view_book(genre))
		self.button_7 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="education":self.engine.change_to_view_book(genre))
		self.button_8 = tk.Button(self.categories_frame, text="   ", font=('Times', 13), fg='white', bg='#964d2d', command=lambda genre="drama":self.engine.change_to_view_book(genre))

		self.button_1_window = self.view_canvas.create_window(225, 410, window=self.button_1)
		self.button_2_window = self.view_canvas.create_window(305, 410, window=self.button_2)
		self.button_3_window = self.view_canvas.create_window(385, 410, window=self.button_3)
		self.button_4_window = self.view_canvas.create_window(465, 410, window=self.button_4)
		self.button_5_window = self.view_canvas.create_window(545, 410, window=self.button_5)
		self.button_6_window = self.view_canvas.create_window(625, 410, window=self.button_6)
		self.button_7_window = self.view_canvas.create_window(705, 410, window=self.button_7)
		self.button_8_window = self.view_canvas.create_window(785, 410, window=self.button_8)

		self.back_button = tk.Button(self.categories_frame, text='<- Return', font=('Times', 18), fg='snow', bg='sienna1', command=self.engine.return_to_menu)
		self.back_button_window = self.view_canvas.create_window(50, 490, window=self.back_button)