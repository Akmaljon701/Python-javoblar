# if 13

a = float(input(" a = ")) 
b = float(input(" b = ")) 
c = float(input(" c = "))

if a>b and b>c or b>a and c>b :
    print("O'rtancha", b)
elif b>a and a>c or a>b and c>a:
    print("O'rtacha", a)
elif a>c and c>b or c>a and b>c:
    print("O'rtacha", c)
    