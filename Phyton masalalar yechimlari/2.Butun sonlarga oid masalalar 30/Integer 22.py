#Integer 22

sek = float(input(" Kun boshidan boshlab necha sekund vaqt o'tdi: "))

soat = (sek/60)//60
qolgabsekund1 = soat * (60**2)
qolgabsekund2 = sek - qolgabsekund1

print(" Kun boshidan boshlab",soat, "soat", qolgabsekund2,"sekund vaqt o'tdi. ")
