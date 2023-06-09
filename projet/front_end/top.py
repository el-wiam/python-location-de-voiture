import customtkinter 
from tkinter import *
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import addcar
import users
from Modeles import connexion
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        window_width = 1000
        window_height = 600
        bg_color="black",
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.config(bg="black")
        self.title('TOPP')

        self.resizable(False, False)


    def forgot_password(self):
        # Email
        self.label_username = customtkinter.CTkLabel(self, 
                                            text="Username / email : ",
                                            bg_color="black")
        self.label_username.place(x=440, y=100)

        self.username=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="black",
                                             width=200,
                                             height=50
                                             )
        self.username.place(x=400, y=150) 

        # password 
        self.label_username = customtkinter.CTkLabel(self, 
                                            text="Password : ",
                                            bg_color="black")
        self.label_username.place(x=470, y=250)

        self.PasswordEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="black",
                                             width=200,
                                             height=50)
        self.PasswordEntry.place(x=400, y=300 ) 

        def forget():
            user = self.username.get()
            pwd = self.PasswordEntry.get()
            sql = "SELECT * FROM user"
            connexion.db.execute(sql)
            clients = connexion.db.fetchall()
            for client in clients:
                if user==client[4]:
                    us = users.utilisateur()
                    us.update_password(pwd)
                else:
                    print("Identifiants invalides")

        # button
        self.update_pass = customtkinter.CTkButton(self, 
                                                fg_color='#FFED00', 
                                                text='Update Password', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda:forget())
        self.update_pass.place(x=380, y=410)



    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = addcar.ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

