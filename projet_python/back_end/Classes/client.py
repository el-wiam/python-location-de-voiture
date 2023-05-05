import modelClient
class Client:
    def __init__(self) -> None:
        pass

    
    def creer(self):
        return modelClient.ClientModel.creer_client(self)
    
    def modifier(self,id):
        return modelClient.ClientModel.modifier_client(self,id)
    
    def supprimer(self,id):
        return modelClient.ClientModel.supprimer_client(self,id)

    def reserverVoiture(self, voiture_id,date_debut, date_fin):
        return modelClient.ClientModel.reserver_voiture(self, voiture_id,date_debut, date_fin)
    

    def annulerReservation(self, reservation_id):
        return modelClient.ClientModel.annuler_reservation(self, reservation_id)

    def modifierReservation(self, reservation_id, nouvelle_date_debut, nouvelle_date_fin):
        return modelClient.ClientModel.modifier_reservation(self, reservation_id, nouvelle_date_debut, nouvelle_date_fin)

