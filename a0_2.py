# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3N2P

from datetime import date, timedelta

def kada_jubiliejus(kiek_dienų, metai, mėnuo, diena):
    gim_data = date(metai, mėnuo, diena)
    jub_data = gim_data + timedelta(kiek_dienų)
    print(kiek_dienų, "dienų jubiliejus bus", jub_data)

kada_jubiliejus(6000, 2006, 3, 26)
# kada_jubiliejus(8_000, 2000, 1, 1)
# kada_jubiliejus(10_000, 2000, 1, 1)