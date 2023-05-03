import connexion
import itertools

class ClientModel:
    id = itertools.count()

    nom_complet=''
    cin=''
    num_tel=0
    username=''
    password=''
    email=''
    num_permis=0

    def __init__(self,nom_complet,cin,num_tel,username,password,email,num_permis):
        self.id = next(ClientModel.id)

        self.nom_complet=nom_complet
        self.cin=cin
        self.num_tel=num_tel
        self.username=username
        self.password=password
        self.email=email
        self.num_permis=num_permis


    def creer_client(self):
        try :
            sql=("INSERT INTO user (nom_complet,cin,num_tel,username,password,email,num_permis) VALUES (%s,%s,%s,%s,%s,%s,%s)")
            values=(self.nom_complet,self.cin,self.num_tel,self.username,self.password,self.email,self.num_permis)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except Exception as e:
                print("Error Type:", type(e).__name__)

    def modifier_client(self,id):
        try :
            sql="UPDATE user set nom_complet = (%s),cin = (%s),num_tel = (%s),username = (%s),password = (%s),email = (%s) ,num_permis = (%s) WHERE id = (%s)"
            values=(self.nom_complet,self.cin,self.num_tel,self.username,self.password,self.email,self.num_permis,id)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
            print("la description bien change")
        except:
            print("erreur de modification")

    def supprimer_client(id):
        try :
            sql="DELETE FROM user WHERE id = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression client valide")
        except:
            print('erreur de suppression client !!!')
