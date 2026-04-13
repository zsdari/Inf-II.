import random
from operator import index


def generalas():
    lista = []
    for hallgato in range (random.randint(15,20)):
        hallgato_eredmenyei = []
        for feladat in range (10):
            hallgato_eredmenyei.append(random.randint(0,8))
        lista.append(hallgato_eredmenyei.copy())
    return lista

eredmenyek = generalas()
# print(eredmenyek)

print(f'A számonkérést {len(eredmenyek)} személy írta meg.\n'
      f'A számonkérésről {20-len(eredmenyek)} hiányoztak')

def ket_nulla(lista):
    rossz_hallgatok = 0
    for hallgato in lista:
        count = 0
        for feladat in hallgato:
            if feladat == 0:
                count += 1
        if count == 2:
            rossz_hallgatok += 1

    return rossz_hallgatok

print(f'\n{ket_nulla(eredmenyek)} hallgató írt legalább 2 nulla pontos feladatot')

def vanmax(lista, max_pont):
    # jo_hallgato = 0
    # for hallgato in lista:
    #     for feladat in hallgato:
    #         if feladat == max_pont:
    #             return ;
    #             break
    nincs_ilyen = True
    i = 0
    while i < len(lista) and nincs_ilyen:
            j = 0
            while j < len(lista[i]):
                if lista[i][j] == max_pont:
                    nincs_ilyen = False
                    break
                j += 1
            i += 1
    return i

print(f'\n{vanmax(eredmenyek, 8)} hallgato írta az elso maxpontos feladatot')

def atlagmin4(lista):
    count_min4 = 0
    for hallgato in lista:
        osszepontszam = 0
        for feladat in hallgato:
            osszepontszam += feladat
        if (osszepontszam / 10) >= 4:
            count_min4 += 1
    return count_min4

print(f'\n{atlagmin4(eredmenyek)} hallgato érte le a 4-es átlag pontszámot\n')


def atlag(lista):
    k = 1
    for hallgato in lista:
        osszepontszam = 0
        for feladat in hallgato:
            osszepontszam += feladat
        print(f'{k}. hallgato atlag pontja: {osszepontszam/10}')
        k += 1

atlag(eredmenyek)
print()
def feladatok_szazalek(lista, max_feladat):
    feladatok_osszpontszama = []
    # for e in range(max_feladat):
    #     feladatok_osszpontszama.append(0)
    for e in range(len(lista[0])):
        feladatok_osszpontszama.append(0)

    i = 0
    while i < len(lista):
        j = 0
        while j < len(lista[i]):
            feladatok_osszpontszama[j] += lista[i][j]
            j += 1
        i += 1
    k = 1
    for feladat in feladatok_osszpontszama:
        szazalek = feladat / (len(lista) * 8)*100
        print(f'{k}. feladat {round(szazalek,2)} %')
        k += 1

feladatok_szazalek(eredmenyek, 10)
print()

def hallgatok_szazaleka(lista, maxpont):
    erdemjegyek_lista = []
    szazalek_lista = []
    k = 1
    for hallgato in lista:
        osszpontszam = 0
        for feladat in hallgato:
            osszpontszam += feladat

        szazalek = (osszpontszam / (maxpont * (len(lista[0]))))

        if szazalek >= 0.85:
            erdemjegyek_lista.append(5)
            print(f'{k}. hallgato: {round(szazalek * 100,2)} %, érdemjegy: 5')
        elif szazalek >= 0.75:
            print(f'{k}. hallgato: {round(szazalek * 100, 2)} %, érdemjegy: 4')
            erdemjegyek_lista.append(4)
        elif szazalek >= 0.65:
            erdemjegyek_lista.append(3)
            print(f'{k}. hallgato: {round(szazalek * 100,2)} %, érdemjegy: 3')
        elif szazalek >= 0.48:
            erdemjegyek_lista.append(2)
            print(f'{k}. hallgato: {round(szazalek * 100, 2)} %, érdemjegy: 2')
        else:
            erdemjegyek_lista.append(1)
            print(f'{k}. hallgato: {round(szazalek * 100, 2)} %, érdemjegy: 1')
        szazalek_lista.append(szazalek)
        k += 1
    return erdemjegyek_lista, szazalek_lista

eredmenyek_lista = hallgatok_szazaleka(eredmenyek, 8)
print()
print(eredmenyek_lista)

def legjobb_hallgatok(lista):
    max_szazalek = lista[0]
    for szazalek in lista:
        if szazalek > max_szazalek:
            max_szazalek = szazalek

    k = 0
    while k < len(lista):
        if lista[k] == max_szazalek:
            print(f'\n{k + 1}. hallgato erte el a legjobb eredmenyt.\n')
        k += 1

legjobb_hallgatok(eredmenyek_lista[1])