import random


#peksutemenyek = ["kifli", "kakaoscsiga", "brios"]

#1. feladat
kifli = []
kakaoscsiga = []
brios = []

for i in range(0,30):
    kifli.append(random.randint(0,50))#benne van az 50 is így!!!
#for i in range(0,30): elég 1 ciklus!!!
    kakaoscsiga.append(random.randint(0,50))#benne van az 50 is így!!!
#for i in range(0,30): elég 1 ciklus!!!
    brios.append(random.randint(0,50))#benne van az 50 is így!!!

#print(kifli)
#print(kakaoscsiga)
#print(brios)
#print(len(kifli), len(kakaoscsiga), len(brios))

#2. feladat
print("Nap", "\t", "Kifli", "\t","Kakaoscsiga","\t","Brios")
for i in range(0, 30):
    print(f"{i+1}. nap:\t{kifli[i]}\t{kakaoscsiga[i]}\t{brios[i]}")
#VAGY ÍGY:
#i = 0
# while i < len(kifli)
#    print(f"{i+1}. nap:\t{kifli[i]}\t{kakaoscsiga[i]}\t{brios[i]}")
#    i += 1


#3. feladat
kifliosszeg = 0
csigaosszeg = 0
briososszeg = 0
for i in kifli:
    kifliosszeg += i
for i in kakaoscsiga:
    csigaosszeg += i
for i in brios:
    briososszeg += i

print(f"Összesen {kifliosszeg+csigaosszeg+briososszeg} terméket "
      f"adtak el a hónapban, ebből kifli: {kifliosszeg}, kakaoscsiga: {csigaosszeg}"
      f", brios: {briososszeg}")

#4. feladat

legtobbk = 0 #kilfi[0]
legtobbcs = 0 #kakaoscsiga[0]
legtobbb = 0 #brios[0]
legkevesebbk = 51 #kilfi[0]
legkevesebbcs = 51 #kakaoscsiga[0]
legkevesebbb = 51 #brios[0]

i = 0
while i < len(kifli):
    if legtobbk < kifli[i]:
        legtobbk = kifli[i]
    if legtobbcs < kakaoscsiga[i]:
        legtobbcs = kakaoscsiga[i]
    if legtobbb < brios[i]:
        legtobbb = brios[i]
    if legkevesebbk > kifli[i]:
        legkevesebbk = kifli[i]
    if legkevesebbcs > kakaoscsiga[i]:
        legkevesebbcs = kakaoscsiga[i]
    if legkevesebbb > brios[i]:
        legkevesebbb = brios[i]
    i += 1

print(f"Kifliből a legtöbb: {legtobbk}, a legkevesebb: {legkevesebbk}")
print(f"Kakóscsigából a legtöbb: {legtobbcs}, a legkevesebb: {legkevesebbcs}")
print(f"Briósból a legtöbb: {legtobbb}, a legkevesebb: {legkevesebbb}")

#5. feladat
i = 0
while i < len(kifli):
    if legtobbk == kifli[i]:
        print("Legtobb kiflit elsőnek a ", i+1, ". napon adták el.")
    if legtobbcs == kakaoscsiga[i]:
        print("Legtobb kakaoscsigat elsőnek a ", i+1, ". napon adták el.")
    if legtobbb == brios[i]:
        print("Legtobb briost elsőnek a ", i+1, ". napon adták el.")
    i += 1

#6. feladat
hetnapjai = ("hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat", "vasarnap")

for i in range(0,30):
    print(hetnapjai[i % 7], end=":\t")
    print('\t', kifli[i], "\t", kakaoscsiga[i], "\t", brios[i])
    if i % 7 == 6:
        print()
