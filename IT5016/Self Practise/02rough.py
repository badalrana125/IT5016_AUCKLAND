# # Membership class
# class Membership:
#     membership_counter = 1000  # To automatically assign Membership ID
#     registered_members = []    # List to store registered members
#     withdrawn_members = []     # List to store withdrawn members
    
#     def __init__(self):
#         self.total_registered = 0
#         self.total_diploma = 0
#         self.total_bachelor = 0
#         self.total_withdrawn = 0
    
#     def register_member(self, student_id, last_name, programme):
#         if programme not in ["Diploma", "Bachelor"]:
#             print("Invalid programme. Only 'Diploma' or 'Bachelor' is allowed.")
#             return
        
#         membership_id = Membership.membership_counter
#         Membership.membership_counter += 1
        
#         # Create a student dictionary
#         student = {
#             'student_id': student_id,
#             'last_name': last_name,
#             'programme': programme,
#             'membership_id': membership_id
#         }
        
#         Membership.registered_members.append(student)
#         self.total_registered += 1
        
#         if programme == "Diploma":
#             self.total_diploma += 1
#         elif programme == "Bachelor":
#             self.total_bachelor += 1
        
#         print(f"Student {last_name} registered successfully with Membership ID {membership_id}.\n")
    
#     def withdraw_member(self, membership_id, last_name):
#         found = False
        
#         for student in Membership.registered_members:
#             if student['membership_id'] == membership_id and student['last_name'] == last_name:
#                 Membership.withdrawn_members.append(student)
#                 Membership.registered_members.remove(student)
#                 self.total_withdrawn += 1
#                 self.total_registered -= 1
                
#                 if student['programme'] == "Diploma":
#                     self.total_diploma -= 1
#                 elif student['programme'] == "Bachelor":
#                     self.total_bachelor -= 1
                
#                 print(f"Student {last_name} with Membership ID {membership_id} has withdrawn.\n")
#                 found = True
#                 break
        
#         if not found:
#             print("Member not found or incorrect details provided.\n")
    
#     def display_members(self):
#         print("\n--- Whitecliffe Students' Club Members ---")
#         print(f"Total Registered Members: {self.total_registered}")
#         print(f"Total Diploma Students: {self.total_diploma}")
#         print(f"Total Bachelor Students: {self.total_bachelor}")
#         print(f"Total Withdrawn Members: {self.total_withdrawn}\n")
        
#         if Membership.registered_members:
#             print("Registered Members List:")
#             for student in Membership.registered_members:
#                 print(f"ID: {student['membership_id']}, Name: {student['last_name']}, Programme: {student['programme']}")
#         else:
#             print("No registered members.\n")


# # Test the system
# club = Membership()

# # Registering members
# club.register_member(1001, "Smith", "Bachelor")
# club.register_member(1002, "Johnson", "Diploma")
# club.register_member(1003, "Williams", "Bachelor")

# # Display registered members
# club.display_members()

# # Withdraw a member
# club.withdraw_member(1001, "Smith")

# # Display members again after withdrawal
# club.display_members()






class Membership:
    membership_counter = 1000  

    def __init__(self):
        self.members = []      
        self.withdrawn_count = 0 

    def register(self):
        student_id = input("Enter Student ID: ")
        last_name = input("Enter Last Name: ")
        programme = input("Enter Programme (Diploma or Bachelor): ")
        
        membership_id = Membership.membership_counter
        Membership.membership_counter += 1
        
        student = {
            'student_id': student_id,
            'last_name': last_name,
            'programme': programme,
            'membership_id': membership_id
        }
        
        self.members.append(student)
        print(f"{last_name} registered successfully with Membership ID {membership_id}.\n")
        
    def withdraw(self):
        membership_id = int(input("Enter Membership ID: "))
        last_name = input("Enter Last Name: ")
        
        for student in self.members:
            if student['membership_id'] == membership_id and student['last_name'] == last_name:
                self.members.remove(student)
                self.withdrawn_count += 1
                print(f"{last_name} with Membership ID {membership_id} has withdrawn.\n")
                return
        print("Member not found.\n")

    def display(self):
        print(f"\nTotal Registered Members: {len(self.members)}")
        print(f"Total Withdrawn Members: {self.withdrawn_count}\n")
        
        if self.members:
            for student in self.members:
                print(f"ID: {student['membership_id']}, Name: {student['last_name']}, Programme: {student['programme']}")
        else:
            print("No registered members.\n")

# Test the system
club = Membership()

while True:
    print("\n1. Register a member")
    print("2. Withdraw a member")
    print("3. Display all members")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        club.register()
    elif choice == '2':
        club.withdraw()
    elif choice == '3':
        club.display()
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid option. Please try again.")
                                                                           