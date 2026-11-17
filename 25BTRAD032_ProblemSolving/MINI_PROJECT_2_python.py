"""
Mini Project 2
Name : EDWARD PHILIP
USN  : 25BTRAD032
"""


# ============================================================
# OTP generator
# ============================================================
def otp_generator():
    import random

    otp = random.randint(100000, 999999)
    print("Your OTP is:", otp)

    user_otp = int(input("Enter the OTP: "))

    if user_otp == otp:
        print("OTP Verified Successfully!")
    else:
        print("Invalid OTP!")

# ============================================================
# Student grading automation
# ============================================================
def student_grading():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "F"

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)

    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


# ============================================================
# MAIN MENU
# ============================================================
EXERCISES = [
    ("OTP generator", otp_generator),
    ("Student grading automation", student_grading),
]


if __name__ == "__main__":
    while True:
        print("\n===== Mini Project 2 =====")
        for i, (label, _) in enumerate(EXERCISES, 1):
            print(f"{i}. {label}")
        print("0. Exit")
        pick = input("Choose a program to run: ")
        if pick == "0":
            break
        if pick.isdigit() and 1 <= int(pick) <= len(EXERCISES):
            print()
            EXERCISES[int(pick) - 1][1]()
        else:
            print("Invalid choice.")
