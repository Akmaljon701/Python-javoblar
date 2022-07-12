#Begin 39

print(" Ax^2 + Bx + C ")
A = float(input(" A = "))
B = float(input(" B = "))
C = float(input(" C = "))

D = B**2 - 4*A*C
x1 = (-B + (D)**(1/2))/2*A
x2 = (-B - (D)**(1/2))/2*A

if (D>=0):
    print(" x1 = ",x1, "\n x2 = ",x2)
else:
    print(" D>=0 bo'lishi shart!")