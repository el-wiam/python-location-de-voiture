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
        self.title('SEARCH')
        self.resizable(False, False)

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)

        self.bg_imageLogo.place(x=0, y=0)
        self.Logiin_backgroundImage = PhotoImage(file="assets\\search.png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=0, y=120)
    def recherche(self):
        self.label_search = customtkinter.CTkLabel(self, 
                                            text="search: ",
                                            bg_color="black",
                                            font=('Times',24))
        self.label_search.place(x=350, y=50)
        self.modify=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=300,
                                             height=40)
        self.modify.place(x=500, y=50)

        txt=customtkinter.CTkTextbox(self,
                                    width=580,
                                    height=400) 
        txt.place(x=400, y=200)
        txt.focus_set()
        self.buttn = customtkinter.CTkButton(  self, 
                                                fg_color='#FFED00', 
                                                text='find', 
                                                text_color="black",
                                                bg_color='black',
                                                width=106, 
                                                height=40,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2')
        self.buttn.place(x=820, y=50)

        def search():
            c=conn.db
            ser = self.modify.get()
            sql="SELECT * from voiture where 1=1"
            if ser:
                sql += " AND marque LIKE '%{}%'".format(ser)
            else :
                sql += " AND model LIKE '%{}%'".format(ser)
            c.execute(sql)
            rows=c.fetchall()
            txt.delete(1.0,END)
            for row in rows:
                txt.insert(END,"{}\n".format(row))
                txt.yview(END)
            self.modify.focus_set()
        self.buttn.configure(command=search)        
