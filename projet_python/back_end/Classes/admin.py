import modelVoiture 
import modelAdmin
import modelClient
class admin:
    def __init__(self) -> None:
        pass

    def ajouterVehicule(voiture):
        return modelAdmin.modelAdmin.ajouterVoiture(voiture)
    
    def modifierVehicule(voiture,id):
        return modelAdmin.modelAdmin.modifierVoiture(voiture,id)
    
    def supprimerVehicule(id):
        return modelAdmin.modelAdmin.supprimerVoiture(id)
    
    # client 
    def ajouterUser(Client):
        return modelAdmin.modelAdmin.ajouterClient(Client)
    
    def modifierUser(Client,id):
        return modelAdmin.modelAdmin.modifierClient(Client,id)
    
    def supprimerUser(id):
        return modelAdmin.modelAdmin.supprimerClient(id)
    
# p1=modelVoiture.VoitureModel("modifier","modifier","modifier",10002,"modifier",20002,True,"modifier.png")
# 
# p2=modelAdmin.modelAdmin("safaa","batrahi")

# p2.ajouterVoiture(p1)

# p2.modifierVoiture(8,p1)
# p2.supprimerVoiture(20)

#test client 

clt=modelClient.ClientModel("mod","mod",200,"mod","mod","mod",3000)
ad=modelAdmin.modelAdmin()
# ad.ajouterClient(clt)
# ad.modifierClient(1,clt)
# ad.supprimerClient(1)