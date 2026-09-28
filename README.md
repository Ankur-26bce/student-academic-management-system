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

1. students.csv
2. courses.csv
3. marks.csv

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

Screenshots :

<img width="1648" height="996" alt="Screenshot 2026-09-28 at 9 48 07 PM" src="https://github.com/user-attachments/assets/a3787456-2caf-4ed5-8a56-dc8bd918369f" />

<img width="1652" height="1001" alt="Screenshot 2026-09-28 at 9 48 29 PM" src="https://github.com/user-attachments/assets/522757d6-e475-4d65-a153-6da0f878005e" />

<img width="1650" height="995" alt="Screenshot 2026-09-28 at 9 48 43 PM" src="https://github.com/user-attachments/assets/d9e01864-740d-409b-b65a-1fef81f8d710" />

<img width="1644" height="999" alt="Screenshot 2026-09-28 at 9 49 03 PM" src="https://github.com/user-attachments/assets/23df5a44-836b-4d84-8381-d292cce5454f" />

<img width="1648" height="990" alt="Screenshot 2026-09-28 at 9 49 20 PM" src="https://github.com/user-attachments/assets/2bd02757-521d-466f-847f-2f84672c6755" />

<img width="1644" height="991" alt="Screenshot 2026-09-28 at 9 49 38 PM" src="https://github.com/user-attachments/assets/3bc80d4b-d753-48d5-b7b0-3faa7ba20a92" />

<img width="1644" height="983" alt="Screenshot 2026-09-28 at 9 49 58 PM" src="https://github.com/user-attachments/assets/84d08607-79d0-425f-8d97-456c6522bdf8" />

<img width="1645" height="993" alt="Screenshot 2026-09-28 at 9 50 12 PM" src="https://github.com/user-attachments/assets/05dcda47-423f-441f-859b-4265b820f2f4" />

<img width="1645" height="993" alt="Screenshot 2026-09-28 at 9 50 28 PM" src="https://github.com/user-attachments/assets/19afcf01-7351-4d4e-a3a4-73d3e3bc3d0e" />

<img width="1647" height="994" alt="Screenshot 2026-09-28 at 9 50 52 PM" src="https://github.com/user-attachments/assets/ffd40da0-5257-45ff-9bb6-bbbdefc3b048" />

Outputs :

<img width="1637" height="992" alt="Screenshot 2026-09-28 at 10 03 26 PM" src="https://github.com/user-attachments/assets/85813adc-2b29-49a2-a0eb-fcf2ef34af3f" />

<img width="1655" height="1002" alt="Screenshot 2026-09-28 at 10 05 27 PM" src="https://github.com/user-attachments/assets/23cd085c-97a8-4580-a661-4b77b5873435" />

<img width="1354" height="1004" alt="Screenshot 2026-09-28 at 10 07 12 PM" src="https://github.com/user-attachments/assets/a6737d27-67c0-4858-90c8-4b7e8ba5a67f" />

<img width="1357" height="550" alt="Screenshot 2026-09-28 at 10 08 31 PM" src="https://github.com/user-attachments/assets/89a870d8-e6fc-4cd8-a150-20368dba2652" />

<img width="1352" height="1007" alt="Screenshot 2026-09-28 at 10 09 01 PM" src="https://github.com/user-attachments/assets/3101633b-e19d-499b-810f-84c21b8360f9" />

<img width="1357" height="1004" alt="Screenshot 2026-09-28 at 10 22 25 PM" src="https://github.com/user-attachments/assets/34389f96-20f0-44aa-95f2-a44686206b6f" />

<img width="1356" height="431" alt="Screenshot 2026-09-28 at 10 23 12 PM" src="https://github.com/user-attachments/assets/bb129bd1-4f50-4203-b10d-f093e863f1eb" />

