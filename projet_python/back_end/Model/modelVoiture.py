import connexion

class voitureModel:
    marque=''
    modele=''
    image=''
    type_carburant=''
    nb_Places=''
    transmission=''
    prix_location_jr=''
    disponibilite=True

    def __init__(self) -> None:
        pass

    def ajouter(marque,modele,image,type_carburant,nb_Places,transmission,prix_location_jr,disponibilite):
        try :
            sql=("INSERT INTO voiture (marque,modele,image,type_carburant,nb_Places,transmission,prix_location_jr,disponibilite) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
            values=(marque,modele,image,type_carburant,nb_Places,transmission,prix_location_jr,disponibilite)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except:
             print("erreur d ajout")


    def modifier():
        