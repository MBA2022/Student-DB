from pymongo import MongoClient
from dateutil import parser
from pandas import DataFrame
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster0.jthrfng.mongodb.net/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Student-DB']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()


#############################################################################

class std:
    def __init__(self, name,  major,university, department, gpa):
        expiry_date = '2021-07-13T00:00:00.000Z'
        expiry = parser.parse(expiry_date)
        self.name = name
        self.major = major
        self.university = university
        self.department = department
        self.gpa = gpa

    def  add_student(self):
        collection_name = dbname[self.name]
        Student = {
            "name": self.name,
            "major": self.major,
            "university": self.university,
            "department": self.department,
            "gpa": self.gpa
        }
        collection_name.insert_one(Student)
        print("Successfully inserted!")


def add_student():
   print("Enter the following details:")
   name = input("Name: ")
   major = input("Major: ")
   university = input("University: ")
   department = input("Department: ")
   gpa = input("GPA: ")
   student = std(name, major,university, department, gpa)
   student.add_student()



def view_students():
    name = input("Enter the name of the student: ")
    collection_name = dbname[name]
    item_details = collection_name.find()
    items_df = DataFrame(item_details)
    # see the magic
    print(items_df)


def delete_student():
    name = input("Enter the name of the student: ")
    collection_name = dbname[name]
    collection_name.drop()
    print("Successfully deleted!")

def update_student():
    name = input("Enter the name of the student: ")
    collection_name = dbname[name]
    print("Enter the Edited details:")
    major = input("Major: ")
    university = input("University: ")
    department = input("Department: ")
    gpa = input("GPA: ")
    
    collection_name.update_one({"name": name}, {"$set": {"major": major, "university": university,"department": department,"gpa": gpa }})
    print("Successfully updated!")

print("Welcome to Student Database!")
print("1. Add Student")
print("2. View Students")
print("3. Delete Student")
print("4. Update Student")
print("5. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    add_student()
    print("Press 1 to continue or press 0 to exit")
    choice = int(input("Enter your choice: "))
    while choice == 1:
        add_student()
        print("Press 1 to continue or press 0 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break

elif choice == 2:
    view_students()
    print("Press 1 to continue or press 0 to exit")
    choice = int(input("Enter your choice: "))
    while choice == 1:
        view_students()
        print("Press 1 to continue or press 0 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break

elif choice == 3:
    delete_student()
    print("Press 1 to continue or press 0 to exit")
    choice = int(input("Enter your choice: "))
    while choice == 1:
        delete_student()
        print("Press 1 to continue or press 0 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break

elif choice == 4:
    update_student()
    print("Press 1 to continue or press 0 to exit")
    choice = int(input("Enter your choice: "))
    while choice == 1:
        update_student()
        print("Press 1 to continue or press 0 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break

else:
    print("Exiting...")
    exit()
