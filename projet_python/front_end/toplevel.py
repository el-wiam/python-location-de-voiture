from tkinter import *
import customtkinter
import top

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        height = 600
        width = 1000
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.title("login")
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

        self.Logiin_backgroundImage = PhotoImage(file="assets\\logiin (1).png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=0, y=120)

        # self.Login_backgroundImage = PhotoImage(file="assets\loginp.png")
        # self.bg_imageLogin = customtkinter.CTkLabel(
        #     self,
        #     image=self.Login_backgroundImage,
        #     fg_color="black",
        #     text=""
        # )
        # self.bg_imageLogin.place(x=650,y=140)
        
        # ============================= GO TO SIGN UP =============================
        # ================ Email Name Section ====================
        # ICON email
        self.Login_emailName_image = PhotoImage(file="assets\\iconeEmail.png")
        self.Login_emailName_image_Label = customtkinter.CTkLabel(
            self,
            text="",
            fg_color="black",
            image=self.Login_emailName_image,
        )
        self.Login_emailName_image_Label.place(x=500,y=140)

        # Label email name
        self.Login_emailName_text = customtkinter.CTkLabel(
            self,
            text="Email account",
            fg_color="black",
            font=("yu gothic ui SemiBold", 13 * -1),
        )
        self.Login_emailName_text.place(x=550, y=140)

        # input email
        email=StringVar()
        self.email_entry=customtkinter.CTkEntry(self,
                                            textvariable=email,
                                            width=300,
                                            height=30,
                                            corner_radius=30,
                                            bg_color="black")
        self.email_entry.place(x=550,y=190)
        # ================ Email Name Section =======================
        # *******************************************************************
        # *******************************************************************
        # ================ PASSWORD Name Section ====================

        # icon password  
        self.Login_pwdName_image = PhotoImage(file="assets\\iconPwd.png")
        self.Login_pwdName_image_Label = customtkinter.CTkLabel(
            self,
            text="",
            fg_color="black",
            image=self.Login_pwdName_image,
            bg_color="black"
        )
        self.Login_pwdName_image_Label.place(x=500, y=240)

        # Label password name
        self.Login_pwdName_text = customtkinter.CTkLabel(
            self,
            text="Password",
            fg_color="black",
            font=("yu gothic ui SemiBold", 13 * -1),
        )
        self.Login_pwdName_text.place(x=550, y=240)

        # input password
        pwd=StringVar()
        self.pwd_Entry=customtkinter.CTkEntry(self,
                                            textvariable=pwd,
                                            width=300,
                                            height=30,
                                            corner_radius=30,
                                            bg_color="black")
        self.pwd_Entry.place(x=550,y=290)
        # ================ PASSWORD Name Section ====================
        # ================ Submit button ============================
        self.Login_button = customtkinter.CTkButton(
            self,
            width=230,
            height=40,
            text="login",
            bg_color="black",
            cursor="hand2",
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
            command=lambda: top.ToplevelWindow(self).menu(),
        )
        self.Login_button.place(x=600, y=400)

        # ================ Submit button ============================
        # ================ forget button ============================

        self.forgotPassword = customtkinter.CTkButton(
            self,
            text="Forgot Password",
            width=150, height=35,
            text_color="#FFE601",
            font=("yu gothic ui Bold", 13 * -1),
            bg_color="black",
            fg_color="black",
            hover_color="black",
            border_width=0,
            cursor="hand2",
            command=lambda: top.ToplevelWindow(self).forgot_password(),
        )
        self.forgotPassword.place(x=500, y=340)
        # ================ forget button ============================
        # ================ sign in button ============================
        self.forgotPassword = customtkinter.CTkButton(
            self,
            text="Sign UP",
            width=150, height=35,
            text_color="#FFE601",
            font=("yu gothic ui Bold", 13 * -1),
            bg_color="black",
            fg_color="black",
            hover_color="black",
            border_width=0,
            cursor="hand2",
            command=lambda: top.ToplevelWindow(self).signIN(),
        )
        self.forgotPassword.place(x=750, y=340)
        # ================ sign in button ============================
        # ============================= GO TO SIGN UP =============================

        # self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        # self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = top.ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

if __name__ == "__main__":
    app = App()
    app.mainloop()
    