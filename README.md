# Student Academic Management System

## About the Project

This is a simple **Student Academic Management System** made using Python.

The main purpose of this project is to manage student details, courses and marks from the terminal. The data is stored in CSV files, so the information can be saved and used again later.

This project is completely command-line based, so there is no need for any GUI.

## What This Project Can Do

The project has mainly 4 sections:

### 1. Manage Students

In this section we can:

* Add a new student
* View all students
* Search for a student using their student ID

The student information includes:

* Student ID
* Student name
* Email
* Department
* Enrollment year

### 2. Manage Courses

In this section we can:

* Add a new course
* View all available courses

The course information includes:

* Course ID
* Course name
* Department
* Credits

### 3. Enter Marks

This section is used to enter marks for a student.

Before adding marks, the program checks:

* Whether the student ID exists
* Whether the course ID exists
* Whether the marks are between 0 and 100

If everything is correct, the marks are saved in the marks CSV file.

### 4. View Reports

This section contains different reports:

* Student Report
* Class Average
* Top Performers

The **Student Report** shows the student's details, courses, marks, total marks, percentage and grade.

The grading is done as:

* 90 or above → A+
* 80 to 89 → A
* 70 to 79 → B
* 60 to 69 → C
* 50 to 59 → D
* Below 50 → F

The **Class Average** calculates the average of all the marks entered.

The **Top Performers** section shows up to 5 students with the highest percentage.

## Files Used

The program uses CSV files to store the data.

The main files are:

```text
students.csv
courses.csv
marks.csv
```

### students.csv

This file stores student information.

### courses.csv

This file stores course information.

### marks.csv

This file stores the marks of students for different courses.

## Requirements

To run this project, you need:

* Python 3
* Any code editor such as VS Code
* Terminal

The program uses Python's built-in `csv` module, so no extra library needs to be installed.



## Project Type
**Language:** Python
**Storage:** CSV files
**Interface:** Command Line / Terminal
**Main Python Module Used:** csv

## Conclusion

This project helped me understand how to make a simple menu-based Python program and how to store and read data using CSV files.
I also used different concepts like loops, conditions, file handling, lists and basic calculations while making this project.
