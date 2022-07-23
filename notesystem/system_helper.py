def check_input_to_number(input_string):
    if input_string.isdigit():
        return True
    else:
        return False

def get_menu():
    name = input("Please enter your name:\n")
    surname = input("Please enter your surname:\n")
    student_no = input("Please enter your student number:\n")
    exam_note = input("Please enter your exam note:\n")
    if check_input_to_number(exam_note):
        print("Your note is:  " + exam_note)
        exam_note = int(exam_note)
    else:
        print("Your note is: " + exam_note + " is not a number. Please enter a number\n")
        return get_menu()

    return name, surname, student_no, exam_note

def get_letter_grade(note):
    """
    Convert a note to a letter grade.
    """
    if note<= 100 and note >= 90:
        return "AA"
    elif note >= 85 and note <= 89:
        return "BA"
    elif note >= 80 and note <= 84:
        return "BB"
    elif note >= 75 and note <= 79:
        return "CB"
    elif note >= 65 and note <= 74:
        return "CC"
    elif note >= 60 and note <= 64:
        return "DC"
    elif note >= 50 and note <= 59:
        return "DD"
    else:
        return "FF"

def is_student_pass(letter_grade):
    """
    Check if a letter grade is a pass.
    """
    if letter_grade == "AA" or letter_grade == "BA" or letter_grade == "BB" or letter_grade == "CB" or letter_grade == "CC" or letter_grade == "DC" or letter_grade == "DD":
        return "Geçti"
    else:
        return "Kaldı"