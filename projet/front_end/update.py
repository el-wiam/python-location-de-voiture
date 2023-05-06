import customtkinter 
from tkinter import *
import connexion as conn
from tkinter import ttk
from tkinter import BOTH, END, LEFT
# from sqlalchemy.exc import SQLAlchemyError


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
    def updtae(self):
       font1=('Times',14,'normal')
       self.columnconfigure(0,weight=4)
       self.columnconfigure(1,weight=2)
       self.rowconfigure(0, weight=1) 
       self.rowconfigure(1, weight=6) # change weight to 4
       self.rowconfigure(2, weight=2)
       frame_top=customtkinter.Frame(self,bg='white')
       frame_bottom=customtkinter.Frame(self,bg='white')

       frame_m_right=customtkinter.Frame(self,bg='#f8fab4')
       frame_m_left=customtkinter.Frame(self,bg='#284474')

       frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
       frame_m_left.grid(row=1,column=0,sticky='WENS')
       frame_m_right.grid(row=1,column=1,sticky='WENS')
       frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)

       trv = ttk.Treeview(frame_m_left, selectmode ='browse')
       trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)
       trv["columns"] = ("1", "2","3","4","5")
       trv.column("#0", width = 40, anchor ='w') # p_id
       trv.column("1", width = 150, anchor ='w') # p_name
       trv.column("2", width =100 , anchor ='w') # unit
       trv.column("3", width = 50, anchor ='w') # price
       trv.column("4", width = 50, anchor ='w') # category 
       trv.column("5", width = 80, anchor ='w') # available 

       trv.heading("#0", text ="id",anchor='w')
       trv.heading("1", text ="nom complet",anchor='w')
       trv.heading("3", text ="cin",anchor='w')
       trv.heading("2", text ="numero de telephone",anchor='w')
       trv.heading("4", text ="numero permis",anchor='w')
       trv.heading("5", text ="voiture",anchor='w')

       #Right side layout to display product details for Edit 
       id=customtkinter.CTkLabel(frame_m_right,text='P Name',font=font1)
       id.grid(row=0,column=0,sticky='nw')
       p_name=customtkinter.StringVar() # string variable for product name
       e_p_name=customtkinter.CTkEntry(frame_m_right,textvariable=p_name,font=font1)
       e_p_name.grid(row=0,column=1,columnspan=2)
       unit=customtkinter.StringVar()  # string variable for unit 
       lr2=customtkinter.CTkLabel(frame_m_right,text='Unit',font=font1)
       lr2.grid(row=1,column=0,sticky='nw')
       e_unit=customtkinter.CTkEntry(frame_m_right,textvariable=unit,font=font1)
       e_unit.grid(row=1,column=1,columnspan=2)
       price=customtkinter.DoubleVar() # double variable for price 
       lr3=customtkinter.CTkLabel(frame_m_right,text='Price',font=font1)
       lr3.grid(row=2,column=0,sticky='nw')
       e_price=customtkinter.CTkEntry(frame_m_right,textvariable=price,font=font1)
       e_price.grid(row=2,column=1,columnspan=2)

       b_update=customtkinter.CTkButton(frame_m_right,text='Update')
       b_update.grid(row=5,column=1)

       def show_items(cat): # Populating the treeview with records
            my_conn=conn.db
            for item in trv.get_children(): # loop all child items 
                trv.delete(item)        # delete them 
            query="SELECT * FROM reservation WHERE id=%s"
            r_set=my_conn.execute(query,cat) # get the record set from table 
            for dt in r_set: # add data to treeview 
                trv.insert("",'end',iid=dt[0],text=dt[0],
                            values=(dt[1],dt[2],dt[3],dt[4],dt[5]))
        
       def data_collect(self): # collect data to display for edit
            my_conn=conn.db
            selected=trv.focus() # gets the product id or p_id
            if(selected != None ):
                query="SELECT * from reservation WHERE id=%s"
                row=my_conn.execute(query,selected)
                s = row.fetchone() # row details as tuple
                if(s != None):
                    p_name.set(s[1])
                    unit.set(s[2])
                    price.set(s[3])
                    b_update.config(state='normal')
       
