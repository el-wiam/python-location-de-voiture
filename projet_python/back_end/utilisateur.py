import Model.modelUsers as model
import hashlib
class users:
    username=''
    email=''
    pwd=''
    hashed_password = hashlib.sha256(pwd.encode()).hexdigest()

    # def __init__(self):      
    #     self.username=""
    #     self.email=""
    #     self.pwd=""

    def __init__(self,username,email, hashed_password ):  
        self.username=username
        self.email=email
        self.pwd= hashed_password 
    
    def creerUser(self):
        return model.utilisateurModel.creer(self.username,self.email,self.pwd)
    
    def modifierUser(self,id):
        return model.utilisateurModel.modifier(id,self.username,self.email,self.pwd)
    
    def supprimerUser(id):
        return model.utilisateurModel.supprimer(id)
    
    def afficherUser():
        return model.utilisateurModel.affichage()

    
    # def modifier(self,id,username,email,password):
    #     connexion.db.execute("select * from utilisateur")
    #     users= connexion.db.fetchall()
    #     for user in users : 
    #         if user["id"] == id :
    #             sql="UPDATE taches set username = (%s),email = (%s),password = (%s)"
    #             values=(username,email,password)
    #             connexion.db.execute(sql,values)
    #             connexion.conn.commit()
    #             return print("la description bien change")
            
    # def suppresion(self,id_sup):
    #     global id
    #     connexion.db.execute("select * from utilisateur")
    #     users= connexion.db.fetchall()
    #     for user in users:
    #         if user["id"]==id_sup:
    #             users.remove(user)
    #             return
    #         else: print("ERREUR")

    # def affichage():
    #     connexion.db.execute("select * from utilisateur")
    #     users= connexion.db.fetchall()
    #     for user in users:
    #         print(user)
    
    # def connexion(self,username,email,pwd):
    #     connexion.db.execute("select * from utilisateur")
    #     users= connexion.db.fetchall()
    #     for user in users:
    #         if username == user[1] and pwd ==user[3]:
    #             import menu
    #             quit()
    #         else:
    #             self.creerUser(username,email,pwd)