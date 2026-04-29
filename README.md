**Finance Tracker**

**Overview**  
This project is a personal finance tracking application developed in Python to help users monitor their income, expenses, and overall financial balance. The system was designed to provide a simple and structured way to understand spending habits and improve money management.

The application uses object-oriented programming principles and a modular design to ensure clarity, scalability, and maintainability.

**Features**  
- Add income and expense transactions  
- Categorise transactions  
- View all transactions  
- Generate financial summaries (income, expenses, balance)  
- View expenses grouped by category  
- Remove the most recent transaction  
- Input validation for reliable data handling  

**Project Structure**  
- main.py – Handles user interaction and program flow  
- tracker.py – Core logic for managing transactions  
- models.py – Data structures such as the Transaction class  
- commands.py – Implements the command pattern for actions  
- test_tracker.py – Unit tests using pytest  

**Design Approach**  
The system was built using object-oriented programming, where classes are used to organise data and behaviour logically. The command pattern was implemented to separate user actions from the core logic, improving flexibility and making the system easier to extend. A modular design was used so that each file has a clear responsibility, improving maintainability.

**Testing**  
The project includes unit tests written using pytest to verify correct functionality. These tests ensure that transactions are added and removed correctly, financial summaries are accurate, and invalid inputs are properly handled. This improves the reliability of the system.

**Version Control and Change Management**  
This project was developed using Git and GitHub. Changes were tracked using commits, and branches were used to implement updates and fixes without affecting the main version. Pull requests were used to merge changes back into the main branch. This approach allowed all changes to be documented and tracked, making it possible to review or revert previous versions if needed.

**Future Improvements**  
- Add file saving and loading for persistent data  
- Develop a graphical user interface  
- Add budgeting and financial goal tracking  
- Include data visualisation such as charts  

**Author**  
Michael Velissariou  
University of Bath  

**Repository**  
https://github.com/mikevelissariou/financetracker
