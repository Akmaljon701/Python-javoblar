#Begin 35

print(" V > U ")
V = float(input(" Qayiqning tezligi. V(km/s) = "))
U = float(input(" Daryoning tezligi. U(km/s) = "))
t1 = float(input(" Qayiqning daryo oqimi bo'ylab harakatlanish vaqti.\n t1 = "))
t2 = float(input(" Qayiqning daryo oqimiga qarshi harakatlanish vaqti.\n t2 = "))

#S1 oqim boylab
S1 = (V+U)*t1
S2 = (V-U)*t2
S_umumiy = S1+S2

print(" Umumiy bosin utilgan yo'l. S = ", S_umumiy)