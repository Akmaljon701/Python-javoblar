#Integer 23

sek = float(input(" Kun boshidan boshlab necha sekund vaqt o'tdi: "))

soat = (sek/60)//60

minut1 = sek - (soat*(60**2))
minut2 = minut1//60

sekund1 = sek - (soat*(60**2) + (minut2*60))

print(soat,"soat",minut2,"minut",sekund1,"sekund.")