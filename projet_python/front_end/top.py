import customtkinter 
import addcar

from tkinter import *
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

    # def signIN(self):
    #     # Nom
    #     self.label_nom = customtkinter.CTkLabel(self, 
    #                                         text="Nom : ",
    #                                         bg_color="black")
    #     self.label_nom.place(x=20, y=20)

    #     self.nomEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.nomEntry.place(x=120, y=20) 

    #     # prenom 
    #     self.label_prenom = customtkinter.CTkLabel(self, 
    #                                         text="Prenom : ",
    #                                         bg_color="black")
    #     self.label_prenom.place(x=400, y=20)

    #     self.prenomEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.prenomEntry.place(x=500, y=20) 
    #     # username 
    #     self.label_username = customtkinter.CTkLabel(self, 
    #                                         text="username : ",
    #                                         bg_color="black")
    #     self.label_username.place(x=20, y=100)

    #     self.usernameEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.usernameEntry.place(x=120, y=100) 
    #     # CIN
    #     self.label_CIN = customtkinter.CTkLabel(self, 
    #                                         text="CIN : ",
    #                                         bg_color="black")
    #     self.label_CIN.place(x=400, y=100)

    #     self.CINEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.CINEntry.place(x=500, y=100) 

    #     # Tele
    #     self.label_Tele = customtkinter.CTkLabel(self, 
    #                                         text="Telephone : ",
    #                                         bg_color="black")
    #     self.label_Tele.place(x=20, y=180)

    #     self.TeleEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.TeleEntry.place(x=120, y=180) 

    #     # Email
    #     self.label_Email = customtkinter.CTkLabel(self, 
    #                                         text="Email : ",
    #                                         bg_color="black")
    #     self.label_Email.place(x=400, y=180)

    #     self.EmailEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.EmailEntry.place(x=500, y=180) 

    #     # Password
    #     self.label_Password = customtkinter.CTkLabel(self, 
    #                                         text="Password : ",
    #                                         bg_color="black")
    #     self.label_Password.place(x=20, y=260)

    #     self.PasswordEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.PasswordEntry.place(x=120, y=260) 

    #     # Confirm Password
    #     self.label_ConfirmPassword = customtkinter.CTkLabel(self, 
    #                                         text="ConfirmPassword : ",
    #                                         bg_color="black")
    #     self.label_ConfirmPassword.place(x=400, y=260)

    #     self.ConfirmPasswordEntry=customtkinter.CTkEntry(self,
    #                                          bg_color="#3D404B",
    #                                          fg_color="white",
    #                                          width=200,
    #                                          height=50)
    #     self.ConfirmPasswordEntry.place(x=500, y=260) 

    #     # button
    #     self.signButton = customtkinter.CTkButton(  self, 
    #                                             fg_color='#FFED00', 
    #                                             text='Sign UP', 
    #                                             text_color="black",
    #                                             bg_color='black',
    #                                             width=256, 
    #                                             height=45,
    #                                             font=("yu gothic ui bold", 16 * -1),
    #                                             cursor='hand2')
    #     self.signButton.place(x=380, y=410)

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

        # button
        self.update_pass = customtkinter.CTkButton(  self, 
                                                fg_color='#FFED00', 
                                                text='Update Password', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2')
        self.update_pass.place(x=380, y=410)
    def menu(self):
        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)

        self.Logiin_backgroundImage = PhotoImage(file="assets\\carmenu (1).png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=20, y=120)

        # ================ add a car button ============================
        self.Login_button = customtkinter.CTkButton(
            self,
            width=230,
            height=40,
            text=" ajouter voiture",
            bg_color="black",
            cursor="hand2", 
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
            command=lambda: addcar.ToplevelWindow(self).addcar()
        )
        self.Login_button.place(x=600, y=200) 
        # ================ see cars button ============================
        self.see_car = customtkinter.CTkButton(
            self,
            width=230,
            height=40,
            text=" consulter la liste des voitures ",
            bg_color="black",
            cursor="hand2",
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
        )
        self.see_car.place(x=600, y=300)      

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = addcar.ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

