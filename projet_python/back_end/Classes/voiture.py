import Model.modelVoiture as voiture
class voiture:
    marque=''
    modele=''
    image=''
    type_carburant=''
    nb_Places=''
    transmission=''
    prix_location_jr=''
    disponibilite=True


    def __init__(self,marque=None,modele=None,image=None,type_carburant=None,nb_Places=None,transmission=None,prix_location_jr=None,disponibilite=True):  

        self.marque=marque
        self.modele=modele
        self.image=image
        self.type_carburant=type_carburant
        self.nb_Places=nb_Places
        self.transmission=transmission
        self.prix_location_jr=prix_location_jr,
        self.disponibilite=disponibilite

    
    def ajouterVoiture(self):
        return voiture.voitureModel.ajouter(self.username,self.email,self.pwd)
    
    def modifierVoiture(self,id):
        return voiture.voitureModel.modifier(id,self.username,self.email,self.pwd)
    
    # def supprimerUser(id):
    #     return voiture.voitureModel.supprimer(id)
    
    # def afficherUser():
    #     return voiture.voitureModel.affichage()

    # def authentifierUser(self,id):
    #     return voiture.voitureModel.authentifier(id,self.username,self.pwd)
    
