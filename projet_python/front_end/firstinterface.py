from tkinter import *
import customtkinter
import top
import toplevel
import addUser
import seecars




class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        height = 600
        width = 1000
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.title("WELCOME")
        self.config(bg='black')
        
        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)
        # self.bg_imageLogo.pack(side="left", padx=0, pady=0)

        self.Logiin_backgroundImage = PhotoImage(file="assets\\first.png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=0, y=120)

        self.label_nom = customtkinter.CTkLabel(self, 
                                            text="BIENVENUS  ",
                                            width=200,
                                            height=50,
                                            font=('Arial', 25),
                                            bg_color="black")
        self.label_nom.place(x=400, y=80)

        self.signup = customtkinter.CTkButton(
                                                self, 
                                                fg_color='#FFED00', 
                                                text='SIGN UP', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda: addUser.ToplevelWindow(self).addUser(),
        )
        self.signup.place(x=600, y=250)
        self.login = customtkinter.CTkButton(
                                                 self, 
                                                fg_color='#FFED00', 
                                                text='LOG IN', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda: toplevel.ToplevelWindow(self).login(),
        )
        self.login.place(x=600, y=350)
        self.seecars = customtkinter.CTkButton(
                                                 self, 
                                                fg_color='#FFED00', 
                                                text='consuter les voitures', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda: seecars.ToplevelWindow(self).seecars(),
        )
        self.seecars.place(x=600, y=450)

        

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = top.ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

if __name__ == "__main__":
    app = App()
    app.mainloop()
    