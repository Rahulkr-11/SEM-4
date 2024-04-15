#WAP to compute distance between two points using pythagorean theorem

def distance(x1, y1, x2, y2):
   
  # Calculating distance
   
  return (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
 

x1 = int (input("x1 : "))
y1 = int (input("y1 : "))
x2 = int (input("x2 : "))
y2 = int (input("y2 : "))
result = distance(x1,y1, x2, y2)
print ("Distance between the given points : ", result)