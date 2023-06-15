##NESTED IF:- 
a=int(input("enter your mark"))
if(a>=60):
    print("you are eligible")
    if(a>=75):
        print("you are eligible with merit quota")
    else:
        print("you are eligible in self finance")
else:
    print("you are not eligible")
    
##ELIF:-
a=int(input("enter your mark"))
if a>=80:
      print("passed with distinction")
elif a>=60:
    print("passed in first class")
elif a>=40:
    print("passed in second class")
else:
    print("ARREAR")

