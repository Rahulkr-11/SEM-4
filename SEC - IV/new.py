'''filename="meteor.txt"
line=reversed(list(open(filename)))
for l in line:
    print(l.rstrip())'''

import math
def ball_collide(x1,y1,r1,x2,y2,r2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2);
    print("Distance b/w two balls:",dist)
    center=dist/2;
    print("Collision point",center);
    r=r1+r2;
    print("Sum of radious",r)
    if(center<=r):
        print("They are Colliding")
        return True;
    else:
        print("Not Colliding")
        return False;

c=ball_collide(4,4,3,2,2,3)
print(c) 
c=ball_collide(100,200,20,200,100,10)
print(c) 