import traceback
from .users import * 
from ..Modeles.clientModel import * 


class Client(utilisateur):
    def __init__(self,nomComplet='',cin='',numTel='',username='',password='',email='',numPermis=''):
        utilisateur.__init__(self,nomComplet,cin,numTel,username,password,email,numPermis)
    
    def reserver_voiture(self,voiture_id, date_debut, date_fin):
        try:
            return ClientModel.reserver_voiture(voiture_id, date_debut, date_fin,self.id)
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def annuler_reservation(self,id):
        try:
            return ClientModel.annulerReservation(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifier_reservation(self,id):
        try:
            return ClientModel.modifierReservation(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def consulter_reservation(self):
        try:
            return clientModel.ClientModel.consulter_reservation(self.id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()



#c=Client()
#c.authentifier("migo","safaabatrahi123")
#c.annuler_reservation(3)
#voiture = c.rechercher_voiture("mercedes")
#print(voiture)