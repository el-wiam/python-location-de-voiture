from tkinter import *
import customtkinter
from tkinter import filedialog
import toplevel
import addUser
import seecars
import reservation
import top


class menu(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        height = 700
        width = 1000
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.title("menu")
        self.config(bg='black')

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)

        self.Logiin_backgroundImage = PhotoImage(file="assets\\menuUser.png")
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
            text=" Consulter les voitures ",
            bg_color="black",
            cursor="hand2", 
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
            command=lambda: seecars.ToplevelWindow(self).seecars()
        )
        self.Login_button.place(x=600, y=200) 
        # ================ see cars button ============================
        self.see_car = customtkinter.CTkButton(
            self,
            width=230,
            height=40,
            text=" effectuer une reservation ",
            bg_color="black",
            cursor="hand2",
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
            command=lambda: reservation.ToplevelWindow(self).reservation()
        )
        self.see_car.place(x=600, y=300)    


if __name__ == "__main__":
    app = menu()
    app.mainloop()