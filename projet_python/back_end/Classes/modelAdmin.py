import connexion
import modelUsers
class modelAdmin(modelUsers.utilisateurModel):
    def __init__(self):
        super().__init__()

        # Voiture
    def creerVoiture(self,voiture):
        try :
            sql=("INSERT INTO voiture VALUES (%s)")
            values=(voiture)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except:
                print("erreur de creation voiture")
    # def creerClient(username,email,pwd,nom_complet,cin,num_tel,num_permis):
    #     try :
    #         sql=("INSERT INTO user (username,email,password,nom_complet,cin,num_tel,num_permis) VALUES (%s,%s,%s,%s,%s,%s,%s)")
    #         values=(username,email,pwd,nom_complet,cin,num_tel,num_permis)
    #         connexion.db.execute(sql,values)
    #         connexion.conn.commit()
    #     except:
    #          print("erreur de creation client")

    # def modifierClient(id,username,email,pwd,nom_complet,cin,num_tel,num_permis):
    #         try :
    #             sql="UPDATE user set username = (%s),email = (%s),password = (%s),nom_complet = (%s),cin = (%s),num_tel = (%s) ,num_permis = (%s) WHERE id = (%s)"
    #             values=(username,email,pwd,nom_complet,cin,num_tel,num_permis,id)
    #             connexion.db.execute(sql,values)
    #             connexion.conn.commit()
    #             print("la description bien change")
    #         except:
    #              print("erreur de modification")

    # def supprimerClient(id):
    #     try :
    #         sql="DELETE FROM user WHERE id = %s"
    #         connexion.db.execute(sql,(id,))
    #         connexion.conn.commit()
    #         print("suppression valide")
    #     except:
    #         print('erreur de suppression!!!')
    

    # def affichageClient():
    #     connexion.db.execute("select * from user")
    #     users= connexion.db.fetchall()
    #     for user in users:

            # print(user)

    # # Voiture
    # def creerVoiture(self,voiture):
    #     try :
    #         sql=("INSERT INTO voiture VALUES (%s)")
    #         values=(voiture)
    #         connexion.db.execute(sql,values)
    #         connexion.conn.commit()
    #     except:
    #             print("erreur de creation voiture")
    

    # def modifierClient(id,marque,modele,type_carburant,nb_places,transmission,prix_location,disponibilité,image):
    #     try :
    #         sql="UPDATE user set username = (%s),email = (%s),password = (%s),nom_complet = (%s),cin = (%s),num_tel = (%s) ,num_permis = (%s) WHERE id = (%s)"
    #         values=(marque,modele,type_carburant,nb_places,transmission,prix_location,disponibilité,image)
    #         connexion.db.execute(sql,values)
    #         connexion.conn.commit()
    #         print("la description bien change")
    #     except:
    #             print("erreur de modification")

    # def supprimerVoiture(id):
    #     try :
    #         sql="DELETE FROM voiture WHERE id = %s"
    #         connexion.db.execute(sql,(id,))
    #         connexion.conn.commit()
    #         print("suppression voiture valide")
    #     except:
    #         print('erreur de suppression voiture !!!')