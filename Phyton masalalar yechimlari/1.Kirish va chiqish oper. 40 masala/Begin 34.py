#Begin 34

x_shokolad = float(input(" X kg shokolad = "))
a_som = float(input(" X kg shokolad A so'm = "))
y_konfet = float(input(" Y kg konfet = "))
b_som = float(input(" Y kg konfet B so'm = "))

birkgshokolad = a_som/x_shokolad
birkgkonfet = b_som/y_konfet

shok_konf = birkgshokolad - birkgkonfet

if (birkgshokolad>birkgkonfet):
    print(" 1 kg Shokolad 1 kg konfetdan ", shok_konf, " so'm qimmat.")

elif (birkgkonfet==birkgshokolad):
    print(" 1 kg Shokolad va 1 kg Konfet narxlari teng. 1 kg si ", birkgkonfet, " so'mdan. ")
    
else:
    print(" 1 kg Shokolad 1 kg konfetdan ", abs(shok_konf), " so'm arzon. ")
