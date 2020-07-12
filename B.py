import json
import csv

while True:
    try:
        print(id)
        print('Enter Choice')
        print('-------------------')
        print('1.Course List')
        print('2.New Registration')
        print('3.All Student Info')
        print('4.Update Student Info')
        print('5.Delete Student Info')
        print('6.Course Completion')
        print('7.Pay Installment')
        print('8.Exit')
        print('-------------------')
        GIVEN_CHOICE = int(input("Enter choice number: "))
        if GIVEN_CHOICE == 8:
            break
    except ValueError:
        print("Not valid integer. TRY AGAIN!!")
        continue
    else:
        break


class Academy:
    def __init__(self, choice):
        self.choice = choice
        self.selector()
        self.all_list = []

    def course_list(self):
        return """
        a. PHP
        b. Python
        c. Java
        d. C++
        """

    def new_registration(self):
        name = input('Enter Name to register: ')
        password = input('Enter password: ')
        courses = input('Enter a course (a,b,c,d): ')


        fields = [{'name':name,'password':password,'courses':courses,'balance':0}]

        with open('data_file.txt', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        return 'Successfully Registered'

    def get_all_student_info(self):
        f = open('data_file.txt', 'r')
        with f:
            reader = csv.reader(f)
            for row in reader:
                for e in row:
                    print(eval(e))

    def display_all_student_info(self):
        self.get_all_student_info()
        return f'All Student Data'



    def update_student_info(self):
        return "update_student_info"

    def delete_student_info(self):
        return "delete_student_info"

    def course_complete(self):
        return "course_complete"

    def pay_installment(self):
        name = input('Enter name: ')
        password = input('Enter password: ')
        amount = input('Enter amount to pay 1.) 5000 2.) 10000: ')



        return "pay_installment"

    def selector(self):
        if self.choice == 1:
            print(self.course_list())
        elif self.choice == 2:
            print(self.new_registration())
        elif self.choice == 3:
            print(self.display_all_student_info())
        elif self.choice == 4:
            print(self.update_student_info())
        elif self.choice == 5:
            print(self.delete_student_info())
        elif self.choice == 6:
            print(self.course_complete())
        elif self.choice == 7:
            print(self.pay_installment())
        else:
            print("Please enter correct operator")


cal = Academy(GIVEN_CHOICE)
