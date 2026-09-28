import csv

print("HELLO !")
print("==================================================================================================================================")
print("                                                 STUDENT ACADEMIC MANAGEMENT SYSTEM                                       ")
print("==================================================================================================================================")

run=1
while run:
    print()
    print("1. MANAGE STUDENTS")
    print()
    print("2. MANAGE COURSES")
    print()
    print("3. ENTER MARKS")
    print()
    print("4. VIEW REPORTS")
    print()
    print("5. EXIT")
    print()

    choice=int(input("ENTER YOUR CHOICE FROM ABOVE : "))

    if (choice==1): # manage students
        print()
        print("================ MANAGE STUDENTS ================")
        print()
        print("1. ADD STUDENT")
        print()
        print("2. VIEW STUDENTS")
        print()
        print("3. SEARCH STUDENT")
        print()
        print("4. BACK TO MAIN MENU")
        print()
        choice1=int(input("ENTER YOUR CHOICE : "))

        if (choice1==1): # Add students
            t=1
            while t:
                print()
                std_id = input("ENTER THE STUDENT REGISTRATION NUMBER: ")
                print()
                std_name = input("ENTER STUDENT NAME: ")
                print()
                std_email = input("ENTER STUDENT EMAIL ID: ")
                print()
                dep = input("ENTER STUDENT DEPARTMENT: ")
                print()
                batch = input("ENTER STUDENT ENROLLMENT YEAR: ")
                print()
                file=open("students.csv","a",newline="")
                writer=csv.writer(file)
                writer.writerow([std_id,std_name,std_email,dep,batch])
                file.close()
                print("STUDENT ADDED SUCCESSFULLY")
                print()
                t = int(input("ENTER 1 TO ADD ANOTHER STUDENT OR 0 TO GO TO THE MAIN MENU: "))

        elif (choice1==2): # View students
            file=open("students.csv","r")
            reader=csv.reader(file)
            print()
            print("================ STUDENT LIST ================")

            for i in reader:
                if i[0]!="student_id":
                    print("STUDENT ID :",i[0])
                    print("NAME       :",i[1])
                    print("EMAIL      :",i[2])
                    print("DEPARTMENT :",i[3])
                    print("BATCH      :",i[4])
                    print("---------------------------------------")
            file.close()

        elif (choice1==3): #Search Student
            print()
            search=input("ENTER STUDENT ID TO SEARCH : ")
            file=open("students.csv","r")
            reader=csv.reader(file)
            found=0

            for i in reader:
                if i[0]!="student_id":
                    if i[0]==search:
                        print()
                        print("                    STUDENT FOUND                   ")
                        print("----------------------------------------------------")
                        print("STUDENT ID :",i[0])
                        print("NAME       :",i[1])
                        print("EMAIL      :",i[2])
                        print("DEPARTMENT :",i[3])
                        print("BATCH      :",i[4])
                        found=1
            file.close()

            if found==0:
                print()
                print("STUDENT NOT FOUND")

        elif (choice1==4): # Going back to the main menu 
            print()
            print("GOING BACK TO MAIN MENU")
