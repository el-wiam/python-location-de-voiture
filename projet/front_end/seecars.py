import customtkinter 
from tkinter import *
import sys 
sys.path.append("C:/Users/toshiba/Desktop/pyproject/python-location-de-voiture/projet")

from Modeles import connexion as conn


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
        self.title('check the cars')

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
        my_conn.execute("select * from voiture")
        i=0
        for car in my_conn:
            for j in range(len(car)):
                e= customtkinter.CTkEntry(self, width=10, fg='blue')
                e.grid(row=i, column=j) 
                e.insert(END,car[j])
                W=customtkinter.CTkLabel(self,width=10,text='id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=0)

                W=customtkinter.CTkLabel(self,width=10,text='marque',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=1)
                W=customtkinter.CTkLabel(self,width=10,text='type de carburant',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=2)
                W=customtkinter.CTkLabel(self,width=10,text='nombre de place',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=3)
                W=customtkinter.CTkLabel(self,width=10,text='transmission',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=4)
                W=customtkinter.CTkLabel(self,width=10,text='prix de location',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=5)
                W=customtkinter.CTkLabel(self,width=10,text='disponibilité',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=6)
                W=customtkinter.CTkLabel(self,width=10,text='image',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=7)
            i=i+1

            
