# Problem 1-2: Simplifying Code
# Given the function below, refactor it for better readability by renaming variables and adding comments:
def f(lst):
    s = 0
    for n in lst:
        s += n
    return s / len(lst)


# Problem 3: Improving Code Structure
# Refactor the following function to allow it to work with any number of grades, instead of just three:
def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3


# Problem 4: Refactor this function to avoid repeated calculations:
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total = principal + (principal * rate * time) / 100
    return total
