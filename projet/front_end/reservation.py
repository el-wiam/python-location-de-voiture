import customtkinter 
from tkinter import *
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modeles import connexion as conn
from admin import *
from client import Client
from reservationb import Reservation


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        window_width = 1000
        window_height = 800
        bg_color="black",
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.config(bg="black")
        self.title('reservation')

        self.resizable(False, False)

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)
    def reservation(self):
        self.bg_imageLogo.place(x=0, y=0)
        self.Logiin_backgroundImage = PhotoImage(file="assets\\reservation.png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=0, y=120)
        
        # nomcomplet
        self.label_nom = customtkinter.CTkLabel(self, 
                                            text="Nom complet : ",
                                            bg_color="black")
        self.label_nom.place(x=450, y=80)

        self.nomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=40)
        self.nomEntry.place(x=600, y=80) 

        # num
        self.label_prenom = customtkinter.CTkLabel(self, 
                                            text="Numero de telephone : ",
                                            bg_color="black")
        self.label_prenom.place(x=450, y=150)

        self.prenomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=40)
        self.prenomEntry.place(x=600, y=150) 
        # cin
        self.label_username = customtkinter.CTkLabel(self, 
                                            text="CIN  : ",
                                            bg_color="black")
        self.label_username.place(x=450, y=250)

        self.usernameEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=40)
        self.usernameEntry.place(x=600, y=250) 

        # permis
        self.label_Email = customtkinter.CTkLabel(self, 
                                            text="num permis de conduite : ",
                                            bg_color="black")
        self.label_Email.place(x=450, y=350)

        self.EmailEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=40)
        self.EmailEntry.place(x=600, y=350) 
        # choisir la voiture
        self.label_Password = customtkinter.CTkLabel(self, 
                                            text="choisir une voiture: ",
                                            bg_color="black")
        self.label_Password.place(x=450, y=450)

        c=conn.db
        c.execute("SELECT marque FROM `voiture`")
        result=c.fetchall()
        listvoiture=[]
        if result:
            listvoiture = [row[0] for row in result]
        else:
            print("No results found")
        combobox = customtkinter.CTkComboBox(self,
                                     values=listvoiture,
                                     dropdown_fg_color="black",
                                     text_color="white",
                                     width=200,
                                     height=40,
                                     corner_radius=10
                                    )
        combobox.place(x=600, y=450)
        combobox.set("voiture disponible ")

        self.label_dateD = customtkinter.CTkLabel(self, 
                                            text="date debut : ",
                                            bg_color="black")
        self.label_dateD.place(x=450, y=500)

        self.dateDEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=40)
        self.dateDEntry.place(x=600, y=500) 
        self.label_dateF = customtkinter.CTkLabel(self, 
                                            text="date fin : ",
                                            bg_color="black")
        self.label_dateF.place(x=450, y=550)

        self.dateFEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=150,
                                             height=40)
        self.dateFEntry.place(x=600, y=550) 
        #function 
        def reserve():
            nomc=self.nomEntry.get()
            num=self.prenomEntry.get()
            cin=self.usernameEntry.get()
            permis=self.EmailEntry.get()
            voiture=combobox.get()
            dated=self.dateDEntry.get()
            datef=self.dateFEntry.get()
            cli=Client()
            cli.reserver_voiture(nomc,num,cin,permis,voiture,dated,datef)
        

        # button
        self.signButton = customtkinter.CTkButton(  self, 
                                                fg_color='#FFED00', 
                                                text='effectuer la reservation', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda:reserve())
        self.signButton.place(x=380, y=700)