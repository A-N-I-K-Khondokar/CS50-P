
''' 
why not make the code more cleaner.
we can use function!
'''

def getInt():
    while True:
        try:
            x=int(input("Enter a Number :"))
        except ValueError:
            print(f"x is not an integer!")
        else:
            break
    
    return x

#print(getInt())


"""
we can do more compact with
** return** keyword!
"""

def GetInt():
    while True:
        try:
            return int(input("Enter a Number :"))
        except ValueError:
            pass


print(GetInt())

"""
CAREFULL with function name!
"""