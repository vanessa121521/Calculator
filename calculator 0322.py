x = input("Give me a number >")
def validate_int (x):
     try:
           int (x)
           return True
     except Exception:
          return False
while validate_int(x) == False:
     x = input('I SAID A NUMBER >')
     
op = int(input( "Enter 1 for + \nEnter 2 for - \nEnter 3 for × \nEnter 4 for ÷\n"))
y = input("to >")
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
     print("you did something wrong, please start over.")

