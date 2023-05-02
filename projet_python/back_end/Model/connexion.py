import mysql.connector as ms

conn=ms.connect(
    host="localhost",
    user="root",
    password="",
    database="locationvoiture"
)

db=conn.cursor()

# print("connexion reussie a la base de donnees")

# table_exists=db.fetchone()
# if table_exists:
#     print("table existe")

# req_1='''CREATE TABLE utilisateur
# (
#     id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     username VARCHAR(100),
#     email VARCHAR(255),
#     password VARCHAR(255)
# )'''
# db.execute(req_1)
# conn.commit()
# print("La table utilisateur est cree")
# db.execute("CREATE DATABASE projet_python")

# req2='''CREATE TABLE voiture (
#   id INT PRIMARY KEY AUTO_INCREMENT,
#   marque VARCHAR(255) NOT NULL,
#   modele VARCHAR(255) NOT NULL,
#   image VARCHAR(255) NOT NULL,
#   type_carburant VARCHAR(50) NOT NULL,
#   nombre_places INT NOT NULL,
#   transmission BOOLEAN ,
#   prix_location FLOAT NOT NULL,
#   disponibilite BOOLEAN 
# )'''
# db.execute(req2)
# conn.commit()
# print("La table vehicule est cree")


