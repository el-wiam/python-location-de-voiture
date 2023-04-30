import connexion
class utilisateurModel:
    id
    username=''
    email=''
    pwd=''
    def __init__(self) -> None:
        pass

    def creer(username,email,pwd):
        try :
            sql=("INSERT INTO utilisateur (username,email,password) VALUES (%s,%s,%s)")
            values=(username,email,pwd)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except:
             print("erreur de creation")

    def modifier(id,username,email,pwd):
            try :
                sql="UPDATE utilisateur set username = (%s),email = (%s),password = (%s) WHERE id = (%s)"
                values=(username,email,pwd,id)
                connexion.db.execute(sql,values)
                connexion.conn.commit()
                print("la description bien change")
            except:
                 print("erreur de modification")

    def supprimer(id):
        try :
            sql="DELETE FROM utilisateur WHERE id = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression valide")
        except:
            print('erreur de suppression!!!')
    

    def affichage():
        connexion.db.execute("select * from utilisateur")
        users= connexion.db.fetchall()
        for user in users:
            print(user)
