
# COMP3005 Assignment 3

### By Max Sobota

## Summary
Application which connects to a PostgreSQL to perform CRUD (Create, Read, Update, Delete) operations.

## Video
(Video link here)

## Requirements
I chose Python as my language of choice to keep things simple, as there are many available libraries to use which make connections to a PostgreSQL database.  
I'm running Python version 3.11.9.

I used the psycopg2 package for my implementation, to install using pip, run the command "pip install psycopg2".  
The library can be found here: https://pypi.org/project/psycopg2/

## Running
Run with "python application.py"

## Query
Here is the query I used to create the database:

```
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,  
    first_name VARCHAR(255) NOT NULL,  
    last_name VARCHAR(255) NOT NULL,  
    email VARCHAR(255) UNIQUE NOT NULL,  
    enrollment_date DATE  
)
```

I then populated it using the query given on the assignment spec.  
Since it wasn't clearly stated, I assumed the database already exists and is populated using these queries prior to running the application.py script.

## Assumptions and other details
I'm using a 255 character limit for the strings as we've previously used in our SQL assignments.
For addStudent, I assumed that enrollment_date would be a string in the correct format "year-month-date", as that's how psycopg2 processes them. I added error checking just in case.
Seeing as psycopg2 requires a connection to the database to run queries, and I couldn't edit the function signatures, I opted to just use global variables.
It's not explicitly stated, but I'm assuming our file will be run on its own, not just the individual required 4 functions.