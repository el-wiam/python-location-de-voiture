
import modelAdmin as ad
import voiture as voiture

class Admin:

    def __init__(self) -> None:
        pass

    def ajouter_voiture(self,voiture):
        return ad.voitureModel.ajouter(voiture)

#     def creerUser(self):
#         return admin.modelAdmin.creerClient(self.username,self.email,self.pwd)
    
#     def modifierUser(self,id):
#         return admin.modelAdmin.modifierClient(id,self.username,self.email,self.pwd)
    
#     def supprimerUser(self,id):
#         return admin.modelAdmin.supprimerClient(id)
    
#     def afficherUser(self):
#         return admin.modelAdmin.affichageClient()
    
#     def ajouter_voiture(self):
#         return admin.modelAdmin.creerVoiture(self.marque,self.modele,self.type_carburant,self.nb_places,self.transmission,self.prix_location,self.disponibilité,self.image)

#     def modifier_voiture():
#         return True
    
#     def supprimer_voiture(id):
#         return admin.modelAdmin.creerVoiture(id)
    
    
#     def consulter_reservation():
#         return True
    
#     def consulter_client():
#         return True
    
#     def consulter_voiture():
#         return True