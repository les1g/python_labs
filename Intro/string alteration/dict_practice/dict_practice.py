student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'): "
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        name = name.title() # initializes name
        grade = grade.upper() # capitalizes grade
        student_grades[name] = grade # stores key 'name' with value 'grade'
        print(f'{name} with grade {grade} has been added.') # confirms grade was added to user
    elif command == '2':
        name, grade = input(grade_prompt).split()
        name = name.title()  # initializes name
        grade = grade.upper()  # capitalizes grade
        if name not in student_grades: # when key is not found in student_grades
            print(f'{name} with grade {grade} was not found.')
        else:
            del student_grades[name] # deletes key 'name'
            print(f'{name} with grade {grade} has been removed.')
    elif command == '3':
        for name in student_grades: # iterates through each name in student_grades
            print(f'{name} has a {student_grades[name]}.')
    elif command == '4':
        break
    else:
        print('Unrecognized command.')

