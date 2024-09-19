size = int(input("Enter the size of the pattern: "))
row = size
while row > 0 :
        for i in range(1,size+1) :
                print("*",end="")
        print("\n")
        row -= 1
