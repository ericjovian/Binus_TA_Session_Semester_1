x=input("Input :$")
x=float(x)

if x>=0 and x<200.01:
    print("Commision :$",(0.05*x))
elif x>=200.01 and x<1000.01:
    print("Commision :$",((200*0.05)+((x-200)*0.08)))
elif x>=1000.01 and x<2000.01:
    print("Commision :$",((200*0.05)+(800*0.08)+((x-1000)*0.1)))
elif x>=2000.01:
    print("Commision :$",((200*0.05)+(800*0.08)+(1000*0.1)+((x-2000)*0.12)))
else:
    print("Wrong Input")