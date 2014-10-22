# Takes an integer and returns the factorial of that number

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total = total*i
    return total

# Main
number = int(raw_input("Type number: "))
print ("The factorial of %d is %d.") %(number, factorial(number))
