import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def get_grid():
	file_empty_flag = True
	entries = {}

	grid = Gtk.Grid()
	grid.set_row_spacing(10)
	grid.set_column_homogeneous(True)
	grid.set_hexpand(True)
	grid.set_vexpand(True)

	add_new_label = Gtk.Label(label = "Add or Update an Entry: ")
	grid.attach(add_new_label, 0, 0, 1, 2)

	add_new_ws_input = Gtk.Entry()
	add_new_ws_input.set_placeholder_text("Website")
	grid.attach(add_new_ws_input, 1, 0, 2, 1)

	add_new_un_input = Gtk.Entry()
	add_new_un_input.set_placeholder_text("Username")
	grid.attach(add_new_un_input, 1, 1, 1, 1)

	add_new_pw_input = Gtk.Entry()
	add_new_pw_input.set_placeholder_text("Password")
	add_new_pw_input.set_visibility(False)
	grid.attach(add_new_pw_input, 2, 1, 1, 1)

	add_new_button = Gtk.Button(label="Add")
	add_new_button.connect("clicked", add_new_entry, add_new_ws_input, add_new_un_input, add_new_pw_input)
	grid.attach(add_new_button, 1, 3, 1, 1)

	try:
		with open("entries", "rb") as f:
			entries = pickle.load(f)
		if len(entries) == 0:
			file_empty_flag = True
	except:
		file_empty_flag = True
		no_entries_label = Gtk.Label("Add a New Entry to get started!")
		grid.attach(no_entries_label, 0, 4, 1, 1)

	if (not file_empty_flag):
		for website, dict in entries.items():
			entry_label = Gtk.Label(label=website)
			grid.attach(entry_label, 0, i + 4, 1, len(dict))
			j = i + 4


			for user, passwd in dict.items():

				username_label = Gtk.Label(label=user)
				grid.attach(username_label, 1, j, 1, 1)
				copy_button = Gtk.Button(label="Copy")
				copy_button.connect("clicked", on_copy_clicked, website, passwd)
				grid.attach_next_to(copy_button, username_label, Gtk.PositionType.RIGHT, 1, 1)

				delete_button = Gtk.Button(label="Delete")
				delete_button.connect("clicked", delete_clicked, website, user)
				grid.attach_next_to(delete_button, copy_button, Gtk.PositionType.RIGHT, 1, 1)
				
				j += 1

			hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
			grid.attach_next_to(hseparator, entry_label, Gtk.PositionType.BOTTOM, 3, 1)
			i += 2
	return grid