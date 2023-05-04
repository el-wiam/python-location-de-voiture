import connexion
import traceback

class ReservationModel:
    def __init__(self, voiture_id, client_id, date_debut, date_fin):
        self.voiture_id = voiture_id
        self.client_id = client_id
        self.date_debut = date_debut
        self.date_fin = date_fin

    def reserver_voiture(self):
        try:
            sql = "INSERT INTO reservation (voiture_id, client_id, date_debut, date_fin) VALUES (%s, %s, %s, %s)"
            values = (self.voiture_id, self.client_id, self.date_debut, self.date_fin)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            return "Voiture reserved successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()
            return "Error occurred while reserving the voiture."


    def annuler_reservation(self):
        try:
            sql = "DELETE FROM reservation WHERE voiture_id = %s AND client_id = %s"
            values = (self.voiture_id, self.client_id)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            return "Reservation canceled successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()

    def modifier_reservation(self, new_date_debut, new_date_fin):
        try:
            sql = "UPDATE reservation SET date_debut = %s, date_fin = %s WHERE voiture_id = %s AND client_id = %s"
            values = (new_date_debut, new_date_fin, self.voiture_id, self.client_id)
            connexion.db.execute(sql, values)
            connexion.conn.commit()
            return "Reservation modified successfully!"
        except Exception as e:
            print("Error Type:", type(e).__name__)
            traceback.print_exc()


