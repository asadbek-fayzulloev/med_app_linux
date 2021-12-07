import gi, requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("/home/jamshid/med_app_linux/front/Controller/RegisterPage.glade")

window1 = builder.get_object("RegisterPage")
window1.show_all()

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        builder = Gtk.Builder()
        builder.add_from_file("/home/jamshid/med_app_linux/front/Controller/RegisterPage.glade")
        window = builder.get_object("RegisterPage")
        window1.hide()
        window.show_all()
    def onButtonLogin(self, button):
        inputEmail = builder.get_object("email")
        
        payload = {"email": inputEmail}
        r = requests.get("https://httpbin.org/get", params=payload)
        print(r.status_code)


        

builder.connect_signals(Handler())

Gtk.main()