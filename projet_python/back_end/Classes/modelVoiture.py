import connexion
import itertools
import traceback
class VoitureModel:

    id = itertools.count()

    marque=''
    modele=''
    type_carburant=''
    nb_places=0
    transmission=0
    prix_location=0
    disponibilité=True
    image=''
    def __init__(self,marque,modele,type_carburant,nb_places,transmission,prix_location,disponibilité,image):
        self.id = next(VoitureModel.id)

        self.marque=marque
        self.modele=modele
        self.type_carburant=type_carburant
        self.nb_places=nb_places
        self.transmission=transmission
        self.prix_location=prix_location
        self.disponibilité=disponibilité
        self.image=image

    def convertToBinary(self, image_path):
        with open(image_path, 'rb') as image_file:
            binary_data = image_file.read()
        return binary_data

    def creer_voiture(self):
        try:
            sql = "INSERT INTO voiture (marque, modele, type_carburant, nb_places, transmission, prix_location, disponibilité, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            pic = self.convertToBinary(f'images/{self.image}')
            values = (self.marque, self.modele, self.type_carburant, self.nb_places, self.transmission, self.prix_location, self.disponibilité, pic)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifier_voiture(self,id):
        try :
            sql="UPDATE voiture set marque = (%s),modele = (%s),type_carburant = (%s),nb_places = (%s),transmission = (%s),prix_location = (%s) ,disponibilité = (%s) WHERE id = (%s)"
            pic=self.convertToBinary('images/{self.image}')
            values=(self.marque,self.modele,self.type_carburant,self.nb_places,self.transmission,self.prix_location,self.disponibilité,pic,id)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
            print("la description bien change")
        except:
                print("erreur de modification")

    def supprimer_voiture(id):
        try :
            sql="DELETE FROM voiture WHERE id = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression voiture valide")
        except:
            print('erreur de suppression voiture !!!')