#_________________________MANAGE COURSES____________________________________
    elif (choice==2):
        print()
        print("================ MANAGE COURSES ================")
        print()
        print("1. ADD COURSE")
        print()
        print("2. VIEW COURSES")
        print()
        print("3. BACK TO MAIN MENU")
        print()
        choice2=int(input("ENTER YOUR CHOICE : "))

        if (choice2==1):# Add courses
            print()
            course_id=input("ENTER COURSE ID : ")
            print()
            course_name=input("ENTER COURSE NAME : ")
            print()
            department=input("ENTER DEPARTMENT : ")
            print()
            credits=input("ENTER CREDITS : ")

            file=open("courses.csv","a",newline="")
            writer=csv.writer(file)
            writer.writerow([course_id,course_name,department,credits])
            file.close()
            print("COURSE ADDED SUCCESSFULLY")
            
        elif (choice2==2): # View courses 
            file=open("courses.csv","r")
            reader=csv.reader(file)
            print()
            print("================ COURSE LIST ================")

            for i in reader:
                if i[0]!="course_id":
                    print("COURSE ID   :",i[0])
                    print("COURSE NAME :",i[1])
                    print("DEPARTMENT  :",i[2])
                    print("CREDITS     :",i[3])
                    print("---------------------------------------------")
            file.close()

        elif (choice2==3): # Back to teh main menu
            print()
            print("GOING BACK TO MAIN MENU")
            print("__________________________________________________________________________________________________________________")


    elif (choice==3):# Input marks
        print()
        print("================ ENTER MARKS ================")
        student_id=input("ENTER STUDENT ID : ")
        course_id=input("ENTER COURSE ID : ")
        marks=int(input("ENTER MARKS : "))

        student_found=0
        file=open("students.csv","r")
        reader=csv.reader(file)

        for i in reader:
            if i[0]!="student_id":
                if i[0]==student_id:
                    student_found=1
        file.close()

        course_found=0
        file=open("courses.csv","r")
        reader=csv.reader(file)

        for i in reader:
            if i[0]!="course_id":
                if i[0]==course_id:
                    course_found=1
        file.close()

        if student_found==0:
            print("STUDENT NOT FOUND")
            print("RETURNING TO THE MAIN MENU")
            print("__________________________________________________________________________________________________________________")

        elif course_found==0:
            print("COURSE NOT FOUND")
            print("RETURNING TO THE MAIN MENU")
            print("__________________________________________________________________________________________________________________")

        elif marks<0 or marks>100:
            print("MARKS SHOULD BE BETWEEN 0 AND 100")
        else:
            file=open("marks.csv","a",newline="")
            writer=csv.writer(file)
            writer.writerow([student_id,course_id,marks])
            file.close()
            print("MARKS ENTERED SUCCESSFULLY")
            print("RETURNING TO THE MAIN MENU")
            print("__________________________________________________________________________________________________________________")


    elif (choice==4):
        print()
        print("================ VIEW REPORTS ================")
        print()
        print("1. STUDENT REPORT")
        print()
        print("2. CLASS AVERAGE")
        print()
        print("3. TOP PERFORMERS")
        print()
        print("4. BACK TO MAIN MENU")
        print()
        choice4=int(input("ENTER YOUR CHOICE : "))
        print()

        if (choice4==1): # STUDENT REPORT
            student_id=input("ENTER STUDENT ID : ")
            student_name=""

            file=open("students.csv","r")
            reader=csv.reader(file)

            for i in reader:
                if i[0]!="student_id":
                    if i[0]==student_id:
                        student_name=i[1]
                        student_email=i[2]
                        student_branch=i[3]
                        enrollment_year=i[4]
            file.close()

            if student_name=="":
                print()
                print("STUDENT NOT FOUND")
                print()
                print("RETURNING TO THE MAIN MENU")
                print("-----------------------------------------------")
                
            else:
                print()
                print("================ STUDENT REPORT ================")
                print("STUDENT ID   :",student_id)
                print()
                print("STUDENT NAME :",student_name)
                print()
                print("STUDENT EMAIL :",student_email)
                print()
                print("STUDENT BRANCH :",student_branch)
                print()
                print("STUDENT ENROLLMENT YEAR :",enrollment_year)
                print()
                print("-----------------------------------------------")

                total=0
                count=0
                file=open("marks.csv","r")
                reader=csv.reader(file)

                for i in reader:
                    if i[0]!="student_id":
                        if i[0]==student_id:
                            course_id=i[1]
                            marks=int(i[2])
                            print("COURSE ID :",course_id)
                            print()
                            print("MARKS     :",marks)
                            print("-----------------------------------------------")
                            total=total+marks
                            count=count+1
                file.close()

                if count==0:
                    print("NO MARKS ENTERED")
                else:
                    percentage=total/count

                    if percentage>=90:
                        grade="A+"
                    elif percentage>=80:
                        grade="A"
                    elif percentage>=70:
                        grade="B"
                    elif percentage>=60:
                        grade="C"
                    elif percentage>=50:
                        grade="D"
                    else:
                        grade="F"

                    print("TOTAL MARKS :",total)
                    print()
                    print("PERCENTAGE  :",percentage)
                    print()
                    print("GRADE       :",grade)
                    print("-----------------------------------------------")


        elif (choice4==2): # CLASS AVERAGE
            total=0
            count=0
            file=open("marks.csv","r")
            reader=csv.reader(file)

            for i in reader:
                if i[0]!="student_id":
                    marks=int(i[2])
                    total=total+marks
                    count=count+1
            file.close()

            if count==0:
                print("NO MARKS AVAILABLE")
            else:
                average=total/count
                print()
                print("============== CLASS AVERAGE ==============")
                print("CLASS AVERAGE :",average)
                print()
                print("RETURNING TO THE MAIN MENU")
                print("-----------------------------------------------")

        elif (choice4==3): # TOP PERFORMERS
            result=[]
            file=open("students.csv","r")
            reader=csv.reader(file)

            for student in reader:
                if student[0]!="student_id":
                    student_id=student[0]
                    student_name=student[1]
                    total=0
                    count=0

                    marks_file=open("marks.csv","r")
                    marks_reader=csv.reader(marks_file)

                    for mark in marks_reader:
                        if mark[0]!="student_id":
                            if mark[0]==student_id:
                                total=total+int(mark[2])
                                count=count+1
                    marks_file.close()

                    if count>0:
                        percentage=total/count
                        result.append([student_id,student_name,percentage])
            file.close()

            for i in range(len(result)):
                for j in range(0,len(result)-i-1):
                    if result[j][2]<result[j+1][2]:
                        temp=result[j]
                        result[j]=result[j+1]
                        result[j+1]=temp

            print()
            print("=============== TOP PERFORMERS ===============")

            if len(result)==0:
                print("NO MARKS AVAILABLE")
            else:
                rank=1
                for i in result:
                    if rank<=5:
                        print()
                        print("RANK       :",rank)
                        print("STUDENT ID :",i[0])
                        print("NAME       :",i[1])
                        print("PERCENTAGE :",i[2])
                        print("---------------------------------------------")
                        rank=rank+1

        elif (choice4==4): # Going back to the main menu
            print("GOING BACK TO MAIN MENU")
            print("---------------------------------------------------------------------------------------------------------------------")

    elif (choice==5):
        print()
        print("THANK YOU FOR USING STUDENT ACADEMIC MANAGEMENT SYSTEM")
        run=0

    else:
        print("INVALID CHOICE")