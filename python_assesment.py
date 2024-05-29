studentManagement = {}

def add():
        print("----------------Add Student----------")
        Serial_num=int(input("Enter serial Num : "))
        f_name=input("Fist Name : ")
        l_name=input("Last Name : ")
        mobile_num=int(input("Enter Mobile Num : "))
        suject_dict={}
        no_of_subject=int(input("Enter of Subject No : "))
        for i in range(0,no_of_subject):
            subject=input("Subject : ")
            marks=int(input("Marks : "))
            fess=int(input("Fees : "))
            suject_dict={"Marks":marks,"Fees":fess}
        Faculty=input("Faculty Name : ")
        student_ditails={}
        student_ditails["First Name"]=f_name
        student_ditails["Last Name"]=l_name
        student_ditails["Mobile"]=mobile_num
        student_ditails[subject]=suject_dict
        student_ditails["Faculty"]=Faculty
        print("**********Add Success*********")
        studentManagement[Serial_num]=student_ditails
        print(studentManagement)
def view():
    for k, sub_dic in studentManagement.items():
        print("------------------------------------------------")
        print("************STUDENT DETAILS VIEW PAGE************")
        print("Serial Num : ", k)
        print("First Name :", sub_dic["First Name"])
        print("Last Name :", sub_dic["Last Name"])
        print("Mobile :", sub_dic["Mobile"])
        print("Faculty :", sub_dic["Faculty"])
        print("Subjects:")
        for subject, details in sub_dic.items():
            if subject != "First Name" and subject != "Last Name" and subject != "Mobile" and subject != "Faculty":
             print("\t\tMarks:", details["Marks"])
             print("\t\tFees:", details["Fees"])
def remove():
        Serial_num=int(input("Enter Student Serial num Which You Want To Delete : "))
        if Serial_num in studentManagement.keys():
            del studentManagement[Serial_num]
            print("successfully record deleted ! ")
            view()
        else:
            print("invalid serial number")
            
def view_specific_student():
    Serial_num = int(input("Enter Serial Number of the Student You Want to Search: "))
    if Serial_num in studentManagement.keys():
        print("-------------VIEW SEARCH DETAILS-------------")
        print("First Name:", studentManagement[Serial_num]["First Name"])
        print("Last Name:", studentManagement[Serial_num]["Last Name"])
        print("Mobile:", studentManagement[Serial_num]["Mobile"])
        print("Faculty:", studentManagement[Serial_num]["Faculty"])
        print("Subjects:")
        for subject, details in studentManagement[Serial_num].items():
            if subject not in ["First Name", "Last Name", "Mobile", "Faculty"]:
                print("\t\tMarks:", details["Marks"])
                print("\t\tFees:", details["Fees"])
    else:
        print("Student with Serial Number", Serial_num, "not found.")
def add_marks():
    Serial_num = int(input("Enter Serial Number of the Student: "))
    if Serial_num in studentManagement.keys():
        student = studentManagement[Serial_num]
        print(f"Adding Marks for {student['First Name']} {student['Last Name']}:")
        for subject, details in student.items():
            if subject not in ["First Name", "Last Name", "Mobile", "Faculty"]:
                marks = int(input(f"Enter Marks for {subject}: "))
                student[subject]['Marks'] = marks
        print("Marks added successfully!")
        
    else:
        print("Student not found.")

def menu():
    menu="""
           STUDENT MENAGMENT SYSTEAM
             PRESS 1 FOR CONSELLOR
             PRESS 2 FOR FACULTY
             PRESS 3 FOR STUDENT
   """
    print(menu)
    
    choice=int(input("Enter your choice : "))
    if choice==1:
        menu1="""
               1. Add Student
               2. Remove Student
               3. View All Student
               4. View specific student
        """
        print(menu1)
        choice1=int(input("Enter Your Choice : "))
        if choice1==1:
                add()
        elif choice1==2:
                remove() 
        elif choice1==3:
                view()
        elif choice1==4:
                view_specific_student()
        else:
            print("invalid choice")
    elif choice==2:
        menu1="""
               1. Add Marks To Student
               2. View All Student
               
        """
        print(menu1)
        choice2=int(input("Enter Your Choice : "))
        if choice2==1:
            add_marks()
        elif choice2==2:
            view()
    elif choice==3:
        pass
    else:
        print("invalid choice")
        
status=True
while status:
    menu()
    exit = input("do you want to continue ? press y for yes and press n for no ")
    if exit == 'y':
        status = True
    else:
        status = False

        
       