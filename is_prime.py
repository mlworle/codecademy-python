def is_prime(x):
    if x < 2:
        return False
        print ('Composite')
    elif x ==2:
        return True
        print ('Prime')
    else:
        for n in range (2,x-1):
            if x % n == 0:
                return False
                print ('Composite')
        return True
        print ('Prime')

number = int(raw_input('Type number: '))
print ('the number is %d') %(number)
answer = is_prime(number)
if answer == True:
    print ('The number %d is prime.') %(number)
else:
    print ('The number %d is composite.') %(number)
