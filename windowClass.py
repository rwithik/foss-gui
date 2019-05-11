import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Notify', '0.7')
from gi.repository import Notify

import pickle
import os

class MainWindow(Gtk.Window):

	def __init__(self):
		self.file_empty_flag = False
		self.entries = {}
		self.__i = 0

		Notify.init("Password Manager")
		Gtk.Window.__init__(self, title="Password Manager")

		self.__grid = self.get_grid()
		self.add(self.__grid)
	


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
		self.file_empty_flag = False

		if (website in self.entries.keys()):
			self.entries[website][username] = password
		else:
			self.entries[website] = {username: password}

		try:
			self.__dump_to_file(self.entries, "entries")
			self.send_notification("New Entry Successfully Added! :)")
			self.__redraw()
		except Exception as e:
			self.send_notification("An Error Occured! New Entry was not Added! :(")
			print(e)



	def send_notification(self, title):

		n = Notify.Notification.new(title)
		n.show()		



	def on_copy_clicked(self, button, website, username, passwd):
		os.system("echo \"" + passwd +  "\" | xclip -sel clip")
		self.send_notification("Password for " + website + ":" + username + " copied to clipboard! :)")



	def delete_clicked(self, button, website, username):
		try:
			del self.entries[website][username]
			if(len(self.entries[website]) == 0):
				del self.entries[website]

			self.__dump_to_file(self.entries, "entries")
			self.send_notification("Deleted " + website + ":" + username + " from the list!")
			self.__redraw()

		except KeyError as e:
			self.send_notification("An Error Occured! Could not Remove Entry :(")
			print(e)



	def __dump_to_file(self, dict, file):
		with open(file, "wb") as f:
			pickle.dump(dict, f)



	def __redraw(self):
		self.remove(self.__grid)

		self.__grid = self.get_grid()
		self.add(self.__grid)

		self.__grid.show()
		self.show_all()



	def get_grid(self):
		grid = Gtk.Grid()
		grid.set_row_spacing(10)
		grid.set_column_spacing(10)
		grid.set_column_homogeneous(True)
		grid.set_hexpand(True)
		grid.set_vexpand(True)


		add_new_label = Gtk.Label(label = "Add or Update an Entry: ")
		grid.attach(add_new_label, 0, 0, 1, 2)

		add_new_ws_input = Gtk.Entry()
		add_new_ws_input.set_placeholder_text("Service")
		grid.attach(add_new_ws_input, 1, 0, 2, 1)


		add_new_un_input = Gtk.Entry()
		add_new_un_input.set_placeholder_text("Username")
		grid.attach(add_new_un_input, 1, 1, 1, 1)

		add_new_pw_input = Gtk.Entry()
		add_new_pw_input.set_placeholder_text("Password")
		add_new_pw_input.set_visibility(False)
		grid.attach(add_new_pw_input, 2, 1, 1, 1)

		add_new_button = Gtk.Button(label="Add")
		add_new_button.connect("clicked", self.add_new_entry, add_new_ws_input, add_new_un_input, add_new_pw_input)
		grid.attach(add_new_button, 1, 2, 1, 1)


		try:
			with open("entries", "rb") as f:
				self.entries = pickle.load(f)

			if len(self.entries) == 0:
				self.file_empty_flag = True

		except:
			self.file_empty_flag = True
			no_entries_label = Gtk.Label("Add a New Entry to get started!")
			grid.attach(no_entries_label, 0, 4, 1, 1)

		if (not self.file_empty_flag):
			for website, dict in self.entries.items():

				entry_label = Gtk.Label(label=website)
				grid.attach(entry_label, 0, self.__i + 4, 1, len(dict))

				self.__j = self.__i + 4

				for user, passwd in dict.items():
	
					username_label = Gtk.Label(label=user)
					grid.attach(username_label, 1, self.__j, 1, 1)

					copy_button = Gtk.Button(label="Copy")
					copy_button.connect("clicked", self.on_copy_clicked, website, user, passwd)
					grid.attach_next_to(copy_button, username_label, Gtk.PositionType.RIGHT, 1, 1)
	
					delete_button = Gtk.Button(label="Delete")
					delete_button.connect("clicked", self.delete_clicked, website, user)
					grid.attach_next_to(delete_button, copy_button, Gtk.PositionType.RIGHT, 1, 1)
					
					self.__j += 1
	
				hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
				grid.attach_next_to(hseparator, entry_label, Gtk.PositionType.BOTTOM, 3, 1)

				self.__i += 2
		return grid