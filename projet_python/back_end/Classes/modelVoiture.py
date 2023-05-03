import connexion

class voitureModel:

    def __init__(self) -> None:
        pass

    def ajouter(marque,modele,image,type_carburant,nb_places,transmission,prix_location,disponibilite):
        try :
            sql=("INSERT INTO voiture (marque,modele,image,type_carburant,nb_places,transmission,prix_location,disponibilité) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
            values=(marque,modele,image,type_carburant,nb_places,transmission,prix_location,disponibilite)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except:
             print("erreur d ajout")



        