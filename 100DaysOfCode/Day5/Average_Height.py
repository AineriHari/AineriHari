# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

sum_of_student_heights = 0
for height in student_heights:
    sum_of_student_heights += height

length_of_student_heights = 0
for count in student_heights:
    length_of_student_heights += 1

print(round((sum_of_student_heights / length_of_student_heights)))
