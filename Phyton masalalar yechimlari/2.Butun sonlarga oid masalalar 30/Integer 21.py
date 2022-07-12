#Integer 21

sek = float(input(" Kun boshidan boshlab necha sekund vaqt o'tdi: "))

minut = sek//60
qolgabsekund1 = minut * 60
qolgabsekund2 = sek - qolgabsekund1

print(" Kun boshidan boshlab",minut, "minut", qolgabsekund2,"sekund vaqt o'tdi. ")