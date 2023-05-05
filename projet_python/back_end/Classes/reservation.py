import itertools

class Reservation:
    num_res = itertools.count()
    dateDebut=''
    dateFin=''
    def __init__(self,date_debut,date_fin):
        self.id = next(Reservation.num_res)
        self.dateDebut=date_debut
        self.dateFin=date_fin