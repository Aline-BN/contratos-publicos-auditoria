Public Contracts Management System

A desktop application developed in Python using the Tkinter graphical interface and a SQLite database. The system enables the management of administrative contracts, logging of contract-related occurrences, and tracking of responsible inspectors.

Description

This system was created to simplify the oversight and organization of public contracts. Users can register contracts with detailed information, associate occurrences with those contracts, and link them to inspectors, using a relational database with enforced foreign key constraints.

Features

Contracts Module
- Register contracts with number, company, description, value, start and end dates, status, and assigned inspector.
- List all registered contracts with a simplified view.
- Edit contracts by ID.
- Delete contracts by ID.

Occurrences Module
- Register occurrences linked to specific contracts.
- Store type, date, and description of each occurrence.
- List and delete occurrences by contract.

Inspectors Module
- Register inspectors with name and ID.
- List all registered inspectors.
- Delete inspectors by ID.

Database

The database is created automatically upon the first execution of the system.

Technologies Used

- Python 3
- Tkinter (GUI)
- SQLite3 (database)

File Structure

sistema-contratos/
│
├── db.py                  - Database structure and functions
├── interface.py           - Main interface for contract management
├── ocorrencias.py         - Interface for occurrences management
├── interface_fiscais.py   - Interface for inspectors management
├── main.py                - Application entry point
└── README.txt             - Project instructions and details

How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal and run:

   python main.py

Note: this project was originally developed in Portuguese for academic purposes.


Author

Developed by Aline Nascimento  
Computer Science student - CEUB | Public Sector Professional  
Contact: aline.b.nascimento@sempreceub.com


