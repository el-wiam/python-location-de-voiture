import users
import traceback
import clientModel
class Client(users.utilisateur):
    def __init__(self,nomComplet='',cin='',numTel='',username='',password='',email='',numPermis=''):
        users.utilisateur.__init__(self,nomComplet,cin,numTel,username,password,email,numPermis)
    
    def reserver_voiture(self,voiture_id, date_debut, date_fin):
        try:
            return clientModel.ClientModel.reserver_voiture(voiture_id, date_debut, date_fin,self.id)
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def annuler_reservation(self,id):
        try:
            return clientModel.ClientModel.annulerReservation(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifier_reservation(self,id):
        try:
            return clientModel.ClientModel.modifierReservation(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
c=Client()
# c.annuler_reservation(3)
c.reserver_voiture(66,"2024-09-16","2024-09-18")