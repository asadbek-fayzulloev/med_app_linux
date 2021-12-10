import gi, requests, os
HOME = os.getcwd()
#path
GLADE=HOME+"/front/ui/user.glade"
#objects


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file(GLADE)

Login = builder.get_object("login")
Login.show_all()

ClientMenu = builder.get_object("ClientMenu")

ClientSupport = builder.get_object("ClientSupport")

ClientsTable = builder.get_object("ClientsTable")

DoctorMenu = builder.get_object("DoctorMenu")

DoctorSupport = builder.get_object("DoctorSupport")

DoctorsTable = builder.get_object("DoctorsTable")

class Handler:
    def submit_clicked(self, *args):
        Login.hide()
        ClientMenu.show()
    
    def submit_clicked(self, *args):
        Login.hide()
        ClientMenu.show()

    def onDestroy(self, *args):
        Gtk.main_quit()

    

        

builder.connect_signals(Handler())

Gtk.main()