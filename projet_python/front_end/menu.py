from tkinter import *
import customtkinter
from tkinter import filedialog
import toplevel
import addUser
import seecars


class menu(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        height = 700
        width = 1000
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.title("menu")
        self.config(bg='black')

        self.Logo_backgroundImage = PhotoImage(file="assets\\2 (1).png")
        self.bg_imageLogo = customtkinter.CTkLabel(
            self,
            image=self.Logo_backgroundImage,
            fg_color="black",
            text="",
        )
        self.bg_imageLogo.place(x=0, y=0)
        self.Logiin_backgroundImage = PhotoImage(file="assets\\reservation.png")
        self.bg_imageLogiin = customtkinter.CTkLabel(
            self,
            image=self.Logiin_backgroundImage,
            fg_color="black",
            text=""
        )
        self.bg_imageLogiin.place(x=0, y=120)
        
        # nomcomplet
        self.label_nom = customtkinter.CTkLabel(self, 
                                            text="Nom complet : ",
                                            bg_color="black")
        self.label_nom.place(x=450, y=100)

        self.nomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.nomEntry.place(x=600, y=100) 

        # modele 
        self.label_prenom = customtkinter.CTkLabel(self, 
                                            text="Numero de telephone : ",
                                            bg_color="black")
        self.label_prenom.place(x=450, y=200)

        self.prenomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.prenomEntry.place(x=600, y=200) 
        # type_carburant
        self.label_username = customtkinter.CTkLabel(self, 
                                            text="CIN  : ",
                                            bg_color="black")
        self.label_username.place(x=450, y=300)

        self.usernameEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.usernameEntry.place(x=600, y=300) 

        # prix de location
        self.label_Email = customtkinter.CTkLabel(self, 
                                            text="numero de permis : ",
                                            bg_color="black")
        self.label_Email.place(x=450, y=400)

        self.EmailEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.EmailEntry.place(x=600, y=400) 
        # choisir le voiture
        self.label_Password = customtkinter.CTkLabel(self, 
                                            text="choisir une voiture: ",
                                            bg_color="black")
        self.label_Password.place(x=450, y=500)   
        combobox = customtkinter.CTkComboBox(self,
                                     values=["dispo", "non-dispo"],
                                     dropdown_fg_color="black",
                                     text_color="white",
                                     width=200,
                                     height=50,
                                     corner_radius=10
                                    )
        combobox.place(x=600, y=500)
        combobox.set("voiture disponible ")

        # button
        self.signButton = customtkinter.CTkButton(  self, 
                                                fg_color='#FFED00', 
                                                text='effectuer la reservation', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2')
        self.signButton.place(x=380, y=600)


if __name__ == "__main__":
    app = menu()
    app.mainloop()