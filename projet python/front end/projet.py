import customtkinter
from tkinter import *
import signIN
window = customtkinter.CTk()
height = 600
width = 1000
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")
window.title("login")
window.config(bg='black')


Login_backgroundImage = PhotoImage(file="assets\\background.png")
bg_imageLogin = Label(
    window,
    image=Login_backgroundImage,
    bd=0,
)
bg_imageLogin.place(x=100, y=100)

# ============================= GO TO SIGN UP =============================


# ================ Email Name Section ====================
# ICON email
Login_emailName_image = PhotoImage(file="assets\\iconeEmail.png")
Login_emailName_image_Label = Label(
    bg_imageLogin,
    fg="white",
    image=Login_emailName_image,
    bg="black"
)
Login_emailName_image_Label.place(x=370,y=250)
# Label email name
Login_emailName_text = Label(
    bg_imageLogin,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 19 * -1),
    bg="black"
)
Login_emailName_text.place(x=430, y=254)
# input email
email=StringVar()
email_entry=customtkinter.CTkEntry(window,
                                     textvariable=email,
                                     width=300,
                                     height=30,
                                     corner_radius=30,
                                     bg_color="black")
email_entry.place(x=370,y=268)

# ================ Email Name Section =======================
# *******************************************************************
# *******************************************************************
# ================ PASSWORD Name Section ====================
# icon password  
Login_pwdName_image = PhotoImage(file="assets\\iconPwd.png")
Login_pwdName_image_Label = Label(
    bg_imageLogin,
    fg="white",
    image=Login_pwdName_image,
    bg="black"
)
Login_pwdName_image_Label.place(x=370, y=400)
# Label password
Login_pwdName_text = Label(
    bg_imageLogin,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 19 * -1),
    bg="black"
)
Login_pwdName_text.place(x=430, y=404)
# input password
password=StringVar()
pwd_entry=customtkinter.CTkEntry(window,
                                     textvariable=password,
                                     width=300,
                                     height=30,
                                     corner_radius=30,
                                     bg_color="black")
pwd_entry.place(x=370,y=370)
# ================ PASSWORD Name Section ====================
# ================ Submit button ============================
Login_button = customtkinter.CTkButton(
    bg_imageLogin,
    width=300,
    height=50,
    text="login",
    bg_color="black",
    cursor="hand2",
    fg_color="#FFED00",
    text_color="black",
    font=("yu gothic ui Bold", 18 * -1),
    corner_radius=8,
)
Login_button.place(x=300, y=400)
# ================ Submit button ============================
# ================ forget button ============================

forgotPassword = Button(
    master=bg_imageLogin,
    text="Forgot Password",
    fg="#FFE601",
    font=("yu gothic ui Bold", 20 * -1),
    bg="black",
    bd=0,
    activebackground="black",
    activeforeground="#ffffff",
    cursor="hand2",
    command=lambda: signIN.traitement.forgot_password(),
)
forgotPassword.place(x=400, y=550, width=150, height=35)

# ================ forget button ============================
# ================ sign in button ============================
forgotPassword = Button(
    bg_imageLogin,
    text="Sign IN",
    fg="#FFE601",
    font=("yu gothic ui Bold", 20 * -1),
    bg="black",
    bd=0,
    activebackground="black",
    activeforeground="#ffffff",
    cursor="hand2",
    command=lambda: signIN.traitement.signIN(),
)
forgotPassword.place(x=800, y=550, width=150, height=35)
# ================ sign in button ============================


# ============================= GO TO SIGN UP =============================

window.resizable(False, False)
window.mainloop()
