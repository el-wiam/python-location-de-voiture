import connexion
import modelUsers
import modelReservation
class ClientModel(modelUsers.utilisateurModel):
    num_permis=0

    def __init__(self,nom_complet,cin,num_tel,username,password,email,num_permis):
        modelUsers.utilisateurModel(self,nom_complet,cin,num_tel,username,password,email)
        self.num_permis=num_permis


    def creer_client(self):
        try :
            sql=("INSERT INTO user (nom_complet,cin,num_tel,username,password,email,num_permis) VALUES (%s,%s,%s,%s,%s,%s,%s)")
            values=(self.nom_complet,self.cin,self.num_tel,self.username,self.password,self.email,self.num_permis)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except Exception as e:
                print("Error Type:", type(e).__name__)

    def modifier_client(id,self):
        try :
            sql="UPDATE user set nom_complet = (%s),cin = (%s),num_tel = (%s),username = (%s),password = (%s),email = (%s) ,num_permis = (%s) WHERE id = (%s)"
            values=(self.nom_complet,self.cin,self.num_tel,self.username,self.password,self.email,self.num_permis,id)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
            print("la description bien change")
        except Exception as e:
                print("Error Type:", type(e).__name__)

    def supprimer_client(self,id):
        try :
            sql="DELETE FROM user WHERE id = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression client valide")
        except:
            print('erreur de suppression client !!!')


    def consulter_clients():
        try:
            sql = "SELECT * FROM client"
            connexion.db.execute(sql)
            clients = connexion.db.fetchall()
            return clients
        except Exception as e:
            print("Error Type:", type(e).__name__)
            return []
    

    
    def reserver_voiture(self, voiture_id, date_debut, date_fin):
        reservation_model = modelReservation.ReservationModel(
            voiture_id=voiture_id,
            client_id=self.id,
            date_debut=date_debut,
            date_fin=date_fin
        )
        return reservation_model.reserver_voiture()
    
    def annuler_reservation(self, reservation_id):
        return modelReservation.ReservationModel.annuler_reservation(reservation_id)

    def modifier_reservation(self, reservation_id, nouvelle_date_debut, nouvelle_date_fin):
        return modelReservation.ReservationModel.modifier_reservation(reservation_id, nouvelle_date_debut, nouvelle_date_fin)



        