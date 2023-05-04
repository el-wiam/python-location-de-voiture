import modelClient
import modelVoiture  
class Voiture:

    def __init__(self) -> None:
        pass

    def creer(self):
        voiture_model = modelVoiture.VoitureModel(
            marque='',
            modele='',
            type_carburant='',
            nb_places=0,
            transmission=0,
            prix_location=0,
            disponibilité=True,
            image=''
        )
        return voiture_model.creer_voiture()

    def modifier(self):
        return modelVoiture.VoitureModel.modifier_voiture(self)
    
    def supprimer(self,id):
        return modelVoiture.VoitureModel.supprimer_voiture(self,id)
    
    # client
    
    def creerClt(self):
        return modelClient.ClientModel.creer_client(self)
    
    def modifierClt(self,id):
        return modelClient.ClientModel.modifier_client(self)
    
    def supprimerClt(self,id):
        return modelClient.ClientModel.supprimer_client(self,id)

voiture_instance = Voiture()
voiture_instance.creer()
