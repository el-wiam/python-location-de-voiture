from Classes import connexion
import traceback

class ClientModel:
    def reserver_voiture(voiture_id, date_debut, date_fin,id):
        try:
            sql = "INSERT INTO reservation (date_debut, date_fin,id_v,id_c) VALUES (%s, %s, %s, %s)"
            values = (date_debut, date_fin, voiture_id,id)
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
        

    def modifier_reservation(self, new_date_debut, new_date_fin):
        try:
            sql = "UPDATE reservation SET date_debut = %s, date_fin = %s WHERE id_v = %s AND id_c = %s"
            values = (new_date_debut, new_date_fin, self.voiture_id, self.client_id)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            return "Reservation modified successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
