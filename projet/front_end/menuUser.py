import customtkinter 
from tkinter import *
from tkinter import filedialog
import search
import reservation
import seecars


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
        self.title('MENU USER')

        self.resizable(False, False)
        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)
    def menuuser(self):
        self.usermenu = customtkinter.CTkLabel(self, 
                                            text="MENU USER  ",
                                            width=200,
                                            height=50,
                                            font=('Arial', 25),
                                            bg_color="black")
        self.usermenu.place(x=400, y=80)
        self.Logiin_backgroundImage = PhotoImage(file="assets\\menuUser.png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=20, y=120)
        self.Login_button = customtkinter.CTkButton(
            self,
            width=230,
            height=40,
            text=" effectuer reservation",
            bg_color="black",
            cursor="hand2", 
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
            command=lambda: reservation.ToplevelWindow(self).reservation()
        )
        self.Login_button.place(x=600, y=200) 
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
            command=lambda: seecars.ToplevelWindow(self).seecars() )
        self.see_car.place(x=600, y=300) 

        self.see_car = customtkinter.CTkButton(
                self,
                width=230,
                height=40,
                text=" rechercher les voitures ",
                bg_color="black",
                cursor="hand2",
                fg_color="#FFED00",
                text_color="black",
                font=("yu gothic ui Bold", 16 * -1),
                corner_radius=20,
                command=lambda: search.ToplevelWindow(self).recherche()
            )
        self.see_car.place(x=600, y=400) 


