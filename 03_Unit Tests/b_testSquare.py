from a_square import square 

def test_square():
    if square(2)!=4:
        print("unable to print 4")
    if square(3)!=9:
        print("unable to print 9")

def main():
    test_square()

if __name__=="__main__":
    main()

