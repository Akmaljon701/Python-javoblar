#Begin 18

print(" A,B,C nuqtalarni kiriting. C nuqta A va B nuqtalar orasida joylashgan.")
A = float(input(" A = "))
B = float(input(" B = "))
C = float(input(" C = "))

AC = abs(C - A)
BC = abs(C - B)
kopaytma = AC*BC

print("AC * BC = ", kopaytma)