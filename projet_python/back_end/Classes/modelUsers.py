import connexion
import itertools

class utilisateurModel:

    id = itertools.count()

    username=''
    email=''
    pwd=''
    nom_complet=''
    cin=''
    num_tel=''

    def __init__(self,nom_complet,cin,num_tel,username,password,email):
        self.id = next(utilisateurModel.id)
        self.nom_complet=nom_complet
        self.cin=cin
        self.num_tel=num_tel
        self.username=username
        self.password=password
        self.email=email

    def authentifier(id, username, password):
        try:
            sql = "SELECT username, password FROM user WHERE id = (%s) AND username= (%s) AND password = (%s)"
            values = (id, username, password)
            connexion.db.execute(sql, values)
            result = connexion.db.fetchone()
            if result:
                print("Username et password sont correct")
            else:
                print("Identifiants incorrects")
        except Exception as e:
            print("Erreur lors de l'authentification :", e)


    def consulter_voiture():
        return True