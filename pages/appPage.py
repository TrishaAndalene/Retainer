import tkinter as tk
from PIL import Image, ImageTk


class AppPage(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings
		self.current_contact = self.settings.contacts[0]

		super().__init__(parent) # window.conteiner
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_left_frame()
		self.create_right_frame()
		self.config_left_right_frame()



	def create_left_frame(self):
		self.left_frame = tk.Frame(self, bg="pink")
		self.left_frame.grid(row=0, column=0, sticky="nsew")
		self.create_left_header()
		self.create_left_content()

	def create_right_frame(self):
		self.right_frame = tk.Frame(self, bg="white", width=2*self.settings.width//3)
		self.right_frame.grid(row=0, column=1, sticky="nsew")
		self.create_right_header()
		self.create_right_content()
		self.create_right_footer()

	def config_left_right_frame(self):
		self.grid_columnconfigure(0, weight=1) # 1/3
		self.grid_columnconfigure(1, weight=2) # 2/3
		self.grid_rowconfigure(0, weight=1)

	def create_left_header(self):
		frame_w = self.settings.width//3
		frame_h = self.settings.height//5
		self.left_header = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="white")
		self.left_header.pack()

		image = Image.open(self.settings.logo)
		i_w, i_h = image.size
		ratio = i_w/frame_w
		new_size = (int(i_w/ratio),int(i_h/ratio)) #(x,y)
		image = image.resize(new_size)
		self.logo = ImageTk.PhotoImage(image)

		self.label_logo = tk.Label(self.left_header, image=self.logo)
		self.label_logo.pack()

		self.searchbox_frame = tk.Frame(self.left_header, bg="white", width=frame_w, height=frame_h//4)
		self.searchbox_frame.pack(fill="x")

		self.entry_search = tk.Entry(self.searchbox_frame, bg="white", fg="black", font=("Arial", 14))
		self.entry_search.grid(row=0, column=0)

		self.button_search = tk.Button(self.searchbox_frame, bg="white", fg="black", font=("Arial", 14), text="Find")
		self.button_search.grid(row=0, column=1)

		self.searchbox_frame.grid_columnconfigure(0, weight=3) # 3/4
		self.searchbox_frame.grid_columnconfigure(1, weight=1) # 1/4


	def create_left_content(self):
		frame_w = self.settings.width//3
		frame_h = 4*self.settings.height//5

		self.left_content = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="white")
		self.left_content.pack(fill="x")

		self.contact_listBox = tk.Listbox(self.left_content, bg="white", fg="black", font=("Arial", 12), height=frame_h)
		self.contact_listBox.pack(side="left", fill="both", expand=True)

		self.contacts_scroll = tk.Scrollbar(self.left_content)
		self.contacts_scroll.pack(side="right", fill="y")

		contacts = self.settings.contacts
		for contact in contacts:
			for key, value in contact.items():
				full_name = f"{value['f_name']} {value['l_name']}"
				self.contact_listBox.insert("end", full_name)

		self.contact_listBox.configure(yscrollcommand=self.contacts_scroll.set)
		self.contacts_scroll.configure(command=self.contact_listBox.yview)

		self.contact_listBox.bind("<<ListboxSelect>>", self.clicked_item_in_Listbox)

	def clicked_item_in_Listbox(self, event):
		selection = event.widget.curselection()
		index = selection[0]

		#value = event.widget.get(index)
		#print(event.widget.curselection()[0])
		contact = self.settings.contacts[index]
		self.current_contact = contact
		
		for phoneNumber, info in contact.items():
			phone = phoneNumber
			full_name = info['f_name']+" "+info['l_name']
			address = info['address']
			email = info['email']

		self.full_name_label.configure(text=full_name)
		self.table_info[0][1].configure(text=phone)
		self.table_info[1][1]. configure(text=address)
		self.table_info[2][1]. configure(text=email)




	def create_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5

		self.right_header = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_header.pack()

		self.detail_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg="white")
		self.detail_header.grid(row=0, column=0, sticky="nsew")

		data = list(self.current_contact.values())[0]
		full_name = f"{data['f_name']} {data['l_name']}"

		self.virt_img = tk.PhotoImage(width=1, height=1)
		self.full_name_label = tk.Label(self.detail_header, text=full_name, font=("Arial", 30), width=frame_w, height=frame_h, image=self.virt_img, compound="c", bg="white")
		self.full_name_label.pack()

		self.right_header.grid_columnconfigure(0, weight=1)
		self.right_header.grid_rowconfigure(0, weight=1)

	def create_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.right_content = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_content.pack(expand=True)

		self.update_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="white")
		self.update_content.grid(row=0, column=0, sticky="nsew")

		self.detail_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="white")
		self.detail_content.grid(row=0, column=0, sticky="nsew")

		for phoneNumber, info in self.current_contact.items():	
			info = [
				['Telepon :', phoneNumber],
				['Alamat :', info['address']],
				['Email :', info["email"]]
			]

		self.table_info = []

		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				label = tk.Label(self.detail_content, text=info[row][column], font=("Arial", 12), bg="white")
				aRow.append(label)
				if column == 0:
					sticky = "e"
				else:
					sticky = "w"
				label.grid(row=row, column=column, sticky=sticky)
			self.table_info.append(aRow)

		for row in range(rows):
			aRow = []
			for column in range(columns):
				aRow.append(label)
				if column == 0:
					label = tk.Label(self.update_content, text=info[row][column], font=("Arial", 12), bg="white")
					sticky = "e"
					label.grid(row=row, column=column, sticky=sticky)
				else:
					entry = tk.Entry(self.update_content, text=info[row][column], bg="white")
					sticky = "w"
					entry.grid(row=row, column=column, sticky=sticky)
			self.table_info.append(aRow)



		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)


	def create_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_footer.pack()

		self.update_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="white")
		self.update_footer.grid(row=0, column=0, sticky="nsew")

		self.detail_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="white")
		self.detail_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Update', 'Delete', 'Add New']
		update_features = ['Save', 'Cancel']
		commands = [self.clicked_update_button, self.clicked_delete_button, self.clicked_add_new_button]
		self.buttons_features = []
		self.buttons_update_features = []

		for feature in features:
			button = tk.Button(self.detail_footer, text=feature, bg="white", fg="black", font=("Arial", 12, "bold"), bd=0, command=commands[features.index(feature)])
			button.grid(row=0, column=features.index(feature), sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_features.append(button)

		for feature in update_features:
			button = tk.Button(self.update_footer, text=feature, bg="white", fg="black", font=("Arial", 12, "bold"), bd=0)
			button.grid(row=0, column=update_features.index(feature), sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_update_features.append(button)

		self.buttons_update_features[0].configure(command=self.raise_detail)

		self.right_footer.grid_columnconfigure(0, weight=1)
		self.right_footer.grid_rowconfigure(0, weight=1)

	def clicked_update_button(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.detail_update_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="white")
		self.detail_update_content.grid(row=0, column=0, sticky="nsew")

		self.update_footer.tkraise()

		for phoneNumber, info in self.current_contact.items():	
			info = [
				['Nama Depan :', info['f_name']],
				['Nama Belakang :', info['l_name']],
				['Telepon :', phoneNumber],
				['Alamat :', info['address']],
				['Email :', info["email"]]
			]

		self.table_info = []

		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				if column == 0:
					label = tk.Label(self.detail_update_content, text=info[row][column], font=("Arial", 12), bg="white")
					aRow.append(label)
					sticky = "e"
					label.grid(row=row, column=column, sticky=sticky)
				else:
					entry = tk.Entry(self.detail_update_content, font=("Arial", 12), bg="white")
					entry.insert(0, info[row][column])
					aRow.append(entry)
					sticky = "w"
					entry.grid(row=row, column=column, sticky=sticky)
				
			self.table_info.append(aRow)

		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)

	def clicked_delete_button(self):
		print("del works")

	def clicked_add_new_button(self):
		print("add works")

	def raise_update(self):
		self.update_content.tkraise()
		self.update_footer.tkraise()

	def raise_detail(self):
		self.detail_content.tkraise()
		self.detail_footer.tkraise()

'''
	def create_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_footer.pack()

		self.update_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="white")
		self.update_footer.grid(row=0, column=0, sticky="nsew")

		self.detail_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="white")
		self.detail_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Update', 'Delete', 'Add New']
		update_features = ['Save', 'Cancel']

		self.buttons_features = []
		self.buttons_update_features = []

		for feature in features:
			button = tk.Button(self.detail_footer, text=feature, bg="white", fg="black", font=("Arial", 12, "bold"), bd=0)
			button.grid(row=0, column=features.index(feature), sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_features.append(button)

		self.buttons_features[0].configure(command=self.raise_update)

		for feature in update_features:
			button = tk.Button(self.update_footer, text=feature, bg="white", fg="black", font=("Arial", 12, "bold"), bd=0)
			button.grid(row=0, column=update_features.index(feature), sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_update_features.append(button)

		self.buttons_update_features[0].configure(command=self.raise_detail)

		self.right_footer.grid_columnconfigure(0, weight=1)
		self.right_footer.grid_rowconfigure(0, weight=1)

	def raise_update(self):
		self.update_content.tkraise()
		self.update_footer.tkraise()

	def raise_detail(self):
		self.detail_content.tkraise()
		self.detail_footer.tkraise()
'''

