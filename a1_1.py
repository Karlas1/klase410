# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3O74

def demo_intervalas2(nuo, iki):
    print("(", nuo, iki , ") ->", end=' ')
    for sk in range(nuo, iki):
        print(sk, end=' ')
    print()

print("intervalinis ciklas su 2 parametrais")
demo_intervalas2(1, 4)
demo_intervalas2(3, 12)
demo_intervalas2(-2, 5)