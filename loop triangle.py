#TASK 1
rows=int(input("enter rows"))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()
#TASK 2
rows=int(input("enter rows"))
columns=int(input("enter rows"))
for i in range(1,rows+1):
    for j in range(i,columns+1):
        print("*",end=" ")
    print()
#TASK 3
rows=int(input("enter rows"))
for i in range(1,rows+1):
    for j in range(i,rows):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
#TASK 4
rows=int(input("enter rows"))
columns=int(input("enter columns"))
for i in range(1,rows+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(i,rows+1):
        print("*",end=" ")
    print()
