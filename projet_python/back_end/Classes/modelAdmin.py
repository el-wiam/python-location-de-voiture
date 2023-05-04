import modelVoiture
import modelClient
class modelAdmin:
    def __init__(self) -> None:
        pass
    
    def ajouterVoiture(self,voiture):
        try :
            modelVoiture.VoitureModel.creer_voiture(voiture)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            
    def modifierVoiture(self,id,voiture):
        try :
            modelVoiture.VoitureModel.modifier_voiture(voiture)
        except Exception as e:
            print("Error Type:", type(e).__name__)

    def supprimerVoiture(id):
        try :
            modelVoiture.VoitureModel.supprimer_voiture(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            

    # client :
    def ajouterClient(self,client):
        try :
            modelClient.ClientModel.creer_client(client)
        except Exception as e:
            print("Error Type:", type(e).__name__)


    def modifierClient(self,id,client):
        try :
            modelClient.ClientModel.modifier_client(id,client)
        except Exception as e:
            print("Error Type:", type(e).__name__)

    def supprimerClient(self,id):
        try :
            modelClient.ClientModel.supprimer_client(id)
        except Exception as e:
            print("Error Type:", type(e).__name__)
            
        
    def consulter_reservation():
        return True
    
    def consulter_client():
        return True