x=input("Input Any Number:")
x=int(x)

i=0
while i<=x:
    print("*"*i)
    i=i+1

i=0
j=x
while i<=x:
    print(" "*j,"*"*i)
    i=i+1
    j=j-1

print("")

i=x
while i>=0:
    print("*"*i)
    i=i-1

i=0
j=x
while j>=0:
    print(" "*i,"*"*j)
    i=i+1
    j=j-1

i=1
j=x
k=1
while k<=x:
    print(" "*j,"*"*i)
    i=i+2
    j=j-1
    k=k+1


print("")

i=1
j=x
k=1
l=x
m=((x*2)-1)
n=1
while l>=0:
    while k<x:
        print(" "*j,"*"*i)
        i=i+2
        j=j-1
        k=k+1
    print(" "*n,"*"*m)
    l=l-1
    m=m-2
    n=n+1