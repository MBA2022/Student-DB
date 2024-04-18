# Student Database using MongoDB and Python

This Python script provides a simple command-line interface for managing a student database using MongoDB. Users can add, view, delete, and update student records.

## Requirements:


- Python 3.x
- pymongo library (pip install pymongo)
- dateutil library (pip install python-dateutil)
- pandas library (pip install pandas)
- A MongoDB Atlas account and database (refer to MongoDB documentation for setup instructions)
## Installation:
1. PyMongo has a set of packages for Python MongoDB interaction. For the following tutorial, start by creating a 
virtual environment, and activate it.

```bash
python -m venv env
```
`source env/bin/activate`

2. Clone this repository.

3. Install the required libraries using .

```bash
pip install pymongo python-dateutil pandas
```
4. Replace `mongodb+srv://<username>:<password>@cluster0.mongodb.net/` in get_database() with your actual MongoDB Atlas connection string.

## Usage:
Run the script using `python student_database.py`.
The script will present a menu for adding, viewing, deleting, or updating students.
Follow the prompts to enter student information or names for specific actions.

### Example:
```
Welcome to Student Database!
1. Add Student
2. View Students
3. Delete Student
4. Update Student
5. Exit
Enter your choice: 1

Enter the following details:
Name: John Doe
Major: Computer Science
University: Any University
Department: Information Systems
GPA: 3.8

Successfully inserted!

Press 1 to continue or press 0 to exit
Enter your choice: 2

Enter the name of the student: John Doe

        name   major      university        department        gpa
      John Doe  CS     Any University  Information Systems  3.800000
```
**The data will be saved as a collection on MongoDB server**
## Contributing:

Feel free to submit pull requests with improvements or bug fixes.
