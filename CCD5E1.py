
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


num_of_students = 0 
for student in student_heights:
  num_of_students += 1
# print(num_of_students)

total_height = 0 
for height in student_heights:
  total_height += height 
# print(total_height)

height_average = round(total_height / num_of_students)
print(f"Average Student height is :{height_average}")