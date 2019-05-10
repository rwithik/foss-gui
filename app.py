import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class passwdWindow(Gtk.Window):
	"""docstring for passwdWindow"""
	def __init__(self):
		Gtk.Window.__init__(self, title="Master Password")
		self.set_default_size(400, 200)
		grid = Gtk.Grid()
		grid.set_row_spacing(10)
		self.add(grid)

		input_box = Gtk.Entry()
		input_box.set_text("Password")
		grid.attach(input_box, 0, 0, 1, 1)
		
		download_button = Gtk.Button(label="Download")
		# download_button.connect("clicked", start_download)
		download_button.connect("clicked", self.verify, input_box)
		grid.attach_next_to(download_button, input_box, Gtk.PositionType.BOTTOM, 1, 2)

	def verify(self, button, input_box):
		input = input_box.get_text()
		print(input)
		if(input == "12345"):
			print("logged in")
		else:
			print("nope")

win = passwdWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
