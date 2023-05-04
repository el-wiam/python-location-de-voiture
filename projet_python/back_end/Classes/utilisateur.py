import modelUsers as model
import itertools

class users:
    def __init__(self) -> None:
        pass
    
    def afficherUser(self):
        return model.utilisateurModel.affichage()

    def authentifierUser(self,id,username,pwd):
        return model.utilisateurModel.authentifier(id,username,pwd)
    
