student_scores = input("Input a list of student scores ").split()
max_number = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if max_number < student_scores[n]:
      max_number = student_scores[n]

print(f"The highest score in the class is: {max_number}")