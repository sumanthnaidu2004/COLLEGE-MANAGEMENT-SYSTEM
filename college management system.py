import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
class student(Person):
    def __init__(self,name,email,branch):
        super().__init__(name,email)
        self.branch = branch
class teacher(Person):
    def __init__(self,name,email,subject):
        super().__init__(name,email)
        self.subject = subject
class college:
    def __init__(self,cid,name):
        self.name = name
        self.cid = cid
        self.students = []
        self.teachers = []
    def add_teachers(self,teacher):
        self.teachers.append(teacher)
    def add_students(self,student):
        self.students.append(student)
    def display_teachers(self):
        if len(self.teachers) == 0:
            print("No Teachers Present")
        else:
            print()
            print("Teacher Details")
            for x in self.teachers:
                print("Name:",x.name)
                print("Email:",x.email)
                print("Subject:",x.subject)
                print()
    def display_students(self):
        if len(self.students) == 0:
            print("No Students Present")
        else:
            print("student Details:")
            for x in self.students:
                print("Name:",x.name)
                print("Email:",x.email)
                print("Branch:",x.branch)
                print()
colleges = []
while True:
    print("choose your Option: ")
    print("1. To Create College")
    print("2. To Add Teacher")
    print("3. To Add Student")
    print("4. To Display Teacher Details")
    print("5. To Display Student Details")
    print("6. Exit")
    option = int(input("Enter Your Option: "))
    if option == 1:
        clg_id = int(input("Enter College Id: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x = True
                break
        if x == True:
            print()
            print(f"College with {clg_id} already Exist, Try again")
            print()
        else:
            clg_name = input("Enter College Name: ")
            clg = college(clg_id,clg_name)
            colleges.append(clg)
            print()
            print("College Created Sucessfully")
            print()
    elif option == 2:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            name = input("Enter Teacher Name: ")
            
            otp = random.randint(1111,9999)

            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            username = "sumanthnaidu59@gmail.com"
            password = "krde bjah foxm vkat"

            from_email = "sumanthnaidu59@gmail.com"
            email = input("Enter Teacher Email: ")
            subject = "OTP Validation"
            body = f"OTP for Validation {otp}. \nThank You."

            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(body,'plain'))

            server = smtplib.SMTP(smtp_server,smtp_port)
            server.starttls()
            server.login(username,password)
            server.send_message(msg)
            server.quit()

            print("email Sent")
            for i in range(3):
                x = int(input("Enter OTP Recieved to your mail: "))
                if (x == otp):
                    print("Valid")
                    subject = input("Enter Teacher Subject: ")
                    t = teacher(name,email,subject)
                    clg1.add_teachers(t)
                    print()
                    print(f"Teacher Added Sucessfully to {clg1.name}")
                    print()
                    break
                    
                else:
                    print("Invalid, Try again")
            else:
                print("Invalid, No Option Left")

            
            
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 3:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            name = input("Enter Student Name: ")
            
            otp = random.randint(1111,9999)

            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            username = "sumanthnaidu59@gmail.com"
            password = "krde bjah foxm vkat"

            from_email = "sumanthnaidu59@gmail.com"
            email = input("Enter Student Email: ")
            subject = "OTP Validation"
            body = f"OTP for Validation {otp}. \nThank You."

            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(body,'plain'))

            server = smtplib.SMTP(smtp_server,smtp_port)
            server.starttls()
            server.login(username,password)
            server.send_message(msg)
            server.quit()
            print("email Sent")
            for i in range(3):
                x = int(input("Enter OTP Recieved to your mail: "))
                if (x == otp):
                    print("Valid")
                    branch = input("Enter Student Branch: ")
                    s = student(name,email,branch)
                    clg1.add_students(s)
                    print()
                    print(f"Student Added Sucessfully to {clg1.name}")
                    print()
                    break
                    
                else:
                    print("Invalid, Try again")
            else:
                print("Invalid, No Option Left")
           
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 4:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_teachers()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 5:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_students()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 6:
        print("THANK YOU")
        break
    else:
        print()
        print("Wrong Option Opted, Try Again")
        print()
    
'''
c1 = college("JNTU-GV")

t1 = teacher("T1","t1@gmail.com","Python")
t2 = teacher("T2","t2@gmail.com","Java")

c1.add_teachers(t1)
c1.add_teachers(t2)

s1 = student("S1","s1@gmail.com","PFS")
s2 = student("S2","s2@gmail.com","JFS")

c1.add_students(s1)
c1.add_students(s2)

c1.display_teachers()
c1.display_students()
'''