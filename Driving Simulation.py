#User Input
x=int(input("Time spent on the road(s):"))
y=int(input("Acceleration(m/s):"))
z=int(input("Distance(m):"))
i=0
#important variables
#Initial​ ​Velocity​ ​=​ ​Constant​ ​0​ ​m/s
#Speed​ ​Limit​ ​=​ ​Constant​ ​60​ ​m/s
while i <= x:
    print("Duration:",i,"Distance:","*" * int(0.05*i*i*y))
    i= i+1

u=y*i*i/2

if ((y*i) <60):
    print("The​ ​person​ went ​over​ ​the​ ​speed​ ​limit.(Max speed was ",y*i,"m/s)")
else:
    print("The​ ​person​ ​did​ ​not​ ​go​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was​ ",y*i,"m/s)")

if u>=z:
    print("The​ ​person​ ​reached​ ​the​ ​destination.​ ​(Reached",u,"m)")
else:
    print("The​ ​person​ ​did​ ​not​ ​reach​ ​the​ ​destination.​ ​(Reached",u,"m)")