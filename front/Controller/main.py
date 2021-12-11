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

RegisterPage = builder.get_object("RegisterPage")

USERNAME = builder.get_object("entry1")
PASSWORD = builder.get_object("entry2")

REG_EMAIL = builder.get_object("reg_email")
REG_ROLE = builder.get_object("reg_role")
#REG_USERNAME = builder.get_object("reg_role")
REG_PASSWORD = builder.get_object("reg_pass")
REG_PASSWORD_CHECK = builder.get_object("reg_check")

user_email = ""
user_role = ""
user_id = ""
HOST = '192.168.0.102'  # The server's hostname or IP address
PORT = 8888        # The port used by the server
class Handler:
    def submit_clicked(self, *args):
        
      
        result = []
        

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            req = 'GET /index.php/user/login?email='+str(USERNAME.get_text())+'&password='+str(PASSWORD.get_text())+' HTTP/1.0\r\n\r\n'
            s.sendall(bytes(req,'UTF-8'))
            data = s.recv(1024).decode("utf-8")
            if(data.index("[")>0):
                t = data[data.index("[")+len("["):data.index("]")]
                result = json.loads(t)
                user_id = result["id"]
                user_role = result["role"]
                user_email = result["email"]
                print('Wellcome ',(user_role))
            else:
                print("WRONG")
            
        if not user_role:
            print("Wrong credential")
        elif user_role=="doctor":
            Login.hide()
            DoctorMenu.show()
        else:
            Login.hide()
            ClientMenu.show()

    def on_client_support_clicked(self, *args):
        ClientMenu.hide()
        ClientSupport.show()

    def on_client_support_back_clicked(self, *args):
        ClientSupport.hide()
        ClientMenu.show_all()
    
    def on_appointment_register_clicked(self, *args):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            req = 'GET /index.php/user/register?role="'+str(REG_ROLE.get_text())+'"email='+str(REG_USERNAME.get_text())+'&password='+str(REG_PASSWORD.get_text())+' HTTP/1.0\r\n\r\n'
            s.sendall(bytes(req,'UTF-8'))
            data = s.recv(1024).decode("utf-8")
            if(data.index("[")>0):
                t = data[data.index("[")+len("["):data.index("]")]
                result = json.loads(t)
                user_id = result["id"]
                user_role = result["role"]
                user_email = result["email"]
                print('Wellcome ',(user_role))
            else:
                print("WRONG")
        ClientMenu.hide()
        AppointmentRegister.show()

    def on_register_page_clicked(self, *args):
        Login.hide()
        RegisterPage.show()

    def on_register_page_back_clicked(self, *args):
        RegisterPage.hide()
        Login.show_all()

    def on_appointment_back_clicked(self, *args):
        AppointmentRegister.hide()
        ClientMenu.show()

    def on_clients_table_clicked(self, *args):
        DoctorMenu.hide()
        ClientsTable.show()

    def on_doctors_table_clicked(self, *args):
        ClientMenu.hide()
        DoctorsTable.show()

    def on_doctors_table_back_clicked(self, *args):
        DoctorsTable.hide()
        ClientMenu.show()

    def on_clients_table_clicked(self, *args):
        DoctorMenu.hide()
        ClientsTable.show()

    def on_clients_table_back_clicked(self, *args):
        ClientsTable.hide()
        DoctorMenu.show()

    def on_doctor_support_clicked(self, *args):
        DoctorMenu.hide()
        DoctorSupport.show()

    def on_doctor_support_back_clicked(self, *args):
        DoctorSupport.hide()
        DoctorMenu.show_all()

    def on_client_menu_back_clicked(self, *args):
        ClientMenu.hide()
        Login.show_all()

    def on_doctor_menu_back_clicked(self, *args):
        DoctorMenu.hide()
        Login.show_all()

    def onDestroy(self, *args):
        Gtk.main_quit()

    

        

builder.connect_signals(Handler())

Gtk.main()