# Take a positive integer n and returns the sum of all the digits of that number. From CodeAcademy

def digit_sum(n):
    number = str(n)
    dig_sum = 0
    for digit in number:
        print digit + '+ ',
        dig_sum += int(digit)
    return dig_sum

n = raw_input('Type a number: ')
print ('The sum of digits is: %d') %(digit_sum(n))
