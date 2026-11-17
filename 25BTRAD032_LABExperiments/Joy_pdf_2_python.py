"""
Lab Experiment 2
Name : EDWARD PHILIP
USN  : 25BTRAD032
"""


# ============================================================
# Ex 5: Number guessing game
# ============================================================
def ex5_guessing_game():
    import random

    number = random.randint(1, 100)

    print("Number Guessing Game")
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

# ============================================================
# Ex 6: Prime number and factorial
# ============================================================
def ex6_prime_factorial():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(num, "is not a prime number")
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")

    # Factorial Program
    n = int(input("\nEnter a number to find factorial: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial of", n, "is", factorial)

# ============================================================
# Ex 7: Fibonacci using recursion
# ============================================================
def ex7_fibonacci():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


    terms = int(input("Enter the number of terms: "))
    print("Fibonacci Series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")


# ============================================================
# MAIN MENU
# ============================================================
EXERCISES = [
    ("Ex 5: Number guessing game", ex5_guessing_game),
    ("Ex 6: Prime number and factorial", ex6_prime_factorial),
    ("Ex 7: Fibonacci using recursion", ex7_fibonacci),
]


if __name__ == "__main__":
    while True:
        print("\n===== Lab Experiment 2 =====")
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
