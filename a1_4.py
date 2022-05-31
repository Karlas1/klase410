# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3O74

# http://www.mat.lt/matematikos-formules/progresijos.html

def arit_progresijos_suma(a0, d, n):
    print("(", a0, d , n, ") ->", end=' ')
    s = 0
    for a in range(a0, a0 + d*n, d):
        print(a, end=' ')
        s += a
    print("Suma=", s)

print("Aritmetinės Progresijos Suma")
arit_progresijos_suma(5, 2, 4)
#arit_progresijos_suma(2, -1, 5)