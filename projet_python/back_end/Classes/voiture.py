import modelClient
import modelVoiture  
class Voiture:

    def __init__(self) -> None:
        pass

    def creer(self):
        return modelVoiture.VoitureModel.creer_voiture(self)
    
    def modifier(self):
        return modelVoiture.VoitureModel.modifier_voiture(self)
    
    def supprimer(self,id):
        return modelVoiture.VoitureModel.supprimer_voiture(self,id)
    
    # client
    
    def creerClt(self):
        return modelClient.ClientModel.creer_client(self)
    
    def modifierClt(self,id):
        return modelClient.ClientModel.modifier_client(self,id)
    
    def supprimerClt(self,id):
        return modelClient.ClientModel.supprimer_client(self,id)