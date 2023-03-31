x = input("Give me a number >")  #how to add break in the first line?
def validate_int (x):
     try:
           int (x)
           return True
     except Exception:
          return False
while validate_int(x) == False:
     x = input('I SAID A NUMBER or enter q to quit >')
     if x == 'q':
          break
     
     
s = {1, 2, 3, 4}
op = int(input( "Enter 1 for + \nEnter 2 for - \nEnter 3 for × \nEnter 4 for ÷ >"))
if op not in s:
     op = input( "\nInvalid input, try again \nEnter 1 for + \nEnter 2 for - \nEnter 3 for × \nEnter 4 for ÷ >")
     
y = input("\nto >")
def validate_int (y):
     try:
           int (y)
           return True
     except Exception:
          return False   
while validate_int(y) == False:
     y = input('A NUMBER >')
     
x = int(x)
y = int(y)
          
if op == 1:
     print("{}+{}=".format(x, y), x+y)
elif op == 2:
     print("{}-{}=".format(x, y), x-y)
elif op == 3:
     print("{}x{}=".format(x, y), x*y)
elif op == 4:
     print("{}÷{}=".format(x, y), x/y)
else:
     print("I don't know but something went wrong")




