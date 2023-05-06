import itertools

class Reservation:
    num_res = itertools.count()
    dateDebut=''
    dateFin=''
    nomc=''
    num=''
    cin=''
    permis=''
    voiture=''
    def __init__(self,nomc,num,cin,permis,voiture, date_debut, date_fin):
        self.id = next(Reservation.num_res)
        self.dateDebut=date_debut
        self.dateFin=date_fin
        self.nomc=nomc
        self.num=num
        self.cin=cin
        self.permis=permis
        self.voiture=voiture