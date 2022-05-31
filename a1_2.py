# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3O74

def demo_intervalas3(nuo, iki, pokytis):
    print("(", nuo, iki , pokytis, ") ->", end=' ')
    for sk in range(nuo, iki, pokytis):
        print(sk, end=' ')
    print()

print("intervalinis ciklas su 3 parametrais")
demo_intervalas3(1, 6, 2)
demo_intervalas3(2, 11, 3)
demo_intervalas3(-2, 5, 2)
demo_intervalas3(11, 5, -1)