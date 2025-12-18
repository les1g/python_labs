# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

# Print the name and grade percentage of the student with the highest total of points.
sum_student_grades = {}
for student, grades in student_grades.items(): # iterate through values using items() to be able to access names and grades
    sum_student_grades[student] = sum(grades) # store name and sum of each student grades in dict
student_with_highest_points = max(sum_student_grades, key=sum_student_grades.get) # Store student name with max grade
highest_points_percent = (sum_student_grades[student_with_highest_points] / 500) * 100 # computer percentage of grade
print(f'{student_with_highest_points} has the highest score: %{highest_points_percent:.2f}')

# Find the average score of each assignment.
print() # new line
sum_all_grades = 0
total_students = 0
for student in sum_student_grades: # iterate through values of sum_student_grades
    total_students += 1 # get number of total students
    sum_all_grades += sum_student_grades[student] # get sum of all total grade points
average_score = ((sum_all_grades / 500) / total_students) * 100 # 5 assignments, computes average as percent
print(f'The average score of each assignment: %{average_score:.2f}')

# Find and apply a curve to each student's total score, such that the best student has 100% of the total points.
print() # new line
class_curve = 100 / highest_points_percent
for student in sum_student_grades:
    curved_score_percent = sum_student_grades[student] * class_curve
    print(f"{student}'s curved score is: {curved_score_percent:.2f}")
