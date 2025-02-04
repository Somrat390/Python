student_height = input("Input a list of student heights ").split()
for i in range(0,len(student_height)):
    student_height[i] = int(student_height[i])
len = 0
sum = 0
print(student_height)
for i in student_height:
    sum += i
    len += 1

print(f"Average of student height {round(sum / len)}")
