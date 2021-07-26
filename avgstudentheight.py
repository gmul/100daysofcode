
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


list_sum = 0
for height in student_heights:
    list_sum = int(height) + list_sum

height_average = round(list_sum / len(student_heights))

print(height_average)

    

