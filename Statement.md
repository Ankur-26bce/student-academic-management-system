# STATEMENT OF THE PROJECT

## Student Academic Management System

### Problem Statement

Managing student academic information manually can become difficult when there are many students, courses and marks.

The purpose of this project is to create a simple **Student Academic Management System** using Python. The system allows the user to store student details, course details and marks and view different academic reports.

The project works completely through the **command line/terminal** and stores the information in CSV files.

### Objectives

The main objectives of this project are:

* To store student information.
* To store course information.
* To enter and store marks of students.
* To search for a student using their student ID.
* To display all students and courses.
* To generate student academic reports.
* To calculate the class average.
* To display the top performing students.
* To store data permanently using CSV files.

### Main Features

The project contains the following main sections:

#### 1. Manage Students

This section allows the user to:

* Add a new student.
* View all students.
* Search for a student using student ID.

The student details stored are:

* Student ID
* Student Name
* Email
* Department
* Enrollment Year

#### 2. Manage Courses

This section allows the user to:

* Add a new course.
* View all available courses.

The course details stored are:

* Course ID
* Course Name
* Department
* Credits

#### 3. Enter Marks

The user can enter marks for a particular student and course.

Before saving the marks, the program checks:

* Whether the student exists.
* Whether the course exists.
* Whether the marks are between 0 and 100.

The marks are then stored in the marks.csv file.

#### 4. View Reports

The project provides three types of reports:

* Student Report
* Class Average
* Top Performers

The Student Report displays the student's details, marks, total marks, percentage and grade.

The grading system used in the project is:

* 90 and above → A+
* 80 to 89 → A
* 70 to 79 → B
* 60 to 69 → C
* 50 to 59 → D
* Below 50 → F

The Class Average section calculates the average of all the marks entered.

The Top Performers section displays up to 5 students having the highest percentage.

### Technologies Used

* **Programming Language:** Python
* **Data Storage:** CSV files
* **Interface:** Command Line / Terminal
* **Python Module Used:** csv

No external Python libraries are required to run the project.

### Files Used

The project uses three CSV files:

* students.csv – stores student information.
* courses.csv – stores course information.
* marks.csv – stores student marks.

The main Python file is:

* main.py

### Expected Outcome

The expected outcome of this project is a simple and easy-to-use academic management system that can manage student records, courses and marks from the terminal.

The system also helps generate useful academic information such as student reports, class average and top performers.

### Conclusion

This project demonstrates the use of basic Python concepts such as:

* Variables
* Input and output
* Conditions
* Loops
* Lists
* File handling
* CSV files
* Basic calculations

By making this project, I learned how to create a menu-based Python program and how to store and retrieve information using CSV files.
