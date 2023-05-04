
import modelVoiture
import modelClient
import modelReservation

class reservation:
    def __init__(self, voiture_id, client_id, date_debut, date_fin):
        self.voiture_id = voiture_id
        self.client_id = client_id
        self.date_debut = date_debut
        self.date_fin = date_fin

    def reserver_voiture(self):
        reservation_model = modelReservation.ReservationModel(
            self.voiture_id, self.client_id, self.date_debut, self.date_fin
        )
        return reservation_model.reserver_voiture()

    def consulter_reservation(self, reservation_id):
        return modelReservation.ReservationModel.consulter_reservation(reservation_id)

    def annuler_reservation(self, reservation_id):
        return modelReservation.ReservationModel.annuler_reservation(reservation_id)

    def modifier_reservation(self, reservation_id, nouvelle_date_debut, nouvelle_date_fin):
        return modelReservation.ReservationModel.modifier_reservation(
            reservation_id, nouvelle_date_debut, nouvelle_date_fin
        )

    def consulter_client(self, client_id):
        return modelClient.ClientModel.consulter_client(client_id)

    def consulter_voiture(self, voiture_id):
        return modelVoiture.VoitureModel.consulter_voiture(voiture_id)
