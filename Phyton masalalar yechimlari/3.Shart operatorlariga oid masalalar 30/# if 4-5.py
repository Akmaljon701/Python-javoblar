# if 4-5
a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))

manfiy = []
musbat = []

if a >= 0:
    musbat.append(a)
else:
    manfiy.append(a)

if b >= 0:
    musbat.append(b)
else:
    manfiy.append(b)
    
if c >= 0:
    musbat.append(c)
else:
    manfiy.append(c)    
    
print("manfiy = ", manfiy)
print("musbat = ", musbat)
manfiylar = len(manfiy)
musbatlar = len(musbat)
print("\n")
print(" Manfiylar soni: ", manfiylar, "ta.")
print(" Musbatlar soni: ", musbatlar, "ta.")