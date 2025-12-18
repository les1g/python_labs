# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    # Type your code here.
    # Check if name exists in the dictionary
    if name not in info:
        raise StudentInfoError(f'Student ID not found for {name}')
    return info[name]


def find_name(ID, info):
    # Type your code here.
    # Check if ID exists in the dictionary values
    name = [name for name, student_ID in info.items() if student_ID == ID]
    if not name:  # If no name is found
        raise StudentInfoError(f'Student name not found for {ID}')
    return name[0]


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }

    userChoice = input()    # Read search option from user. 0: find_ID(), 1: find_name()

    # FIXME: find_ID() and find_name() may raise an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as e:  # Catch the custom exception
        print(e)
