def avarege_grade(records):
    total_grade= sum(record[2] for record in records)
    return total_grade/ len(records)
student= (
    ("james",20,85)
    ("Sumeet",22,90)
    ("Modi",21,44)
)
def main():
    avg_grades = avarege_grade(student)
    print("Avrage Grades",avg_grades)