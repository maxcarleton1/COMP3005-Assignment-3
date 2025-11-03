# Name: Max Sobota

import psycopg2 # The library which allows connecting to PostgreSQL databases

CHAR_LIMIT = 255

database = "assignment3q1"
host = "localhost"
user = "postgres"
password = "password"
port = "5432" # Default port

connection = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)
cursor = connection.cursor()

def start_application():
    while(True):
        print("\n1. Get all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete student record")
        print("5. Exit")
        option = input("Enter choice: ")

        try:
            option = int(option)
        except ValueError:
            print("Incorrect input.")
            continue

        if option == 1:
            getAllStudents()
        elif option == 2:
            first_name = input("Enter first name: ")
            first_name = first_name[:CHAR_LIMIT] if len(first_name) > CHAR_LIMIT else first_name # Reducing to 255 characters

            last_name = input("Enter last name: ")
            last_name = last_name[:CHAR_LIMIT] if len(last_name) > CHAR_LIMIT else last_name

            email = input("Enter email: ")
            email = email[:CHAR_LIMIT] if len(email) > CHAR_LIMIT else email

            enrollment_date = input("Enter enrollment date in the form year-month-day (yyyy-mm-dd): ")

            addStudent(first_name, last_name, email, enrollment_date)
        elif option == 3:
            student_id = input("Enter student ID: ")

            new_email = input("Enter email: ")
            new_email = new_email[:CHAR_LIMIT] if len(new_email) > CHAR_LIMIT else new_email

            updateStudentEmail(student_id, new_email)
        elif option == 4:
            deleteStudent(input("Enter student ID: "))
        elif option == 5:
            exit(1)
        else:
            print("Incorrect input.")

def end_application(): # Just to close the database connection properly
    cursor.close()
    connection.close()

def validate_email(email):
    parts = email.split("@")
    if len(parts) == 2 and "." in parts[1]: # Making sure there's at least an @ and . in the second half of the email
        return True
    else:
        return False

def getAllStudents():
    """
    Retrieves and displays all records from the students table.
    """
    cursor.execute("SELECT * FROM students") # All records in the table

    column_names = [description[0] for description in cursor.description] # Retrieves each column name

    print("-----------------------------------------------------------------") 
    for column in column_names:
        print(f"| {column} ", end="")
    print("|")
    print("-----------------------------------------------------------------")

    rows = [row for row in cursor] # Get all row data
    for row in rows:
        print("|", end="")
        for column in row: # Each individual attribute for each student
            print(f" {column} ", end="|")
        print()
    print("-----------------------------------------------------------------") 

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Adds the given data to a new row, then inserts the row into the students table.

    Arguments:
        first_name: String
        last_name: String
        email: String
        enrollment_date: String
    """

    if not validate_email(email):
        print("Incorrect email format, check again.")
        return

    values = (first_name, last_name, email, enrollment_date) # New row, these get substituted into the query

    try:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", values) 
        connection.commit() # Completes the transaction, sending the query to the database
    except Exception as e:
        print(e)
        connection.rollback() # Make sure to rollback on any errors
    

def updateStudentEmail(student_id, new_email):
    """
    Updates the email address for a student with the specified student_id.

    Arguments:
        student_id: String
        new_email: String
    """

    if not validate_email(new_email):
        print("Incorrect email format, check again.")
        return

    values = (new_email, student_id) # These get substituted into the query

    try:
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", values) # Updates the corresponding student's email
        connection.commit() # If there is no student_id which matches, nothing gets updated, no harm done
    except Exception as e:
        print(e)
        connection.rollback()

def deleteStudent(student_id):
    """
    Deletes the record of the student with the specified student_id

    Arguments:
        student_id: String
    """

    cursor.execute("DELETE FROM students WHERE student_id = %s", student_id)
    connection.commit() # If there is no student_id which matches, nothing gets deleted, no harm done

if __name__ == "__main__":
    start_application()
    end_application()