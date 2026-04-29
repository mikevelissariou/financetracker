# Finance Tracker

## Overview
This project is a personal finance tracking application developed in Python to help users monitor their income, expenses, and overall financial balance. The system was designed to provide a simple, structured way to understand spending habits and improve money management.

The application uses object-oriented programming principles and a modular design to ensure clarity, scalability, and maintainability.

## Features
- Add income and expense transactions  
- Categorise transactions  
- View all transactions  
- Generate financial summaries (income, expenses, balance)  
- View expenses grouped by category  
- Remove the most recent transaction  
- Input validation for reliable data handling  

## Project Structure
The project is divided into multiple modules for better organisation:

- `main.py` → Handles user interaction and program flow  
- `tracker.py` → Core logic for managing transactions  
- `models.py` → Data structures (e.g. Transaction class)  
- `commands.py` → Implements command pattern for actions  
- `test_tracker.py` → Unit tests using pytest  

## Design Approach
The system was built using:

- Object-Oriented Programming (OOP)  
  Classes are used to organise data and behaviour logically.

- Command Pattern  
  User actions (e.g. add/remove transactions) are implemented as commands, improving flexibility and separation of concerns.

- Modular Design  
  Each file has a specific responsibility, making the code easier to maintain and extend.

## Testing
The project includes unit tests written using pytest to verify:

- Correct addition and removal of transactions  
- Accurate calculation of summaries  
- Proper handling of invalid inputs  

All core functionality is tested to ensure reliability.

## Version Control and Change Management
This project was developed using Git and GitHub:

- Changes were tracked using commits  
- Branches were used for implementing updates and fixes  
- Pull requests were used to merge changes into the main branch  
- Version history allows tracking and reverting changes if needed  

## Future Improvements
- Add file saving/loading (persistent storage)  
- Develop a graphical user interface (GUI)  
- Add budgeting and financial goal tracking  
- Include data visualisation (charts/graphs)  

## Author
Michael Velissariou  
University of Bath  

## Repository
https://github.com/mikevelissariou/financetracker
