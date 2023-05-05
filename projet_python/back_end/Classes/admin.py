import modelVoiture 
import modelAdmin
import modelClient
class admin:
    def __init__(self) -> None:
        pass

    def ajouterVehicule(self,voiture):
        return modelAdmin.modelAdmin.ajouterVoiture(voiture)
    
    def modifierVehicule(self,voiture,id):
        return modelAdmin.modelAdmin.modifierVoiture(voiture,id)
    
    def supprimerVehicule(self,id):
        return modelAdmin.modelAdmin.supprimerVoiture(id)
    
    # client 
    def ajouterUser(self,Client):
        return modelAdmin.modelAdmin.ajouterClient(Client)
    
    def modifierUser(self,Client,id):
        return modelAdmin.modelAdmin.modifierClient(Client,id)
    
    def supprimerUser(self,id):
        return modelAdmin.modelAdmin.supprimerClient(id)

    def consulterReservation(self):
        return modelAdmin.modelAdmin.consulterReservation()

    def consulterUser(self):
        return modelAdmin.modelAdmin.consulterClient()
    
# p1=modelVoiture.VoitureModel("modifier","modifier","modifier",10002,"modifier",20002,True,"modifier.png")
# 
# p2=modelAdmin.modelAdmin("safaa","batrahi")

# p2.ajouterVoiture(p1)

# p2.modifierVoiture(8,p1)
# p2.supprimerVoiture(20)

#test client 

# clt=modelClient.ClientModel("mod","mod",200,"mod","mod","mod",3000)
# ad=modelAdmin.modelAdmin()
# ad.ajouterClient(clt)
# ad.modifierClient(1,clt)
# ad.supprimerClient(1)
# p2.ajouter(p1)

