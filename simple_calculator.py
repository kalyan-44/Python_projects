def addition(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b!=0:
    return a/b
  return "Error. Cannot divide with zero"
print('Simple Calculator')
print('-'*len('Simple Calculator'))
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
choice=input('Enter your choice:')
first_number=float(input('Enter first Number: '))
second_number=float(input('Enter second Number: '))
if choice=='1':
  result=addition(first_number,second_number)
elif choice=='2':
  result=subtract(first_number,second_number)
elif choice=='3':
  result=multiply(first_number,second_number)
elif choice=='4':
  result=divide(first_number,second_number)
else:
  print('Invalid Input')
print('Result= ',result)
