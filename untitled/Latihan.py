x=input("Input Salary:$")
x=float(x)

if x>=0 and x<5000:
    print("Income tax rate:0%")

elif x>=5000 and x<10000:
    print("Income tax rate:6%")

elif x>=10000 and x<20000:
    print("Income tax rate:15%")

elif x>=20000 and x<30000:
    print("Income tax rate:20%")

elif x>=30000 and x<40000:
    print("Income tax rate:25%")

elif x>=40000:
    print("Income tax rate:30%")

else:
    print("Wrong Input")