#!/usr/bin/env/python3

def main():
    students = [
        "Amir", "Breana", "Katie", "Clayton", "Coty", "Daiyron",
        "Douglas", "Gabriel", "Jakira", "John", "Jonathan",
        "Justin", "Megan", "Tayo", "Summer", "Tomiwa"
               ]

    headcount = len(students)

    str_number = input(f"Pick a number between 1 and {headcount}: ")

    int_number = int(str_number) - 1

    student_choice = students[int_number]

    print(f"{student_choice} is AWESOME!")

main()




