import array
import gi, requests, os
import socket
import json
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

AppointmentRegister = builder.get_object("AppointmentRegister")

USERNAME = builder.get_object("entry1")
PASSWORD = builder.get_object("entry2")

class Handler:
    def submit_clicked(self, *args):
        
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 8888        # The port used by the server
        result = []
        r_email = ""
        r_role = ""
        r_id = ""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            req = 'GET /index.php/user/login?email='+str(USERNAME.get_text())+'&password='+str(PASSWORD.get_text())+' HTTP/1.0\r\n\r\n'
            s.sendall(bytes(req,'UTF-8'))
            data = s.recv(1024).decode("utf-8")
            if(data.index("[")>0):
                t = data[data.index("[")+len("["):data.index("]")]
                result = json.loads(t)
                print(result)
                r_id = result["id"]
                r_role = result["role"]
                r_email = result["email"]
                print(r_role)
            else:
                print("WRONG")
            
        if USERNAME.get_text() == "client" and PASSWORD.get_text() == "1234":
            Login.hide()
            ClientMenu.show()
        if USERNAME.get_text() == "doctor" and PASSWORD.get_text() == "5678":
            Login.hide()
            DoctorMenu.show()

    def on_client_support_clicked(self, *args):
        ClientMenu.hide()
        ClientSupport.show()

    def on_client_support_back_clicked(self, *args):
        ClientSupport.hide()
        ClientMenu.show_all()
    
    def on_appointment_register_clicked(self, *args):
        ClientMenu.hide()
        AppointmentRegister.show()

    def on_appointment_back_clicked(self, *args):
        ClientMenu.hide()
        Login.show_all()

    def on_doctors_table_clicked(self, *args):
        ClientMenu.hide()
        DoctorsTable.show()

    def on_client_table_clicked(self, *args):
        ClientMenu.hide()
        ClientsTable.show()

    def on_doctor_support_clicked(self, *args):
        ClientMenu.hide()
        DoctorSupport.show()

    def on_doctors_support_back_clicked(self, *args):
        DoctorSupport.hide()
        DoctorMenu.show_all()

    def on_client_menu_back_clicked(self, *args):
        ClientMenu.hide()
        Login.show_all()

    def onDestroy(self, *args):
        Gtk.main_quit()

    

        

builder.connect_signals(Handler())

Gtk.main()