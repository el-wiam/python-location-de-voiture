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
    

    # def reserver_voiture():
    #     return True
    
    # def annuler_reservation():
    #     return True
    
    # def modifier_reservation():
    #     return True