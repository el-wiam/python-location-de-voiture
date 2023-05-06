import itertools
from ..Modeles import userModel 
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
            return userModel.UserModel.authentifierUser(username,password)
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

    def consulterVoiture(self):
        try:
            return userModel.UserModel.consulterV()
        except Exception as e:
                print("Error Type:", type(e).__name__)
                traceback.print_exc()

u=utilisateur()
# u.authentifier("migo","safaabatrahi123")
# print(u.consulterVoiture())
