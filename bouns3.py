numbers = [1,2,3,4,5,6,7,8,9]
user = int(input("enter a number in the list: "))
if user in numbers:
    print(f'{user} is in the list of numbers')
else:
    print('invalid input')