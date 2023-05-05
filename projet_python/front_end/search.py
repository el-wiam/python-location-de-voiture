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
    def recherche(self):
        frm=customtkinter.CTkFrame(self)
        Label(frm,text="enter what u search for").pack(side=LEFT)   
        modify=customtkinter.CTkEntry(frm) 
        modify.pack(side=LEFT , fill=BOTH , expand=1)
        modify.focus_set()

        buttn = Button(frm, text='Find')
        buttn.pack(side=RIGHT)
        frm.pack(side=TOP)

        txt = Text(self)

        txt.insert('1.0','''Enter here...''')
        txt.pack(side=BOTTOM)
        def search():
            txt.tag_remove('found', '1.0', END)
            ser = modify.get()
            if ser:
                idx = '1.0'
                while 1:
                    idx = txt.search(ser, idx, nocase=1,
                                    stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(ser))
                    
                    txt.tag_add('found', idx, lastidx)
                    idx = lastidx
                txt.tag_config('found', foreground='blue')
            modify.focus_set()
        buttn.config(command=search)       
