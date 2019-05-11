import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import pickle
from windowClass import MainWindow


def verify(button):
	input = input_box.get_text()
	print(input)
	# if(input == "12345"):
	if(True):
		master_passwd_window.hide()
		main_win = MainWindow()
		main_win.connect("destroy", Gtk.main_quit)
		main_win.set_default_size(500, 600)
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
input_box.set_placeholder_text("Password")
input_box.set_visibility(False)
grid.attach(input_box, 1, 0, 1, 1)

password_label = Gtk.Label(label="Master Password")
grid.attach(password_label, 0, 0, 1, 1)

download_button = Gtk.Button(label="Submit")
download_button.connect("clicked", verify)
grid.attach_next_to(download_button, input_box, Gtk.PositionType.BOTTOM, 1, 2)

master_passwd_window.add(grid)
master_passwd_window.show_all()
Gtk.main()

