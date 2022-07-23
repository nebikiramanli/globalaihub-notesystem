import pandas as pd
import system_helper
import excel_helper
import dataframe_helper


def main():
    print("************** Welcome to the note system ************** \n")
    students_dataframe = pd.DataFrame()
    while True:
        print("If you want to exit, enter 'q or Q' / If you want to continue, enter 'c or C' to see the menu \n")

        input_choice = input("Enter your choice: \n")
        if input_choice == "q" or input_choice == "Q":
            if dataframe_helper.check_dataframe(students_dataframe):
                print("You have not entered any data yet\n")
            else:
                print("You have entered the following data:\n")
                print(students_dataframe)
                excel_helper.write_excel("notes.xlsx", students_dataframe)
            print("Goodbye")
            break   # break the loop
        elif input_choice == "c" or input_choice == "C":
            name, surname, student_no, exam_note = system_helper.get_menu()
            letter_grade = system_helper.get_letter_grade(exam_note)
            print("Your letter grade is: " + letter_grade)
            student_dataframe = dataframe_helper.to_dataframe([{"name": name, "surname": surname, "student_no": student_no, "exam_note": exam_note, "letter_grade": letter_grade}])
            student_status = system_helper.is_student_pass(letter_grade)
            
            if student_status:
                print("You passed the exam\n")
            
            student_dataframe = dataframe_helper.insert_column(student_dataframe, "student_status", student_status)
            student_data = dataframe_helper.delete_column(student_dataframe, "letter_grade")
            students_dataframe = dataframe_helper.insert_dataframe(students_dataframe, student_data)
                      
        else:
            print("Invalid input\n")
            continue

if __name__ == "__main__":
    main()
    exit(0)