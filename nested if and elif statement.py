#QUESTION NO:1
a=int(input("Enter the units consumed"))
b=(a-100)*5
c=(100*5)+(a-200)*10
d=(100*5)+(100*10)+(a-300)*20
if a<=100:
    print("no charges, Total bill:Rs.0")
elif a>100 and a<=200:
    print("Total Bill: Rs.",+b)
elif a>200 and a<=300:
    print("Total Bill: Rs."+c)
else:
    print("Total Bill: Rs.",+d)
#QUESTION NO:2
a=int(input("enter your marks"))
if a>90:
    print("A Grade")
elif a>80 and a<=90:
    print("B Grade")
elif a>=60 and a<=80:
    print("C Grade")
else:
    print("D Grade")
#QUESTION NO:3
a=int(input("Enter the cost price of the bike"))
b=int(a*5/100)
c=int(a*10/100)
d=int(a*15/100)
if a>100000:
    print("Road Tax: Rs.",+d)
elif a>50000 and a<=100000:
    print("Road Tax: Rs.",+c)
else:
    print("Road Tax: Rs.",+b)
#QUESTION NO:4
a=int(input("Enter week number"))
if a>0 and a<8:
    if a==1:
        print("Sunday")
    elif a==2:
        print("Monday")
    elif a==3:
        print("Tuesday")
    elif a==4:
        print("Wednesday")
    elif a==5:
        print("Thursday")
    elif a==6:
        print("Friday")
    elif a==7:
        print("Saturday")
else:
    print("enter the valid input")
#QUESTION NO:5
a=int(input("Enter month number"))
if a>0 and a<13:
    if a==1:
        print("JANUARY and No.of.Days=31")
    elif a==2:
        print("FEBRUARY and No.of.Days=28")
    elif a==3:
        print("MARCH and No.of.Days=31")
    elif a==4:
        print("APRIL and No.of.Days=30")
    elif a==5:
        print("MAY and No.of.Days=31")
    elif a==6:
        print("JUNE and No.of.Days=30")
    elif a==7:
        print("JULY and No.of.Days=31")
    elif a==8:
        print("AUGUST and No.of.Days=31")
    elif a==9:
        print("SEPTEMBER and No.of.Days=30")
    elif a==10:
        print("OCTOBER and No.of.Days=31")
    elif a==11:
        print("NOVEMBER and No.of.Days=30")
    elif a==12:
        print("DECEMBER and No.of.Days=31")
else:
    print("enter the valid input")
#QUESTION NO:6
a=int(input("enter the value of 1st side"))
b=int(input("enter the value of 2nd side"))
c=int(input("enter the value of 3rd side"))
if a==b==c:
    print("The sides denote equilateral triangle")
elif a!=b and b==c or a==b and b!=c or a==c and c!=b:
    print("The sides denote Isosceles triangle")
else:
    print("The sides denote Scalene triangle")
#QUESTION NO:7
a=int(input("enter Year"))
if a%4==0 and a%100==0 and a%400==0:
    print(a,"is a Leap Year")
else:
    print(a,"is not a Leap Year")
#QUESTION NO:8
a=int(input("enter 'a' value"))
b=int(input("enter 'b' value"))
c=int(input("enter 'c' value"))
if a>b and a>c:
    if b<a and b>c:
        print("B is the second largest number")
    if c<a and c>b:
        print("C is the second largest number")
elif c>a and c>b:
    if b<c and b>a:
        print("B is the second largest number")
    if a<c and a>b:
        print("A is the second largest number")
elif b>a and b>c:
    if a<b and a>c:
        print("A is the second largest number")
    if c<b and c>a:
         print("C is the second largest number")
#QUESTION NO:9
a=int(input("enter 'a':"))
b=int(input("enter 'b':"))
c=str(input("enter mathematical operator:"))
if c=="-":
    print(a-b)
elif c=="+":
    print(a+b)
elif c=="/":
    print(a/b)
elif c=="*":
    print(a*b)
elif c=="**":
    print(a**b)
elif c=="%":
    print(a%b)


        

    



    


    

