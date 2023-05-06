import customtkinter 
from tkinter import *

import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modeles import connexion as conn
from admin import *
import update



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
        self.title('check reservation')

        self.resizable(False, False)

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=800, y=0)
    def seereservation(self):
        
        my_conn=conn.db
        my_conn.execute("SELECT * FROM `reservation` ")
        i=1
        for res in my_conn:
            for j in range(len(res)):
                e= customtkinter.CTkEntry(self, text_color='black',width=100, fg_color='white')
                e.grid(row=i, column=j) 
                e.insert(END,res[j])  
                W=customtkinter.CTkLabel(self,width=120,text='id',anchor='w',bg_color='yellow',text_color='black',)
                W.grid(row=0,column=0)
                W=customtkinter.CTkLabel(self,width=120,text='nom complet',anchor='w',bg_color='yellow',text_color='black',)
                W.grid(row=0,column=1)
                W=customtkinter.CTkLabel(self,width=120,text='numero de tel',anchor='w',bg_color='yellow',text_color='black',)
                W.grid(row=0,column=2)
                W=customtkinter.CTkLabel(self,width=120,text='cin',anchor='w',bg_color='yellow',text_color='black',)
                W.grid(row=0,column=3)
                W=customtkinter.CTkLabel(self,width=120,text='permis de conduite',anchor='w',bg_color='yellow',text_color='black',)
                W.grid(row=0,column=4)
                W=customtkinter.CTkLabel(self,width=120,text='Voiture',anchor='w',bg_color='yellow',text_color='black',)
                W.grid(row=0,column=5)          
                
            i=i+1   


            self.Login_button = customtkinter.CTkButton(
            self,
            width=230,
            height=40,
            text="modifier reservation",
            bg_color="black",
            cursor="hand2",
            fg_color="#FFED00",
            text_color="black",
            font=("yu gothic ui Bold", 16 * -1),
            corner_radius=20,
            command=lambda: update.ToplevelWindow(self).update(),
        )
        self.Login_button.place(x=600, y=400)
    
        #def modifierReservation():
        