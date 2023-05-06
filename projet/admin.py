import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modeles import adminModel
import traceback

import users
from client import Client

class Admin(users.utilisateur):
    
    def __init__(self):
        pass
    
    # VOITURE 
    def ajouterVoiture(self,voiture):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.ajouterV(voiture)
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def modifierVoiture(self,voiture,id):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.modifierV(voiture,id)
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def supprimerVoiture(self,id):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.supprimerV(id)
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

# ====================================================================================================================================
# ====================================================================================================================================
    
    # CLIENT
    def ajouterClient(self,client):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.ajouterClt(client)
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def modifierClient(self,client,id):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.modifierClt(client,id)
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def supprimerClient(self,id):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.supprimerClt(id)
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def consulterReservation(self):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.consulterReservation()
            except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()
        
    def consulterUser(self):
        if  self.authentified:
            try:
                return adminModel.Modeladmin.consulterClients()
            except Exception as e:
                    print("Error Type:", type(e).__name__)
                    traceback.print_exc()

    
# test dial athentification admin (maykhdmouch les fonctions ila makanch username=admin and password=admin)
# admin=Admin()
# # admin.authentifier("admin","admin")
# print(admin.consulterReservation())


#admin.authentifier("admin","admin")

# v=voiture.voiture("marque","modele","typeCarburant",8,69,700,True,"image.png")
# admin.ajouterVoiture(v)
# admin=Admin()
# admin.supprimerVoiture(44)

#clt=Client("hi","hi",9998888,"hi","hi","hi",29292)
#admin=Admin()
#admin.authentifier("admin","admin")
#admin.ajouterClient(clt)
# admin=Admin()
# c=admin.consulterUser()
# print(c)

