import Model.modelUsers as model
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
    
    def supprimerUser(id):
        return model.utilisateurModel.supprimer(id)
    
    def afficherUser():
        return model.utilisateurModel.affichage()

    def authentifierUser(id,username,pwd):
        return model.utilisateurModel.authentifier(id,username,pwd)
    
