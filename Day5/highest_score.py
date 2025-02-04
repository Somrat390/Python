student_scores =input("Input a list of student scores ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])

print(student_scores)
max = 0
for i in student_scores:
    if i > max:
        max = i

print(f"Highest score is {max}")
