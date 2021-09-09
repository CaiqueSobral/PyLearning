student_heights = input("Input a list of student heights. ").split()
sum_of_heights = 0
number_of_heights = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_of_heights += student_heights[n]
  number_of_heights += 1

print("The avarage height is: " + str(round(sum_of_heights / number_of_heights)))