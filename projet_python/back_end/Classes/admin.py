import modelVoiture 
import modelAdmin
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
    
# p1=m_voiture.Voiturem("wiam","wiam","wiam",10002,"wiam",20002,True,"wiam.png")

# p2=adminModel.Modeladmin("safaa","batrahi")

# p2.ajouter(p1)