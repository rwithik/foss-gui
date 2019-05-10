#!/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# class mainWindow(Gtk.Window):
# 	"""docstring for mainWindow"""
# 	def __init__(self, title):
# 		super(self).__init__()
# 		self.title = title
		

def on_close():
	Gtk.main_quit()

def verify_master_password(input):
	if input.get_text() == "12345":
		print("Correct")


builder = Gtk.Builder()
builder.add_from_file("Passcheck.glade")


window = builder.get_object("password_window")
window.show_all()

Gtk.main()