import sys 
sys.path.append("C:/Users/toshiba/Desktop/pyproject/python-location-de-voiture/projet")
from Modeles import connexion
import traceback

class ClientModel:
    def reserver_voiture(nomc,num,cin,permis,voiture,dated,datef):
        try:
            sql = "INSERT INTO reservation (nom_complet,num_tel,cin,numero_permis,voiture,datedebut,datefin) VALUES ( %s, %s, %s,%s, %s, %s, %s)"
            values = (nomc,num,cin,permis,voiture,dated,datef)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            return "Voiture reserved successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
            return "Error occurred while reserving the voiture."


    def annulerReservation(id):
        try:
            sql="DELETE FROM reservation WHERE id_res = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            return "Reservation canceled successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
        

    def modifier_reservation(self, new_date_debut, new_date_fin,username,):
        try:
            sql = "UPDATE reservation SET date_debut = %s, date_fin = %s WHERE id_v = %s AND id_c = %s"
            values = (new_date_debut, new_date_fin, self.voiture_id, self.client_id)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            return "Reservation modified successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def consulter_reservation(client_id):
        try:
            sql = "SELECT * FROM reservation WHERE id_c = %s"
            values = (client_id,)
            connexion.db.execute(sql, values)
            result = connexion.db.fetchall()
            return result
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
