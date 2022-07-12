#Begin 21 

print(" (x1,y1)(x2,y2)(x3,y3) ")
x1 = float(input(" x1 = "))
x2 = float(input(" x2 = "))
x3 = float(input(" x3 = "))

y1 = float(input(" y1 = "))
y2 = float(input(" y2 = "))
y3 = float(input(" y3 = "))

a = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
b = ((x2 - x3)**2 + (y2 - y3)**2)**(1/2)
c = ((x3 - x1)**2 + (y3 - y2)**2)**(1/2)

P = (a + b + c)/2
S = (P * (P-a)*(P-b)*(P-c))**(1/2)

print(" S = ", S)
print(" P = ", P)