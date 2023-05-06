import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modeles import userModel

import itertools
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
    authentified= False

    def __init__(self,nomComplet='',cin='',numTel=0,username='',password='',email='',numPermis=0) :
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
            if self.id == -1:
                self.authentified = True
                return id
            else:
                self.authentified = False
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


    def rechercher_voiture(self, critere):
        return userModel.UserModel.rechercherVoiture(self, critere)
    
    def update_password(self,pwd):
            return userModel.UserModel.updatePwd(pwd) 
          
# us=utilisateur().update_password(2,"safaa")