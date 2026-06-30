def main():
    x=int(input("Enter a integer: "))
    print(f"The square is :{square(x)}")

def square(n):
    return n+n

if __name__=="__main__": # main should not be always called!
    main()
