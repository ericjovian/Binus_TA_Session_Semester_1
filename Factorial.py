x = int(input("Number:"))
f = 1

if x == 0:
    print("1")
elif x < 0:
    print("Wrong Input")
else:
    for i in range(1,x+ 1):
         f = f*i
    print(f)