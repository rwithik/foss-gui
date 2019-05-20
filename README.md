Introduction
============

GTK, or the GIMP Toolkit, is a multi-platform toolkit for creating
graphical user interfaces. Offering a complete set of widgets, GTK is
suitable for projects ranging from small one-off tools to complete
application suites.

GTK is written in C but has been designed from the ground up to support
a wide range of languages, not only C/C++. Using GTK from languages such
as Perl and Python (especially in combination with the Glade GUI
builder) provides an effective method of rapid application development.

GTK is free software and part of the GNU Project. However, the licensing
terms for GTK, the GNU LGPL, allow it to be used by all developers,
including those developing proprietary software, without any license
fees or royalties.

Some popular GTK applications include:

1.  GIMP

2.  Kitty Terminal

3.  Inkscape

4.  Pigdin

5.  Glade Interface Designer

6.  GNOME Boxes

7.  GNOME Terminal

About the Application
=====================

The project that we decided to do is a simple password manager. An
application that stores your passwords and can place them into your
clipboard when you need to use them. Since not everyone should have
access to your passwords, it asks for the master password when you start
it up and gives you access only if you manage to get the master password
correct.

The application stores the service or website, the username(can store
multiple usernames for the same website), and password for each
username. The user can then copy the password or delete an entry all
together.

The github link of our project is https://github.com/rwithik/foss-gui

Development of the Application
==============================

The code is divided into two files: app.py and windowClass.py. The
app.py file generates the initial password verification window. It loads
the main application window if the entered password is correct.

We have used the Notify class to send notifications via the system dbus.
Messages likeIncorrect password and successfully adding and removing
entries are sent as notifications.

The entries are stored in the following format in a dictionary:

``` {.python tabspace="4"}
{
website: {
    username: password, 
    username: password, 
    ...
    }, 
website: {
    username: password, 
    username: password
    ...
    }, 
    ...
}
```

windowClass.py
--------------

This file has a class named MainWindow that inherits the Gtk.Window
class. It generates the main application window.

The functions defened in the class:

### add\_new\_entry()

This function is called when the Add entry button is clicked. It inserts
a new entry into the dictionary and writes it to the file. It then
redraws the whole window.

### delete\_clicked()

This function is called when the delete button of any entry is clilcked.
The website and username is passed to the function and the corresponding
entry in the dictionary is deleted.

### get\_grid()

This function returns a Gtk.Grid element with all the entries and input
fields.

### on\_copy\_clicked()

This function is called when the Copy button of an entry is clicked. It
shows a notification and places the password into the clipboard, ready
to be pasted.

### send\_notification()

An utility function to display a notification message.

### \_\_redraw()

A private function that redraws the window after each update.

app.py
------

This file import the windowClass.py file. This file generates the master
password dialog box. It has only one method defined, verify(), to verify
the given password. If the password is correct, it creates a MainWindow
object and start the main application window.

Conclusion
==========

The Password Manager is working satisfactorily. We learnt a lot of new
things about GTK by completing this project, not only about GTK, but
also about the common coding conventions.

References
==========

-   stackoverflow.com

-   GTK Read the Docs

-   GNOME GTK3 Reference

-   programcreek.com
