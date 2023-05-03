from tkinter import *
import customtkinter
from PIL import Image,ImageTk
from tkinter import filedialog
import top


class menu(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        height = 600
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

        self.label_nom = customtkinter.CTkLabel(self, 
                                            text="MARQUE : ",
                                            bg_color="black")
        self.label_nom.place(x=70, y=180)

        self.nomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.nomEntry.place(x=200, y=180) 

        # modele 
        self.label_prenom = customtkinter.CTkLabel(self, 
                                            text="modele : ",
                                            bg_color="black")
        self.label_prenom.place(x=450, y=180)

        self.prenomEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.prenomEntry.place(x=600, y=180) 
        # type_carburant
        self.label_username = customtkinter.CTkLabel(self, 
                                            text="type de carburant : ",
                                            bg_color="black")
        self.label_username.place(x=70, y=250)

        self.usernameEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.usernameEntry.place(x=200, y=250) 
        # nombre de places
        self.label_CIN = customtkinter.CTkLabel(self, 
                                            text="nombre de places : ",
                                            bg_color="black")
        self.label_CIN.place(x=450, y=250)

        self.CINEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.CINEntry.place(x=600, y=250) 

        # transmission
        self.label_Tele = customtkinter.CTkLabel(self, 
                                            text="transmission : ",
                                            bg_color="black")
        self.label_Tele.place(x=70, y=320)

        self.TeleEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             width=200,
                                             height=50)
        self.TeleEntry.place(x=200, y=320) 

        # prix de location
        self.label_Email = customtkinter.CTkLabel(self, 
                                            text="prix de location : ",
                                            bg_color="black")
        self.label_Email.place(x=450, y=320)

        self.EmailEntry=customtkinter.CTkEntry(self,
                                             bg_color="#3D404B",
                                             fg_color="white",
                                             text_color="black",
                                             width=200,
                                             height=50)
        self.EmailEntry.place(x=600, y=320) 

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
        self.label_ConfirmPassword = customtkinter.CTkLabel(self, 
                                            text="Image : ",
                                            bg_color="black")
        self.label_ConfirmPassword.place(x=450, y=400)
    
        def uploadImg():
             filedialog.askopenfilename(initialdir =  "/", title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
        self.imageButton = customtkinter.CTkButton(  self, 
                                                fg_color='white', 
                                                text='add an image', 
                                                text_color="black",
                                                bg_color='black',
                                                width=200, 
                                                height=50,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2',
                                                command= uploadImg)
        self.imageButton.place(x=600, y=400)

        # button
        self.signButton = customtkinter.CTkButton(  self, 
                                                fg_color='#FFED00', 
                                                text='Sign UP', 
                                                text_color="black",
                                                bg_color='black',
                                                width=256, 
                                                height=45,
                                                font=("yu gothic ui bold", 16 * -1),
                                                cursor='hand2')
        self.signButton.place(x=380, y=500)


if __name__ == "__main__":
    app = menu()
    app.mainloop()