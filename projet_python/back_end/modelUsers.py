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
            sql=("INSERT INTO user (username,email,password) VALUES (%s,%s,%s)")
            values=(username,email,pwd)
            connexion.db.execute(sql,values)
            connexion.conn.commit()
        except:
             print("erreur de creation")

    def modifier(id,username,email,pwd):
            try :
                sql="UPDATE user set username = (%s),email = (%s),password = (%s) WHERE id = (%s)"
                values=(username,email,pwd,id)
                connexion.db.execute(sql,values)
                connexion.conn.commit()
                print("la description bien change")
            except:
                 print("erreur de modification")

    def supprimer(id):
        try :
            sql="DELETE FROM user WHERE id = %s"
            connexion.db.execute(sql,(id,))
            connexion.conn.commit()
            print("suppression valide")
        except:
            print('erreur de suppression!!!')
    

    def affichage():
        connexion.db.execute("select * from user")
        users= connexion.db.fetchall()
        for user in users:
            print(user)

    
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

