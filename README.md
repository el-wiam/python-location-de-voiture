
# Car Rental System

The Car Rental System is a software application that allows users to manage the rental and reservation of vehicles . It provides functionality for both administrators and clients to perform various operations related to vehicle management and reservation.


## Features

- Administrator Functionality:
  - Add new vehicles to the system.
  - Modify vehicle details such as brand, model, and availability.
  - Remove vehicles from the system.
  - View and manage reservations made by clients.

the admin is able to use these Functionalities with the help of these functions: 

  1. ajouterVoiture(self,voiture): Method to add a new car to the database. It takes a voiture object as input and returns the result of calling the ajouterV method of the adminModel.Modeladmin class.

  2. modifierVoiture(self,voiture,id): Method to modify an existing car in the database. It takes a voiture object and an id as input and returns the result of calling the modifierV method of the adminModel.Modeladmin class.

  3. supprimerVoiture(self,id): Method to delete an existing car from the database. It takes an id as input and returns the result of calling the supprimerV method of the adminModel.Modeladmin class.

  4. ajouterClient(self,client): Method to add a new client to the database. It takes a Client object as input and returns the result of calling the ajouterClt method of the adminModel.Modeladmin class.

  5. modifierClient(self,client,id): Method to modify an existing client in the database. It takes a Client object and an id as input and returns the result of calling the modifierClt method of the adminModel.Modeladmin class.

  6. supprimerClient(self,id): Method to delete an existing client from the database. It takes an id as input and returns the result of calling the supprimerClt method of the adminModel.Modeladmin class.

  7. consulterReservation(self): Method to retrieve all reservations from the database. It returns the result of calling the consulterReservation method of the adminModel.Modeladmin class.

  8. consulterUser(self): Method to retrieve all clients from the database. It returns the result of calling the consulterClients method of the adminModel.Modeladmin class.
- Client Functionality:
  - Create a new client account.
  - Update client information such as name, contact details, and driving license number.
  - Browse available vehicles and their details.
  - Reserve a vehicle for a specific duration.
  - Cancel or modify existing reservations.



   the client is able to use these Functionalities with the help of these functions: 

 1.  reserver_voiture(self,nomc,num,cin,permis,voiture, date_debut, date_fin) - This function takes in parameters nomc, num, cin, permis, voiture, date_debut, and date_fin, and uses them to reserve a car using clientModel.ClientModel.reserver_voiture().

    2. annuler_reservation(self,id) - This function takes in a parameter id and uses it to cancel a reservation using clientModel.ClientModel.annulerReservation(id).

   3. modifier_reservation(self,id) - This function takes in a parameter id and uses it to modify a reservation using clientModel.ClientModel.modifier_reservation(id).

   4. consulter_reservation(self) - This function does not take any parameters and returns the reservation details of the current user using clientModel.ClientModel.consulter_reservation(self.id)
## Technologies Used

The Car Rental System is built using the following technologies:

- Python 3.11.2: The backend programming language used for implementing the system's logic and functionality.
  We separated the models code from the actual classes
- MySQL: The database management system used for storing and retrieving data related to vehicles, clients, and reservations.
- CustomTkinter: The front-end technologies used for creating the user interface of the system.
## Getting Started

Follow these instructions to operate the car rental system on your local computer:

    1. Clone the repository to your local machine.
    2. Install the dependencies , that are specified in the requirements.txt file as being necessary.
    3. Create a MySQL database and specify the connection details in the connexion.py file.
    4. Run the firstinterface application file to start the system.
## Contribution

If you would like to contribute to the Car Rental System, please follow the guidelines below:

- Fork the repository and create a new branch for your feature or bug fix.
- Implement your changes and ensure that the code adheres to the project's coding standards.
- Write appropriate tests to validate the functionality.
- Submit a pull request, describing the changes you have made and providing any necessary information or documentation.
## License



The Car Rental System is open-source software . Feel free to use, modify, and distribute the software as per the terms of the license.
## Contact

For any inquiries or support regarding the Car Rental System, please contact us at [safaabatrahi7@gmail.com] [Elfardwiam@gmail.com] [mohamedamine8el@gmail.com]