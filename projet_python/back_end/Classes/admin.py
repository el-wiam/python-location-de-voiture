# import adminModel
import traceback
import users
from ..Modeles import adminModel 
# import voiture
# import adminModel
# import users
# import client

class Admin(users.utilisateur):
    def __init__(self,nomComplet='',cin='',numTel='',username='',password='',email='',numPermis=''):
        users.utilisateur.__init__(self,nomComplet,cin,numTel,username,password,email,numPermis)
    
    # VOITURE 
    def ajouterVoiture(self,voiture):
        try:
            return adminModel.Modeladmin.ajouterV(voiture)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifierVoiture(self,voiture,id):
        try:
            return adminModel.Modeladmin.modifierV(voiture,id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def supprimerVoiture(self,id):
        try:
            return adminModel.Modeladmin.supprimerV(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

# ====================================================================================================================================
# ====================================================================================================================================
    
    # CLIENT
    def ajouterClient(self,client):
        try:
            return adminModel.Modeladmin.ajouterClt(client)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifierClient(self,client,id):
        try:
            return adminModel.Modeladmin.modifierClt(client,id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def supprimerClient(self,id):
        try:
            return adminModel.Modeladmin.supprimerClt(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def consulterReservation(self):
        try:
            return adminModel.Modeladmin.consulterReservation()
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
    
    def consulterUser(self):
        try:
            return adminModel.Modeladmin.consulterClients()
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    

# admin=Admin("nomComplet","cin",9998888,"username","password","email","29292")
# v=voiture.voiture("marque","modele","typeCarburant",8,69,700,True,"image.png")
# admin.ajouterVoiture(v)
# admin=Admin()
# admin.supprimerVoiture(44)
# clt=client.Client("nomComplet","cin",9998888,"username","password","email","29292")
# admin=Admin()
# admin.ajouterClient(clt)
# admin=Admin()
# c=admin.consulterUser()
# print(c)

