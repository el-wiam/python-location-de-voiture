from tkinter import *
# ================ Sign in Section ====================
class traitement:
    def signIN():
        win = Toplevel()
        window_width = 1000
        window_height = 600
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        win.title('sign in')
        # win.iconbitmap('images\\aa.ico')
        win.configure(background='black')
        win.resizable(False, False)

        # ===================== Nom =====================
        nom_entry = Entry(win, bg="#3D404B", 
                            font=("yu gothic ui semibold", 12), 
                            highlightthickness=1,
                            fg="white",
                            bd=0)
        nom_entry.place(x=100, y=80, width=256, height=50)
        nom_entry.config(highlightbackground="#3D404B", 
                            highlightcolor="#FDEB19")
        nom_label = Label(win, text='• Nom', 
                            fg="#FFFFFF", 
                            bg='black',
                            font=("yu gothic ui", 11, 'bold'))
        nom_label.place(x=100, y=50)

        # ===================== Nom =====================
        # ===================== Prenom ==================
        prenom_entry = Entry(win, bg="#3D404B", 
                            font=("yu gothic ui semibold", 12), 
                            highlightthickness=1,
                            fg="white",
                            bd=0)
        prenom_entry.place(x=600, y=80, width=256, height=50)
        prenom_entry.config(highlightbackground="#3D404B", 
                            highlightcolor="#FDEB19")
        prenom_label = Label(win, text='• Prenom', 
                            fg="#FFFFFF", 
                            bg='black',
                            font=("yu gothic ui", 11, 'bold'))
        prenom_label.place(x=600, y=50)
            
        # ===================== Prenom ==================
        # ===================== Email ===================
        email_entry = Entry(win, bg="#3D404B", 
                                font=("yu gothic ui semibold", 12), 
                                highlightthickness=1,
                                fg="white",
                                bd=0)
        email_entry.place(x=100, y=200, width=760, height=50)
        email_entry.config(highlightbackground="#3D404B", 
                            highlightcolor="#FDEB19")
        email_label = Label(win, text='• Email', 
                            fg="#FFFFFF", 
                            bg='black',
                            font=("yu gothic ui", 11, 'bold'))
        email_label.place(x=100, y=170)
        # ===================== Email ===================
        # ===================== password one =====================
        pwd_entry = Entry(win, bg="#3D404B", 
                            font=("yu gothic ui semibold", 12), 
                            highlightthickness=1,
                            fg="white",
                            bd=0)
        pwd_entry.place(x=100, y=320, width=256, height=50)
        pwd_entry.config(highlightbackground="#3D404B", 
                            highlightcolor="#FDEB19")
        pwd_label = Label(win, text='• Password', 
                            fg="#FFFFFF", 
                            bg='black',
                            font=("yu gothic ui", 11, 'bold'))
        pwd_label.place(x=100, y=280)

        # ===================== password one =====================
        # ===================== password confirm ==================
        pwd_confirm_entry = Entry(win, bg="#3D404B", 
                            font=("yu gothic ui semibold", 12), 
                            highlightthickness=1,
                            fg="white",
                            bd=0)
        pwd_confirm_entry.place(x=600, y=320, width=256, height=50)
        pwd_confirm_entry.config(highlightbackground="#3D404B", 
                            highlightcolor="#FDEB19")
        pwd_confirm_label = Label(win, text='• Password confirm', 
                            fg="#FFFFFF", 
                            bg='black',
                            font=("yu gothic ui", 11, 'bold'))
        pwd_confirm_label.place(x=600, y=280)
            
        # ===================== password confirm ==================
        # ===================== Inscription button ==================

        update_pass = Button(win, fg='black', 
                            text="S'inscrire", 
                            bg='#FDEB19', 
                            font=("yu gothic ui", 12, "bold"),
                            cursor='hand2', relief="flat", bd=0, 
                            highlightthickness=0, 
                            activebackground="#D1BD00")
        update_pass.place(x=350, y=450, width=256, height=45)
        # ===================== Inscription button ==================
        # ================ Sign Up Section ====================

# *******************************************************************************************************************
# *******************************************************************************************************************
# *******************************************************************************************************************

    # ================ Forget Password Section ====================

    def forgot_password():

        win = Toplevel()
        window_width = 350
        window_height = 350
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        win.title('Forgot Password')
        # win.iconbitmap('images\\aa.ico')
        win.configure(background='black')
        win.resizable(False, False)

        # ====== Email ====================
        email_entry3 = Entry(win, bg="#3D404B", 
                            font=("yu gothic ui semibold", 12), 
                            highlightthickness=1,
                            fg="white",
                            bd=0)
        email_entry3.place(x=40, y=80, width=256, height=50)
        email_entry3.config(highlightbackground="#3D404B", 
                            highlightcolor="#FDEB19")
        email_label3 = Label(win, text='• Email', 
                            fg="#FFFFFF", 
                            bg='black',
                            font=("yu gothic ui", 11, 'bold'))
        email_label3.place(x=40, y=50)

        # ====  New Password ==================
        new_password_entry = Entry(win,
                                bg="#3D404B", 
                                font=("yu gothic ui semibold", 12), 
                                fg="white",
                                show='•', 
                                highlightthickness=1,
                                bd=0)
        new_password_entry.place(x=40, y=180, width=256, height=50)
        new_password_entry.config(highlightbackground="#3D404B", 
                                highlightcolor="#FDEB19")
        new_password_label = Label(win, text='• New Password', 
                                fg="#FFFFFF", 
                                bg='black',
                                font=("yu gothic ui", 11, 'bold'))
        new_password_label.place(x=40, y=150)

        # ======= Update password Button ============
        update_pass = Button(win, fg='black', 
                            text='Update Password', 
                            bg='#FDEB19', 
                            font=("yu gothic ui", 12, "bold"),
                            cursor='hand2', relief="flat", bd=0, 
                            highlightthickness=0, 
                            activebackground="#D1BD00")
        update_pass.place(x=40, y=260, width=256, height=45)
    # ================ Forget Password Section ====================


# window.mainloop()