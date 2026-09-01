x=int(input("Enter any number: "))
count=0
while x>0:
    x//=10
    count+=1
print("The number has", count, "digits.")