# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3N2P

from datetime import date, timedelta

def kiek_gyventa(vardas, metai, mėnuo, diena):
    šiandien = date.today()
    pradinė_data = date(metai, mėnuo, diena)
    trukmė = šiandien - pradinė_data
    print(vardas, "jau gyvena", trukmė)

kiek_gyventa("Aleksander", 2006, 3, 26) # atidenkite kai reikės
# kiek_gyventa("Millennium", 2000, 1, 1)  # atidenkite kai reikės