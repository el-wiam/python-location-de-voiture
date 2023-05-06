import connexion
class UserModel:
    def authentifierUser(username,password):
        try:
            sql = "SELECT id, username, password FROM user WHERE username= (%s) AND password = (%s)"
            values = (username, password)
            connexion.db.execute(sql, values)
            result = connexion.db.fetchone()
            if result:
                if username == 'admin' and password == 'admin':
                    print("Admin logged in")
                    return -1
                else:
                    print("Username and password are correct")
                    return result[0]
            else:
                print("Incorrect username or password")
        except Exception as e:
            print("Error during authentication:", e)
    
    def consulterV():
        try:
            sql = "SELECT * FROM voiture"
            connexion.db.execute(sql)
            voitures = connexion.db.fetchall()
            return voitures
        except Exception as e:
            print("Error Type:", type(e).__name__)


    def rechercherVoiture(self,critere):
        try:
            sql = "SELECT * FROM voiture WHERE marque LIKE %s OR modele LIKE %s"
            critere = f"%{critere}%"  
            values = (critere, critere)
            connexion.db.execute(sql, values)
            voitures = connexion.db.fetchall()
            return voitures
        except Exception as e:
            print("Error Type:", type(e).__name__)
            return []
            
