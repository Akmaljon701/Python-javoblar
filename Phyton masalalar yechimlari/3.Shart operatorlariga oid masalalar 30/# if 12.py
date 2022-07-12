# if 12

a = float(input(" a = ")) 
b = float(input(" b = ")) 
c = float(input(" c = "))

if a>c and b>c and (a>b or b>a):
    print("Eng kichigi",c)
elif a>b and c>b and (a>c or c>a):
    print("Eng kichigi",b)
elif b>a and c>a and (b>c or c>b):
    print("Eng kichigi",a)
    
    











# abs_sonlar = []

# abs_sonlar.append(a)
# abs_sonlar.append(b)
# abs_sonlar.append(c)

# print(min(abs_sonlar))
     
