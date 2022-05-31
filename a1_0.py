# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3O74

def demo_intervalas1(kiek):
    print("(", kiek, ") ->", end=' ')
    for sk in range(kiek):
        print(sk, end=' ')
    print()

print("intervalinis ciklas su 1 parametru")
demo_intervalas1(5)
demo_intervalas1(11)