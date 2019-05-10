import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import pickle


class MainWindow(Gtk.Window):
	"""docstring for MainWindow"""
	def __init__(self):
		Gtk.Window.__init__(self, title="Password Manager")
		with open("entries", "rb") as f:
			self.entries = pickle.load(f)

		grid = Gtk.Grid()
		grid.set_row_spacing(10)
		grid.set_column_homogeneous(True)

		add_new_label = Gtk.Label(label = "Add or Update an Entry: ")
		grid.attach(add_new_label, 0, 0, 1, 2)

		add_new_ws_input = Gtk.Entry()
		add_new_ws_input.set_text("Website")
		grid.attach(add_new_ws_input, 1, 0, 2, 1)


		add_new_un_input = Gtk.Entry()
		add_new_un_input.set_text("Username")
		grid.attach(add_new_un_input, 1, 1, 1, 1)

		add_new_pw_input = Gtk.Entry()
		add_new_pw_input.set_text("Password")
		grid.attach(add_new_pw_input, 2, 1, 1, 1)

		add_new_button = Gtk.Button(label="Add")
		add_new_button.connect("clicked", self.add_new_entry, add_new_ws_input, add_new_un_input, add_new_pw_input)
		grid.attach(add_new_button, 1, 3, 1, 1)

		i = 0
		for website, dict in self.entries.items():
			entry_label = Gtk.Label(label=website)
			grid.attach(entry_label, 0, i+4, 1, len(dict))
			j = i + 4

			for user, passwd in dict.items():

				username_label = Gtk.Label(label=user)
				grid.attach(username_label, 1, j, 1, 1)

				copy_button = Gtk.Button(label="Copy")
				copy_button.connect("clicked", self.on_copy_clicked, passwd)
				grid.attach_next_to(copy_button, username_label, Gtk.PositionType.RIGHT, 1, 1)

				j += 1

			i += 1

		self.add(grid)


	def add_new_entry(self, button, wb_input, un_input, pw_input):
		# {
		# website: {
		# 			username: password, 
		# 			username: password, 
		# 			...
		# 		}, 
		# website: {
		# 			username: password, 
		# 			username: password
		# 			...
		# 		}, 
		#	...
		# }
		website = wb_input.get_text()
		username = un_input.get_text()
		password = pw_input.get_text()

		if (website in self.entries.keys()):
			self.entries[website][username] = password
		else:
			self.entries[website] = {username: password}
		print(self.entries)
		with open("entries", "wb") as f:
			pickle.dump(self.entries, f)
		

	def on_copy_clicked(self, button, passwd):
		print(passwd)



def verify(button):
	input = input_box.get_text()
	print(input)
	# if(input == "12345"):
	if(True):
		master_passwd_window.hide()
		main_win = MainWindow()
		main_win.connect("destroy", Gtk.main_quit)
		main_win.set_default_size(400, 500)
		main_win.set_border_width(30)
		main_win.show_all()
		print("logged in")
	else:
		print("nope")

master_passwd_window = Gtk.Window(title="Master Password")
master_passwd_window.connect("destroy", Gtk.main_quit)
master_passwd_window.set_default_size(400, 200)
master_passwd_window.set_border_width(30)

grid = Gtk.Grid()
grid.set_row_spacing(10)
grid.set_column_homogeneous(True)

input_box = Gtk.Entry()
input_box.set_text("Password")
grid.attach(input_box, 1, 0, 1, 1)

password_label = Gtk.Label(label="Master Password")
grid.attach(password_label, 0, 0, 1, 1)

download_button = Gtk.Button(label="Submit")
download_button.connect("clicked", verify)
grid.attach_next_to(download_button, input_box, Gtk.PositionType.BOTTOM, 1, 2)

master_passwd_window.add(grid)



master_passwd_window.show_all()
Gtk.main()
