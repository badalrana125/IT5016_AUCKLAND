


class Whitecliffe:
    membershipid_counter = 400001 

    def __init__(self, studentid, lname, program):
        self.studentid = studentid
        self.lname = lname
        self.program = program
        self.membershipid = Whitecliffe.membershipid_counter  
        Whitecliffe.membershipid_counter += 1  

    def add_request(self):
        last_name = input("Enter your last name: ")
        studentid = input("Enter your student ID: ")
        program = input("Enter your program: ")

        self.studentid = studentid
        self.lname = last_name
        self.program = program

    def display(self):
        print(f"Student ID: {self.studentid} \nLast Name: {self.lname} \nProgram: {self.program} \nMembership ID: {self.membershipid}")

info = Whitecliffe(20240483, "Basyal", "Bachelor of Applied Information Technology")

info.add_request()
info.display()

# # Create another student to see membership ID increment
# another_student = Whitecliffe(20240484, "Shrestha", "Master of Information Technology")
# another_student.display()




