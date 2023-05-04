import customtkinter 
from tkinter import *
from back_end.Classes import connexion as conn
# import back_end.Classes.connexion as conn


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
    def seecars(self):
        my_conn=conn.db
        my_conn.execute("select * from user")
        i=0
        for user in my_conn:
            for j in range(len(user)):
                e = Label(self,width=10, text=user[j],
	                borderwidth=2,relief='ridge', anchor="w") 
                e.grid(row=i, column=j) 
                e.insert(END,user[j])
            i=i+1