import itertools
import userModel
import traceback

class utilisateur:
    id = itertools.count()
    nomComplet=''
    cin=''
    numTel=0
    username=''
    password=''
    email=''
    numPermis=0

    def __init__(self,nomComplet='',cin='',numTel='',username='',password='',email='',numPermis='') :
        self.id = next(utilisateur.id)
        self.nomComplet=nomComplet
        self.cin=cin
        self.numTel=numTel
        self.username=username
        self.password=password
        self.email=email
        self.numPermis=numPermis
    
    def authentifier(self,username, password):
        try:
            self.id = userModel.UserModel.authentifierUser(username,password)
            return id
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def consulterVoiture(self):
        try:
            return userModel.UserModel.consulterV()
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()



