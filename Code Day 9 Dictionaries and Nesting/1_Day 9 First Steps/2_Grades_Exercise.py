studentScores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#ToDo-1: Create an empty dictionary called student_grades.
studentGrades = {}

#ToDo-2: Write your code below to add the grades to student_grades.👇
for key in studentScores:
    if studentScores[key] > 90:
        studentGrades[key] = "Outstanding"
    elif studentScores[key] > 80:
        studentGrades[key] = "Exceeds Expectations"
    elif studentScores[key] > 70:
        studentGrades[key] = "Acceptable"
    else:
        studentGrades[key] = "Fail"
print(studentGrades)