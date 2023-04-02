q = input("Hello, your dumbass calculator! :D \n\nPress any key to continue \npress q to quit \t>")
while q != 'q':
    x = input("\nFeed me a number \npress q to quit \t>")  #how to add break in the first line?
    def validate_int (x):
        try:
            int (x)
            return True
        except Exception:
            return False
    while validate_int(x) == False:
        x = input('hey it has to be a number :( >')
        if x == 'q':
            print ('okay, bye-bye')
            break
    
    
    s = {1, 2, 3, 4}
    op = input( "Enter 1 for + \nEnter 2 for - \nEnter 3 for × \nEnter 4 for ÷ >")
    def validate_op (op):
        try:
            int(op)
        except Exception:
            return False
        except int(op) not in s:
            return False
    while validate_op (op) == False:
        op = input( "\nhmm, nope... try again \nEnter 1 for + \nEnter 2 for - \nEnter 3 for × \nEnter 4 for ÷ >") 
    
    y = input("\nanother number >")
    def validate_int (y):
        try:
            int (y)
            return True
        except Exception:
            return False   
    while validate_int(y) == False:
        y = input('A NUMBER! >')
    
    x = int(x)
    y = int(y)
    op = int(op)
    
    if op == 1:
        print("\n{}+{}=".format(x, y), x+y, "\t(hopefully it's correct)")
    elif op == 2:
        print("\n{}-{}=".format(x, y), x-y, "\t(should be right...)")
    elif op == 3:
        print("\n{}x{}=".format(x, y), x*y, "\t:D?")
    elif op == 4:
        print("\n{}÷{}=".format(x, y), x/y, "\t(this one is not easy tho)")
    else:
        print("\nI don't know but something went wrong lol")
while q == 'q':
    print('okay, bye!')
    break
    
    