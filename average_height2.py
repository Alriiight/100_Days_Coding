# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
counter = 0

for student in student_heights:
  total_height += student
  counter += 1

average_height = round(total_height / counter)
print(f"Total height: {total_height}")
print(f"Number of students: {counter}")
print(f"The average height is: {average_height}")
