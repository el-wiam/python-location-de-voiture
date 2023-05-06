import customtkinter 
from tkinter import *
from tkinter import filedialog
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modeles import connexion as conn
from admin import *
from voiture import voiture


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
    def addcar(self):
        # Marque
        self.label_marque = customtkinter.CTkLabel(self, 
                                            text="MARQUE : ",
                                            bg_color="black")
        self.label_marque.place(x=70, y=180)

        self.marqueEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.marqueEntry.place(x=200, y=180) 
        

        # modele 
        self.label_modele = customtkinter.CTkLabel(self, 
                                            text="modele : ",
                                            bg_color="black")
        self.label_modele.place(x=450, y=180)

        self.modeleEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.modeleEntry.place(x=600, y=180) 
        
        # type_carburant
        self.label_typec = customtkinter.CTkLabel(self, 
                                            text="type de carburant : ",
                                            bg_color="black")
        self.label_typec.place(x=70, y=250)

        self.typecEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.typecEntry.place(x=200, y=250) 
        
        # nombre de places
        self.label_nbp = customtkinter.CTkLabel(self, 
                                            text="nombre de places : ",
                                            bg_color="black")
        self.label_nbp.place(x=450, y=250)

        self.nbpEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.nbpEntry.place(x=600, y=250) 
        
        # transmission
        self.label_trans = customtkinter.CTkLabel(self, 
                                            text="transmission : ",
                                            bg_color="black")
        self.label_trans.place(x=70, y=320)

        self.transEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.transEntry.place(x=200, y=320) 
        

        # prix de location
        self.label_prix = customtkinter.CTkLabel(self, 
                                            text="prix de location : ",
                                            bg_color="black")
        self.label_prix.place(x=450, y=320)

        self.prixEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.prixEntry.place(x=600, y=320) 
        
        # disponibilité
        self.label_Password = customtkinter.CTkLabel(self, 
                                            text="disponibilité : ",
                                            bg_color="black")
        self.label_Password.place(x=70, y=400)   
        combobox = customtkinter.CTkComboBox(self,
                                     values=["dispo", "non-dispo"],
                                     dropdown_fg_color="black",
                                     text_color="white",
                                     width=200,
                                     height=50,
                                     corner_radius=10
                                    )
        combobox.place(x=200, y=400)
        combobox.set("choisir disponibilité")
        

        # add image
        self.label_image = customtkinter.CTkLabel(self, 
                                            text="Image : ",
                                            bg_color="black")
        self.label_image.place(x=450, y=400)
    
        def uploadImg():
            imgfile= filedialog.askopenfilename(initialdir =  "/", title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
            img=PhotoImage(file=imgfile)
            return img
        self.imageButton = customtkinter.CTkButton(  self, 
                                                fg_color='white', 
                                                text='ajouter une image', 
                                                text_color="black",
                                                bg_color='black',
                                                width=200, 
                                                height=50,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command= uploadImg())
        self.imageButton.place(x=600, y=400)
        
        
        # button
        def addC(self):
            marque=self.marqueEntry.get()
            medel=self.modeleEntry.get()
            nbp=self.nbpEntry.get()
            typec=self.typecEntry.get()
            trans=self.transEntry.get()
            prix=self.prixEntry.get()
            imag=self.imageButton.cget()
            dispo=combobox.get()
            car=voiture.voiture(marque,medel,typec,nbp,trans,prix,dispo,imag)
            a=Admin()
            a.authentifier("admin","admin")
            a.ajouterVoiture(car)



        self.signButton = customtkinter.CTkButton(self, 
                                                fg_color='#FFED00', 
                                                text='AJOUTER', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command=lambda: addC())
        self.signButton.place(x=380, y=500)
        

        

        