# aktyvus mokymas, ruošė eimutis.karciauskas@ktu.lt
# https://www.jdoodle.com/a/3O74

# http://www.mat.lt/matematikos-formules/progresijos.html

def geom_progresija(a0, q, n):
    gn = a0 # geom. progresijos narys
    for i in range(n):
        print(round(gn, 2), end=' ')
        gn *= q
    print("fin")

print("Geometrinės Progresijos nariai")
geom_progresija(10, 1.10, 6)
#geom_progresija(10, 1.05, 6)