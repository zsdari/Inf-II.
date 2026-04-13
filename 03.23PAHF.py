a = 1.0 # = 1 --> de a típusa float, ha a = 1 akkor int

#Kiíratás
print(a)
#print(_ * _) --> __\n
#print(_, _) _ _\n
#print(_, end="_") -> __ (és nem nyit új sort)
#print(f"_ {_}")

#logikai operátorok -> == != < > <= >=
#matematikai operátorok -> +, -, /, // -> egészrészes osztás, *, ** -> hatványozás,
#                                   % --> maradékot adja vissza egész osztás esetén

#tömbök () -> nem változtatható

tomb = ("monday", "tuesday","wednesday","thursday","friday","saturday","sunday")
        #lehet benne több féle változó is
#print(f"{tomb[0]}, {tomb[1]}, {tomb[2]}, {tomb[3]}, {tomb[4]}, {tomb[5]}, {tomb[6]}")

# listák [] -> módosíthatók, hivatkozás átadása, nem érték átadás

lista = ["alma", "körte", "banán", 7, 10, 4.5, True]
#lista.append() -> hozzáadás
#lista.remove() -> adott elem eltávolítása
#lista.pop() -> adott helyiértékű elem eltávolítása
#lista.insert() -> adott helyiértékre elem beillesztése
#lista.copy() -> másolatot készít a listáról
print(lista)
lista.remove("banán")
print(lista)
lista.pop(5)
print(lista)
#lista indexelés

lista2 = lista #ha lista2 = lista.copy() --> nem fog változni ha lista változik mert átmásoltuk az értékeket
print(lista2)
lista.append("klima")
print(lista2) #ehhez is hozzáteszi a klima-t mert a hivatkozás van csak átadva

#indexelés -> lista[2] ==> lista 3. eleme

#feltétel

# if _feltétel_:
    #bentebb
# elif _feltétel_:
    #bentebb
# else:
    #bentebb

#ciklusok:
#while _feltétel_:
    #bentebb
    #while True
        #if _feltétel_:
            #break
#for _adott-elem_ in _lista/range/több-elem_:
    #bentebb
    #pl.: for e in lista --> e mint elem
    #           print(e) --> kiírja soronként a lista elemeit
    #           Kimenet:
    #                     3
    #                     4
                         #5
    #for e in range (0,10)
    #      print(e) --> 0,1 ... 9 írja ki

#random
#range() -> felső határ nincs benne --> range(0,10) == [0,1,2,3,4,5,6,7,8,9]