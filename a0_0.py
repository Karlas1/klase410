# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3N2P

from datetime import date, timedelta

def sveikinti(vardas):
    print("Sveikas pasauli!", end=' ')
    print("Mano vardas yra", vardas)
    print("Ši diena", date.today())

sveikinti("Adomas") # išjunkite kai nereikės
# sveikinti("Ieva")   # išjunkite kai nereikės