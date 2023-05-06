import customtkinter 
from tkinter import *
import connexion as conn
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
        self.bg_imageLogo.place(x=0, y=0)
    def seereservation(self):
        my_conn=conn.db
        my_conn.execute("select * from reservation")
        i=0
        for res in my_conn:
            for j in range(len(res)):
                e= customtkinter.CTkEntry(self, width=10, fg='blue')
                e.grid(row=i, column=j) 
                e.insert(END,res[j])
                i=i+1
                W=customtkinter.CTkLabel(self,width=10,text='id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=0)
                W=customtkinter.CTkLabel(self,width=10,text='nom complet',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=1)
                W=customtkinter.CTkLabel(self,width=10,text='CIN',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=3)
                W=customtkinter.CTkLabel(self,width=10,text='numero de telephone',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=2)
                W=customtkinter.CTkLabel(self,width=10,text='numero de permis de conduite',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=4)
                W=customtkinter.CTkLabel(self,width=10,text='voiture',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                W.grid(row=0,column=6)            
                
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
        self.Login_button.place(x=600, y=550)