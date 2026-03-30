"""
------------------------------------------------------------
Author: Rahdner Savain
Date: March 22, 2026

Description:
This program allows a teacher to enter student information (first name, last name, and three exam grades) and stores the data in a CSV file named grades.csv.
It then reads the file and displays the data in a formatted table.
------------------------------------------------------------
"""

# Import csv module
import csv


def inputGrades():

    """
    Description:
    Collects student data and writes it to a CSV file.

    Variables:
    numofStudents (int) - number of students
    firstName (str) - student's first name
    lastName (str) - student's last name
    exam1, exam2, exam3 (int) - exam scores
    file (file object) - CSV file object

    Logical Steps:
    1. Ask user for number of students
    2. Open grades.csv file using 'with'
    3. Write header row
    4. Loop through number of students
    5. Collect student data
    6. Write each record to file
    7. Close file automatically

    """

    # Ask user how many students to enter
    numofStudents = int(input("Enter number of students: "))


    # Open file in write mode
    with open("grades.csv", "w" ,newline="") as csvfile:

        # Create CSV writer to input in file
        writer = csv.writer(csvfile)

        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])


        # Loop through each student
        for i in range(numofStudents):

            print(f"\nEntering data for Student {i + 1}")

            # Collect student names
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")

            # Collect exam grades
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))


            # Write student record to CSV file
            writer.writerow([firstName, lastName, exam1, exam2, exam3])



def tableGrades():

    """
    Description:
    Reads student data from grades.csv and displays it in a formatted table.

    Variables:
    file (file object) - CSV file object
    reader (csv reader) - reads CSV rows

    Logical Steps:
    1. Open grades.csv using 'with'
    2. Read file using csv.reader
    3. Loop through rows
    4. Format and display each row

    """

    print("\n----- Student Grades -----\n")


    # Open file in read mode
    with open("grades.csv", "r") as file:

        # Create CSV reader object
        reader = csv.reader(file)

        # Loop through each row in file
        for row in reader:

            # Format output into columns
            print(f"{row[0]:<12} {row[1]:<15} {row[2]:<8} {row[3]:<8} {row[4]:<8}")



def main():

    """
    Description:
    Controls the program execution.

    Logical Steps:
    1. Call function to write data
    2. Call function to read and display data

    """

    # Write data to CSV file
    inputGrades()

    # Read and display data
    tableGrades()


# Start program
main()