import connexion
class UserModel:
    def authentifierUser(username,password):
        try:
            sql = "SELECT id, username, password FROM user WHERE username= (%s) AND password = (%s)"
            values = (username, password)
            connexion.db.execute(sql, values)
            result = connexion.db.fetchone()
            if result:
                print("Username et password sont correct")
                return result[0]
            else:
                print("Identifiants incorrects")
        except Exception as e:
            print("Erreur lors de l'authentification :", e)
    
    def consulterV():
        try:
            sql = "SELECT * FROM voiture"
            connexion.db.execute(sql)
            voitures = connexion.db.fetchall()
            return voitures
        except Exception as e:
            print("Error Type:", type(e).__name__)



