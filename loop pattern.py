#TASK 1
rows=int(input("enter rows"))
columns=int(input("enter columns"))
for i in range(1,rows+1):
    for j in range(1,columns+1):
        print(i,end=" ")
    print()
#TASK 2
rows=int(input("enter rows"))
columns=int(input("enter columns"))
for i in range(1,rows+1):
    for j in range(1,columns+1):
        print(j,end=" ")
    print()
#TASK 3
rows=int(input("enter rows"))
columns=int(input("enter columns"))
n=0
for i in range(1,rows+1):
    for j in range(1,columns+1):
        n+=1
        print(n,end=" ")
    print()
#TASK 4        
rows=int(input("enter rows"))
columns=int(input("enter columns"))
n=0
for i in range(1,rows+1):
    for j in range(1,columns+1):
        n+=1
        print(chr(64+n),end=" ")
    print()
