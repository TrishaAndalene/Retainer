#----Import system----
import tkinter as tk
from PIL import Image, ImageTk

#----View Page [categories]----
class BookDetail(tk.Frame):

	def __init__(self, parent, Engine):
		self.engine = Engine
		self.settings = Engine.settings
		self.contents = []
		self.contents_index = []

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

		self.left_frame = tk.Frame(self.main_frame, bg="white", width=self.settings.width//4)
		self.left_frame.grid(column=0, row=0, sticky='nsew')

		self.categories_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.categories_frame.grid(column=1, row=0, sticky='nesw')
		
		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_columnconfigure(1, weight=3)
		self.main_frame.grid_rowconfigure(0, weight=1)

		self.create_background()
		self.create_back_button()
		self.create_logo()
		self.create_search_box()
		self.create_list_box()
		#self.create_horror()

	def create_logo(self):
		frame_w = self.settings.width//7
		frame_h = self.settings.height//18

		image = Image.open(self.settings.logo)
		i_w, i_h = image.size
		ratio = i_w/frame_w
		new_size = (int(i_w/ratio),int(i_h/ratio)) #(x,y)
		image = image.resize(new_size)
		self.logo = ImageTk.PhotoImage(image)

		self.label_logo = tk.Label(self.left_frame, image=self.logo)
		self.label_logo.pack()

	def create_background(self):
		image = Image.open(self.settings.view_book_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.view_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.view_canvas = tk.Canvas(self.categories_frame, width=960, height=510)
		self.view_canvas.pack(fill="both")

		#---Insert Image to Canvas---
		self.view_canvas.create_image(0, 0, image=self.view_background, anchor="nw")

	def show_all_contents_in_listbox(self):
		self.listBox.delete(0, 'end')
		contents = self.contents
		self.contents_index = []
		index_counter = 0
		for content in contents:
			self.contents_index.append(index_counter)
			index_counter += 1	
		for index in self.contents_index:
			content = contents[index]
			for judul in content:
				self.listBox.insert("end", judul)

	def show_current_contents_index_in_listbox(self):
		self.listBox.delete(0, 'end')
		contents = self.contents
		for index in self.contents_index:
			content = contents[index]
			for judul in content:
				self.listBox.insert("end", judul)


	def create_search_box(self):
		self.search_data = tk.StringVar()
		self.entry_search = tk.Entry(self.left_frame, bg="white", fg="black", font=("Arial", 14), textvariable=self.search_data)
		self.entry_search.pack()

		self.entry_search.bind("<Key>", self.search_enter)

	def search_enter(self, event):
		item_search = self.search_data.get()
		books = self.contents
		self.contents_index = []
		index_counter = 0
		if item_search:
			for book in books:
				for judul, info in book.items():
					if item_search in judul:
						#print(phoneNumber)
						self.contents_index.append(index_counter)
					elif item_search in info['tahun']:
						#print(info['f_name'])
						self.contents_index.append(index_counter)
					elif item_search in info['penerbit']:
						#print(info['l_name'])
						self.contents_index.append(index_counter)
					elif item_search in info['pencipta']:
						#print(info['l_name'])
						self.contents_index.append(index_counter)
				index_counter += 1
			#print(self.contents_index)
			self.show_current_contents_index_in_listbox()
		else:
			self.show_all_contents_in_listbox()
		

	def create_list_box(self):
		self.listBox = tk.Listbox(self.left_frame, bg="white", fg="black", font=("Arial", 12))
		self.listBox.pack(fill="both", side="left", expand=True)

		self.scroll = tk.Scrollbar(self.left_frame)
		self.scroll.pack(fill="y", side="right")

		self.table_info = []
		self.title_book = self.view_canvas.create_text(400, 120, text='', font=('Times', 30, 'bold'), fill='black')
		self.year_book = self.view_canvas.create_text(390, 200, text="", font=('Helvetica', 16), fill='black')
		self.publish_book = self.view_canvas.create_text(390, 260, text="", font=('Helvetica', 16), fill='black')
		self.creator_book = self.view_canvas.create_text(390, 320, text="", font=('Helvetica', 16), fill='black')

	def create_contents(self, genre):
		if genre == 'horror':
			self.contents = self.settings.horrors
		elif genre == 'romance':
			self.contents = self.settings.romances
		elif genre == 'sci-fi':
			self.contents = self.settings.sci_fis
		elif genre == 'fantasy':
			self.contents = self.settings.fantasies
		elif genre == 'action':
			self.contents = self.settings.actions
		elif genre == 'drama':
			self.contents = self.settings.dramas
		elif genre == 'comedy':
			self.contents = self.settings.comedies
		elif genre == 'education':
			self.contents = self.settings.educations

		for content in self.contents:
			for key, value in content.items():
				judul = key
				#self.view_canvas.itemconfigure(self.title_book, text=judul)
				self.listBox.insert("end", judul)

		starter_value = self.contents[0]
		for key, value in starter_value.items():
			tahun_terbit = f"publication year : {value['tahun']}"
			terbitan = f"publisher : {value['penerbit']}"
			creator = f"creator : {value['pencipta']}"
			self.view_canvas.itemconfigure(self.title_book, text=key)
			self.view_canvas.itemconfigure(self.year_book, text=tahun_terbit)
			self.view_canvas.itemconfigure(self.publish_book, text=terbitan)
			self.view_canvas.itemconfigure(self.creator_book, text=creator)		

		self.listBox.configure(yscrollcommand=self.scroll.set)
		self.scroll.configure(command=self.listBox.yview)

		self.listBox.bind("<<ListboxSelect>>", self.clicked_item_in_Listbox)
		self.show_all_contents_in_listbox()

	def clicked_item_in_Listbox(self, event):
		selection = event.widget.curselection()

		#value = event.widget.get(index)
		#print(event.widget.curselection()[0])
		#item = self.contents[index]
		#print(item)
		try:
			index_listbox = selection[0]
		except IndexError:
			index_listbox = self.last_current_content_index
		index = self.contents_index[index_listbox]
		self.last_current_content_index = index
		content = self.contents[index]
		self.current_content = content
		
		for index, info in self.current_content.items():
			index = index
			tahun = info['tahun']
			penerbit = info['penerbit']
			pencipta = info['pencipta']

		tahun_terbit = f"publication year : {tahun}"
		terbitan = f"publisher : {penerbit}"
		creator = f"creator : {pencipta}"

		self.view_canvas.itemconfigure(self.title_book, text=index)
		self.view_canvas.itemconfigure(self.year_book, text=tahun_terbit)
		self.view_canvas.itemconfigure(self.publish_book, text=terbitan)
		self.view_canvas.itemconfigure(self.creator_book, text=creator)

	def create_back_button(self):
		self.button_back = tk.Button(self.categories_frame, text='   X   ', bg='red', fg='snow', font=("Arial", 12), command=self.engine.change_to_view)
		self.button_back_window = self.view_canvas.create_window(690, 2, anchor="nw", window=self.button_back)