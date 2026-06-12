import sys

if len(sys.argv)<2:
    sys.exit("Too few argumnet")
elif len(sys.argv)>2:
    sys.exit("Too much argument")


print(f"Hello,{sys.argv[1]}")

'''
sys.argv[0] is here the "04_sys_conditional"
this is the first argumnet!
'''