def give_grade(students_average):
    # Give a grade according to average
    if 90 <= students_average:
        student_grade = 'A'
    elif 80 <= students_average:
        student_grade = 'B'
    elif 70 <= students_average:
        student_grade = 'C'
    elif 60 <= students_average:
        student_grade = 'D'
    else:
        student_grade = 'F'

    return student_grade


# read file name from user
file_name = input().strip()

# open and read tsv file
with open(file_name) as student_info:
    student_info = student_info.readlines()

# separate each piece of info
new_info = [info.split() for info in student_info]

# loop variables
num_students = 0
term1_total = 0
term2_total = 0
final_total = 0

with open('report.txt', 'w') as report:  # open new file for writing
    for info in new_info:  # iterate through new_info
        # Retreive information
        last, first, term1, term2, final = info[0], info[1], int(info[2]), int(info[3]), int(info[4])

        students_average = (term1 + term2 + final) / 3  # Compute students overall average

        student_grade = give_grade(students_average)  # Give a grade to overall average

        # get total for each test and count number of students
        num_students += 1
        term1_total += term1
        term2_total += term2
        final_total += final

        # write each student info to file including grade
        report.write(f'{last}\t{first}\t{term1}\t{term2}\t{final}\t{student_grade}\n')

# average for each test
term1_avg = term1_total / num_students
term2_avg = term2_total / num_students
final_avg = final_total / num_students

# create string for averages
class_averages = f'\nAverages: midterm1 {term1_avg:.2f}, midterm2 {term2_avg:.2f}, final {final_avg:.2f}\n'

# add averages to report file
with open('report.txt', 'a') as report:
    report.write(class_averages)
