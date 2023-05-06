import customtkinter 
from tkinter import *
import connexion as conn



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
        self.title('check the users')

        self.resizable(False, False)

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=800, y=0)
    def seeusers(self):
        my_conn=conn.db
        my_conn.execute("select * from user")
        i=1
        for user in my_conn:
            for j in range(len(user)):
                e = customtkinter.CTkEntry(self, text_color='black',width=100, fg_color='white') 
                e.grid(row=i, column=j) 
                e.insert(END,user[j])
               
                W=customtkinter.CTkLabel(self,width=120,text='id',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=0)

                W=customtkinter.CTkLabel(self,width=120,text='nom complet',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=1)

                W=customtkinter.CTkLabel(self,width=120,text='CIN',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=2)

                W=customtkinter.CTkLabel(self,width=120,text='numero de telephone',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=3)

                W=customtkinter.CTkLabel(self,width=120,text='Username',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=4)

                W=customtkinter.CTkLabel(self,width=120,text='Email',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=6)

                W=customtkinter.CTkLabel(self,width=120,text='Numero de permis de conduite',anchor='w',bg_color='yellow',text_color='black')
                W.grid(row=0,column=7)       
            i=i+1