"""
Lab Experiment 1
Name : EDWARD PHILIP
USN  : 25BTRAD032
"""


# ============================================================
# Ex 2: Hello name
# ============================================================
def ex2_hello_name():
    name = "Edward Philip"
    print("My name is", name)

# ============================================================
# Ex 2: Sum of two numbers
# ============================================================
def ex2_sum():
    a = 10
    b = 20
    sum = a + b
    print("First number:", a)
    print("Second number:", b)
    print("Sum:", sum)

# ============================================================
# Ex 3: Sum and product (input)
# ============================================================
def ex3_sum_product():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)
    print("Product =", a * b)

# ============================================================
# Ex 3: Simple interest
# ============================================================
def ex3_simple_interest():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))

    si = (p * r * t) / 100
    print("Simple Interest =", si)

# ============================================================
# Ex 4: Simple calculator
# ============================================================
def ex4_calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

# ============================================================
# Ex 4: Area of circle
# ============================================================
def ex4_circle_area():
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of circle =", area)


# ============================================================
# MAIN MENU
# ============================================================
EXERCISES = [
    ("Ex 2: Hello name", ex2_hello_name),
    ("Ex 2: Sum of two numbers", ex2_sum),
    ("Ex 3: Sum and product (input)", ex3_sum_product),
    ("Ex 3: Simple interest", ex3_simple_interest),
    ("Ex 4: Simple calculator", ex4_calculator),
    ("Ex 4: Area of circle", ex4_circle_area),
]


if __name__ == "__main__":
    while True:
        print("\n===== Lab Experiment 1 =====")
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
