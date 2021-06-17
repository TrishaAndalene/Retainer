#----Import module----
from json import load, dump

#----Settings configuration---
class Settings:

	def __init__(self):

		#---Title-----
		self.title = "9th Last Semester [Library]"

		#---Geometry---
		base = 60
		self.width = 16*base
		self.height = int(8.5*base)
		self.screen = f"{self.width}x{self.height}+500+500"

		self.login_width = int(6*base)
		self.login_height = 8*base
		self.login_screen = f"{self.login_width}x{self.login_height}"

		#---Login attribute---
		self.username = 'Asura'
		self.password = 'Gate'

		#---Image path---
		self.window_icon = 'image/blue_sample_try.ico'
		self.menu_background = "image/front_menu.png"
		self.view_background = "image/view_background.png"
		self.view_book_background = 'image/Buku(4).png'
		self.add_background = 'image/add_background.png'
		self.delete_background = 'image/add_background.png'
		self.login_background = 'image/login_latar.jpg'
		self.no_sound = 'image/no_sound_bg.png'
		self.sound = 'image/audio_bg.png'
		self.logo = 'image/orange_sample.jpg'
		self.notif = 'image/notif_final.png'

		#---Atributte needed---
		self.update_available = 0
		self.horrors = None
		self.fantasies = None
		self.comedies = None
		self.actions = None
		self.romances = None
		self.sci_fis = None
		self.dramas = None
		self.educations = None

		self.load_data()
		self.load_account()

	def load_account(self):
		with open("Library/account.json", "r") as file_json:
			self.username = load(file_json)

	def load_data(self):
		with open("Library/horrors.json", "r") as file_json:
			self.horrors = load(file_json)

		with open("Library/fantasy.json", "r") as file_json:
			self.fantasies = load(file_json)

		with open("Library/comedy.json", "r") as file_json:
			self.comedies = load(file_json)

		with open("Library/action.json", "r") as file_json:
			self.actions = load(file_json)

		with open("Library/romance.json", "r") as file_json:
			self.romances = load(file_json)

		with open("Library/sci-fi.json", "r") as file_json:
			self.sci_fis = load(file_json)

		with open("Library/drama.json", "r") as file_json:
			self.dramas = load(file_json)

		with open("Library/education.json", "r") as file_json:
			self.educations = load(file_json)