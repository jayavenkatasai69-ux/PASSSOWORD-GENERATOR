import random
digits = int(input("Enter number of digits for number "))
num = ''.join([str(random.randint(0, 9)) for _ in range(digits)])

print("Your password is:", num)
