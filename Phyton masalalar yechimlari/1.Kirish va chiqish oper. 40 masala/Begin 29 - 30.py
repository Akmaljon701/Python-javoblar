#Begin 29 - 30

from cmath import pi

print(" 0 < a < 360 ")
Gradus_Radian = float(input(" Gradus - Radian = "))
Radian_Gradus = float(input(" Radian - Gradus = "))

radian = Gradus_Radian*(pi)/180
gradus = Radian_Gradus*(180/pi)

print(" Radian = ",radian, "\n Gradus = ", gradus)
