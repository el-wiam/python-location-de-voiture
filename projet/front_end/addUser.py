
import sys 
sys.path.append("C:/Users/toshiba/Desktop/pyproject/python-location-de-voiture/projet")

# from projet import users
import client
import admin
import customtkinter 
from tkinter import *
import toplevel

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
        self.title('sign up')

        self.resizable(False, False)

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)
    def addUser(self):
        # Marque
        self.label_nom = customtkinter.CTkLabel(self, 
                                            text="Nom complet : ",
                                            bg_color="black")
        self.label_nom.place(x=70, y=180)

        self.nomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.nomEntry.place(x=200, y=180) 

        # modele 
        self.label_Tele= customtkinter.CTkLabel(self, 
                                            text="Numero de telephone : ",
                                            bg_color="black")
        self.label_Tele.place(x=450, y=180)

        self.TeleEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.TeleEntry.place(x=600, y=180) 
        # type_carburant
        self.label_CIN = customtkinter.CTkLabel(self, 
                                            text="CIN  : ",
                                            bg_color="black")
        self.label_CIN.place(x=70, y=250)

        self.CINEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.CINEntry.place(x=200, y=250) 
        # nombre de places
        self.label_Email = customtkinter.CTkLabel(self, 
                                            text="Email : ",
                                            bg_color="black")
        self.label_Email.place(x=450, y=250)

        self.EmailEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.EmailEntry.place(x=600, y=250) 

        # transmission
        self.label_username = customtkinter.CTkLabel(self, 
                                            text="usename : ",
                                            bg_color="black")
        self.label_username.place(x=70, y=320)

        self.usernameEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.usernameEntry.place(x=200, y=320) 

        # prix de location
        self.label_nbPermis = customtkinter.CTkLabel(self, 
                                            text="numero de permis : ",
                                            bg_color="black")
        self.label_nbPermis.place(x=450, y=320)

        self.nbPermisEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.nbPermisEntry.place(x=600, y=320) 

     #Password
        self.label_Password = customtkinter.CTkLabel(self, 
                                            text="Password : ",
                                            bg_color="black")
        self.label_Password.place(x=70, y=400)

        self.PasswordEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.PasswordEntry.place(x=200, y=400) 

        # Confirm Password
        self.label_ConfirmPassword = customtkinter.CTkLabel(self, 
                                            text="ConfirmPassword : ",
                                            bg_color="black")
        self.label_ConfirmPassword.place(x=450, y=400)
        self.ConfirmPasswordEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.ConfirmPasswordEntry.place(x=600, y=400)


        def add():
            nom_complet=self.nomEntry.get()
            cin=self.CINEntry.get()
            num_tel=self.TeleEntry.get()
            username=self.usernameEntry.get()

            password=self.PasswordEntry.get()
            passwordConfirm=self.ConfirmPasswordEntry.get()

            email=self.EmailEntry.get()
            num_permis=self.nbPermisEntry.get()

            if password==passwordConfirm :
                us=client.Client(nom_complet,cin,num_tel,username,password,email,num_permis)
                adm=admin.Admin()
                adm.authentifier("admin","admin")
                adm.ajouterClient(us)
                self.signButton.configure(command=toplevel.ToplevelWindow(self).login())
            else :
                print("password non identique avec password confirm")

        # button
        self.signButton = customtkinter.CTkButton(  self, 
                                                fg_color='#FFED00', 
                                                text='SIGN UP', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda:add())
        self.signButton.place(x=380, y=500)
        
        