print(" half pyramid pattern of stars * ")
x=int(input("Enter the number of the rows:"))
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()