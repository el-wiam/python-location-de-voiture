import connexion
import modelVoiture as vtrmodel
class voiture:
    marque=''
    modele=''
    image=''
    type_carburant=''
    nb_places=''
    transmission=''
    prix_location=''
    disponibilite=True


    def __init__(self,marque=None,modele=None,image=None,type_carburant=None,nb_places=None,transmission=None,prix_location=None,disponibilite=True):  

        self.marque=marque
        self.modele=modele
        self.image=image
        self.type_carburant=type_carburant
        self.nb_places=nb_places
        self.transmission=transmission
        self.prix_location=prix_location
        self.disponibilite=disponibilite

    
    def ajouterVoiture(self):
        return vtrmodel.voitureModel.ajouter( self.marque,self.modele,self.image,self.type_carburant,self.nb_places,self.transmission,self.prix_location,self.disponibilite)
    
    def modifierVoiture(self,id):
        return vtrmodel.voitureModel.modifier(id,self.marque,self.modele,self.image,self.type_carburant,self.nb_places,self.transmission,self.prix_location,self.disponibilite)
    
    # def supprimerUser(id):
    #     return voiture.voitureModel.supprimer(id)
    
    # def afficherUser():
    #     return voiture.voitureModel.affichage()

    # def authentifierUser(self,id):
    #     return voiture.voitureModel.authentifier(id,self.username,self.pwd)
    
