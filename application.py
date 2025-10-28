# Name: Max Sobota

#import psycopg2 # The library which allows connecting to PostgreSQL databases
from datetime import datetime # Allows entering date objects

CHAR_LIMIT = 255

def start_application():
    database = "???"
    host = "???"
    user = "???"
    password = "???"
    port = "5432"

    #connection = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)

    #cursor = connection.cursor() # Create a new cursor to interact with the PostgreSQL database

    #cursor.execute("SELECT * FROM DB_table WHERE id = 1")

    #print(cursor.fetchall()) # Test output

    while(True): # Necessary or not???
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete student record")
        option = input("Enter choice: ")

        try:
            option = int(option)
        except ValueError:
            print("Incorrect input.")

        if option == 1:
            getAllStudents()
        elif option == 2:
            first_name = input("Enter first name")
            first_name = first_name[:CHAR_LIMIT] if len(first_name) > CHAR_LIMIT else first_name # Reducing to 255 characters

            last_name = input("Enter last name")
            last_name = last_name[:CHAR_LIMIT] if len(last_name) > CHAR_LIMIT else last_name

            email = input("Enter email")
            email = email[:CHAR_LIMIT] if len(email) > CHAR_LIMIT else email

            enrollment_date = datetime.now() # Change this later

            addStudent(first_name, last_name, email, enrollment_date)

def getAllStudents():
    """
    Retrieves and displays all records from the students table.
    """
    pass

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Adds the given data to a new row, then inserts the row into the students table.

    Arguments:
        first_name:
        last_name:
        email:
        enrollment_date: A datetime object?
    """
    pass

def updateStudentEmail(student_id, new_email):
    """
    Updates the email address for a student with the specified student_id.

    Arguments:
        student_id: int
        new_email: String
    """
    pass

def deleteStudent(student_id):
    """
    Deletes the record of the student with the specified student_id

    Arguments:
        student_id: int
    """
    pass

if __name__ == "__main__":
    start_application()