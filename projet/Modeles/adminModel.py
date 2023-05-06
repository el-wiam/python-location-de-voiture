import sys 
sys.path.append("C:/Users/toshiba/Desktop/pyproject/python-location-de-voiture/projet")
from Modeles import connexion
import traceback

class Modeladmin:
    
    def ajouterV(voiture):
        try:
            sql = "INSERT INTO voiture (marque,modele,type_carburant,nb_places,transmission,prix_location,disponibilité,image) VALUES (%s, %s,%s,%s,%s, %s,%s,%s)"
            values = (voiture.marque,voiture.modele,voiture.typeCarburant,voiture.nbPlaces,voiture.transmission,voiture.prixLocation,voiture.disponibilité,voiture.image)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            print("La voiture a été ajoutée avec succès.")
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifierV(voiture,id):
        try :
            sql="UPDATE voiture set marque = (%s),modele = (%s),type_carburant=(%s),nb_places=(%s),transmission=(%s),prix_location=(%s),disponibilité=(%s),image=(%s) WHERE id_voiture = (%s)"
            # pic=self.convertToBinary('images/{self.image}')
            values=(voiture.marque,voiture.matricule,voiture.typeCarburant,voiture.nbPlaces,voiture.transmission,voiture.prixLocation,voiture.disponibilité,voiture.image,id)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
            print("la voiture bien change")
        except Exception as e:
                print("Error Type:", type(e).__name__)
        
    
    def supprimerV(id):
        try :
            sql="DELETE FROM voiture WHERE id_voiture = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression voiture valide")
        except:
            print('erreur de suppression voiture !!!')

# ====================================================================================================================================
# ====================================================================================================================================

    # CLIENT
    def ajouterClt(client):
        try:
            sql = "INSERT INTO user (nom_complet,cin,num_tel,username,password,email,num_permis) VALUES (%s, %s,%s,%s,%s, %s,%s)"
            values = (client.nomComplet,client.cin,client.numTel,client.username,client.password,client.email,client.numPermis)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            print("Le client a été ajoutée avec succès.")
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifierV(client,id):
        try :
            sql="UPDATE user set nom_complet=(%s), cin=(%s), num_tel=(%s), username=(%s), password=(%s), email=(%s), num_permis=(%s) WHERE id = (%s)"
            # pic=self.convertToBinary('images/{self.image}')
            values=(client.nomComplet,client.cin,client.numTel,client.username,client.password,client.email,client.numPermis,id)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
            print("le client bien change")
        except Exception as e:
                print("Error Type:", type(e).__name__)
        
    
    def supprimerV(id):
        try :
            sql="DELETE FROM user WHERE id = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression du client valide")
        except:
            print('erreur de suppression client !!!')

    def consulterReservation():
        try:
            sql = "SELECT * FROM reservation"
            connexion.db.execute(sql)
            reservations = connexion.db.fetchall()
            return reservations
        except Exception as e:
            print("Error Type:", type(e).__name__)
    

    def consulterClients():
        try:
            sql = "SELECT * FROM user"
            connexion.db.execute(sql)
            clients = connexion.db.fetchall()
            return clients
        except Exception as e:
            print("Error Type:", type(e).__name__)
 