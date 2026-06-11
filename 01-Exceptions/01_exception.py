'''The Looop will continue untill the 
    user give me what i want! In our case 
    it is an integer
'''

while True:
    try:
        x=int(input("Enter a Number if you will :"))
    except ValueError:
        print(f"x is not an integer")
    else:
        break

print(f"x is {x}")

'''
The key word here is :
1. try
2. except
3. else
4. break
5. ValueError
'''

'''
And of course we can resolve it in different 
approch!
'''