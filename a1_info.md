1-oji pamoka

Ciklai yra neatsiejama bet kurios programavimo kalbos dalis. Python kalboje
svarbi ciklų sudedamoji dalis yra integruota funkcija range(). Jos pagalba
yra generuojamos įvairios sekos, užtikrinamas ciklų kartojimas. Šios
funkcijos elgsenai tirti sukuriame funkcijas, kurių vardas prasideda žodeliu
demo. Tokios funkcijos paprastai neatlieka jokios konkrečios užduoties, o
yra skirtos pademonstruoti kitų funkcijų veikimą.

Patikslinsime funkcijos veikimą, panaudodami matematinio intervalo sąvoką
[a : b), t.y. pusiau atviras intervalas, kur reikšmė a priklauso intervalui, b- ne.
Funkcija range() būtent ir generuoja reikšmes iš tokio intervalo. Bendrai
galimi tokie funkcijos panaudojimo variantai, kai intervalas [nuo : iki)
• range(nuo, iki, pokytis) – pokytis nurodomas konkrečiai;
• range(nuo, iki) – pokytis yra lygus vienetui;
• range(iki) – nuo yra 0, o pokytis yra lygus vienetui.

Kodėl naudojamas pusiau atviras intervalas? Todėl kad skirtumas iki - nuo
visada duoda elementų skaičių. Vieno argumento atveju parametras tiesiog
reiškia kartojimo skaičių. Jei mums reikia kad intervalas [a, b] būtų uždaras,
tai reikia rašyti range(a, b+1). Atkreipiami dėmesį, kad funkcija range() yra
skirta tik sveikiems skaičiams, realių skaičių atveju gaunama klaida.

Generuojamos reikšmės gali būti ir neigiamos. Pokytis taip gali būti
neigiamas, tokiu atveju seka bus mažėjanti.

Visą tą intervalų įvairovę galima išbandyti demonstracinių funkcijų pagalba.
Stebėkite gaunamus rezultatus, keiskite parametrus, kol įsitikinsite jog
supratote kaip veikia funkcijos.

Toliau patys parašykite funkciją, skirtą uždaro intervalo [a, b] kvadrato
reikšmių lentelei spausdinti. Išbandykite aritmetinės ir geometrinės progresijų
narių skaičiavimą.

Spausdinant realius skaičius yra svarbu apriboti ženklų po kablelio skaičių.
Tai atliekama funkcijos round(x, k) pagalba, kurios pagalba skaičius x yra
apvalinamas k skilčių po kablelio tikslumu.

Atkreipkite dėmesį, kad geometrinės progresijos nariai reiškia, kaip kinta
jūsų banko indėlis taikant skirtingas palūkanas ☺