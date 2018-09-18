x=input("Input GPA:")
x=float(x)

if x>=3.5 and x<=4.0:
    print("Cumlaude")

elif x>=3.0 and x<3.55:
    print("Outstanding")

elif x>=2.5 and x<3.0:
    print("Very Good")

elif x>=2.0 and x<2.5:
    print("Good")

elif x<2.0 and x>=0:
    print("Poor")

else:
    print("Wrong Input")