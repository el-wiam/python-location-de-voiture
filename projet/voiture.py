import itertools

class voiture:
    id_voiture = itertools.count()
    marque=''
    modele=''
    typeCarburant=''
    nbPlaces=0
    transmission=0
    prixLocation=0
    disponibilité=True
    image=''

    def __init__(self,marque,modele,typeCarburant,nbPlaces,transmission,prixLocation,disponibilité,image):
        self.id = next(voiture.id_voiture)
        self.marque=marque
        self.modele=modele
        self.typeCarburant=typeCarburant
        self.nbPlaces=nbPlaces
        self.transmission=transmission
        self.prixLocation=prixLocation
        self.disponibilité=disponibilité
        self.image=image
    
    # GETTER
    def get_marque(self):   
        return self._marque   
    
    def get_modele(self):
        return self._modele
    
    def get_typeCarburant(self):
        return self._typeCarburant
    
    def get_typeCarburant(self):
        return self._typeCarburant
    
    def get_nbPlaces(self):
        return self._nbPlaces
    
    def get_transmission(self):
        return self._transmission
    
    def get_prixLocation(self):
        return self._prixLocation
    
    def get_disponibilité(self):
        return self._disponibilité
    
    def get_image(self):
        return self._image
    
    # SETTER
    def set_marque(self, marque):   
        self._marque = marque  

    def set_modele(self, modele):   
        self._modele = modele
    
    def set_typeCarburant(self, typeCarburant):   
        self._typeCarburant = typeCarburant  

    def set_nbPlaces(self, nbPlaces):   
        self._nbPlaces = nbPlaces

    def set_transmission(self, transmission):   
        self._transmission = transmission  

    def set_prixLocation(self, prixLocation):   
        self._prixLocation = prixLocation
    
    def set_disponibilité(self, disponibilité):   
        self._disponibilité = disponibilité  

    def set_image(self, image):   
        self._image = image

    # AFFICHAGE