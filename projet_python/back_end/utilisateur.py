import connexion
import modelUsers as model
class users:
    username=''
    email=''
    pwd=''

    def __init__(self,username=None,pwd=None,email=None):  
        self.username=username
        self.pwd=pwd
        self.email=email
    
    def creerUser(self):
        return model.utilisateurModel.creer(self.username,self.email,self.pwd)
    
    def modifierUser(self,id):
        return model.utilisateurModel.modifier(id,self.username,self.email,self.pwd)
    
    def supprimerUser(self,id):
        return model.utilisateurModel.supprimer(id)
    
    def afficherUser(self):
        return model.utilisateurModel.affichage()

    def authentifierUser(self,id,username,pwd):
        return model.utilisateurModel.authentifier(id,username,pwd)
    
