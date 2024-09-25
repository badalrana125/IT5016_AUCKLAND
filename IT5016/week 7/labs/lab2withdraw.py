class Member:
    def __init__(self, lname, id=0):
        self.lname = lname 
        self.id = id
        self.registeredstudents = 400
        self.withdrawnstudents = 600
        self.active = True
    
    def increment_id(self):
        self.id += 1
        return self.id
    
    def withdraw(self):
        if self.active and self.registeredstudents > 0:
            self.registeredstudents -= 1
            self.withdrawnstudents += 1
            print(f"Registered students: {self.registeredstudents}")
            print(f"Withdrawn students: {self.withdrawnstudents}")
        else:
            print("Invalid operation")
    
    def program(self, stream):
        if stream == "Diploma":
            print("Student Program is Diploma.")
        else:
            print("Student Program is Bachelor.")
    
    def display(self):
        print(f"LAST NAME: {self.lname}")
        print(f"Membership ID: {self.id}")
        print(f"Registered students: {self.registeredstudents}")
        print(f"Withdrawn students: {self.withdrawnstudents}")
        
info = Member("Aashish")
info.increment_id()
info.withdraw()
info.display()