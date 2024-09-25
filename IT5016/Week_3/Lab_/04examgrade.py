def average_grade(assesment_grade, exam_grade):
    return(assesment_grade + exam_grade) * 0.5

def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return"B"
    elif average >= 60:
        return"D"
    else:
        return"FAIL"
    
def main():
    """
    Main function to handle user input and display the final grade.
    """
    try:
# User inputs grades
       assessment_grade = float(input("Enter your assessment grade: "))
       exam_grade = float(input("Enter your exam grade: "))
# Calculate the average grade
       final_grade = average_grade(assessment_grade, exam_grade)
       print(f"Your average grade is {final_grade:.2f}%.")

       letter_grade = determine_grade(final_grade)
       print(f"Your final grade is {letter_grade}.")
    except ValueError:
       print("Invalid input. Please enter numeric values.")

main()    
