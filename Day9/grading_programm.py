student_scores ={
    "Harry" : 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
student_grade ={}
for key in student_scores:
    if 90 < student_scores[key] <= 100:
        student_grade[key] = "Outsanding"
    elif 80 < student_scores[key] <= 90:
        student_grade[key] = "Excelent Expectation"
    elif 70 < student_scores[key] <= 80:
         student_grade[key] = "Acceptable"
    else:
         student_grade[key] = "Fail"

print(student_grade)
