student_grade = { }

#Adding new student
def add_student(name, grade) :
    student_grade[name] = grade
    #[Lia] = 100

    print(f"Added {name} with a grade {grade}")
    #Added Lia with a grade 100

#To update a student
def update_student(name,grade):
    if name in student_grade :
        student_grade[name] = grade
        #Lia = 500
        print(f"{name} with marks are updated {grade}")

    else :
        print(f"{name} is not found!")

# To Delete
def delete_student(name) :
    if name in student_grade :
        del student_grade [name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} not found")

# To view all student
def display_all_student():
    if student_grade :
        for name, grade in student_grade.item():
            print(f"{name} : {grade}")
    else :
        print("No Student Found or Added")

def main():
    while True :
        print(" \n STUDENT GRADE MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")
        
        Choice = int(input("Enter your choice = "))
        if Choice == 1 : 
            name = input("Enter student name = ")
            grade = int(input("Enter the student grade = ")) 
            add_student(name,grade)

        elif Choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter the student grade = "))
            update_student(name,grade)

        elif Choice == 3 :
            name = input("Enter student name = ")
            delete_student(name)

        elif Choice == 4 :
            display_all_student()

        elif Choice == 5 :
            print("Closing the Program ....... ")
            break

        else:
            print("Invalid choice")
