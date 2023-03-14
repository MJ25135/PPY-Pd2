pyt0 = input("Jak masz na imie oraz nazwisko? ")


print("1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: "
      "\n a. oglądanie telewizji/filmów/seriali"
      "\n b. czytanie książek/czasopism"
      "\n c. słuchanie muzyki"
      "\n d. spotkania z rodziną/przyjaciółmi"
      "\n e. podróżowanie"
      "\n f. uprawianie sportu"
      "\n g. inne, jakie?")

pyt1 = input("Podaj odpowiedz: ")
if pyt1 == "g":
    pyt1 = input("Wpisz jakie: ")
elif pyt1 == "a":
    pyt1 = "oglądanie telewizji/filmów/seriali"
elif pyt1 == "b":
    pyt1 = "czytanie książek/czasopism"
elif pyt1 == "c":
    pyt1 = "słuchanie muzyki"
elif pyt1 == "d":
    pyt1 = "spotkania z rodziną/przyjaciółmi"
elif pyt1 == "e":
    pyt1 = "podróżowanie"
elif pyt1 == "f":
    pyt1 = "uprawianie sportu"

print(pyt1)

print("2. W jakich okolicznościach czytasz książki najczęściej? "
      "\n a. podczas podróży"
      "\n b. w czasie wolnym (po pracy, na urlopie)"
      "\n c. podczas pracy/nauki (to ich element)"
      "\n d. w ogóle nie czytam"
      "\n e. inne, jakie?")

pyt2 = input("Podaj odpowiedz: ")
if pyt2 == "e":
    pyt2 = input("Wpisz jakie: ")
elif pyt2 == "a":
    pyt2 = "podczas podróży"
elif pyt2 == "b":
    pyt2 = "w czasie wolnym (po pracy, na urlopie)"
elif pyt2 == "c":
    pyt2 = "podczas pracy/nauki (to ich element)"
elif pyt2 == "d":
    pyt2 = "w ogóle nie czytam"

print(pyt2)

print("3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?  "
      "\n a. chęć poszerzenia wiedzy"
      "\n b. czytanie mnie relaksuje/odpręża"
      "\n c. fakt, że czytanie jest modne"
      "\n d. czytanie to moje hobby"
      "\n e. konieczność nauki w związku z wykonywaną pracą/studiami"
      "\n f. odczuwam presję rodziny/środowiska, żeby czytać"
      "\n g. inny, jakie?")

pyt3 = input("Podaj odpowiedz: ")
if pyt3 == "g":
    pyt3 = input("Wpisz jakie: ")
elif pyt3 == "a":
    pyt3 = "chęć poszerzenia wiedzy"
elif pyt3 == "b":
    pyt3 = "czytanie mnie relaksuje/odpręża"
elif pyt3 == "c":
    pyt3 = "fakt, że czytanie jest modne"
elif pyt3 == "d":
    pyt3 = "czytanie to moje hobby"
elif pyt3 == "e":
    pyt3 = "konieczność nauki w związku z wykonywaną pracą/studiami"
elif pyt3 == "f":
    pyt3 = "odczuwam presję rodziny/środowiska, żeby czytać"

print(pyt3)

print("4. Po książki w jakiej formie sięgasz najczęściej? "
      "\n a. papierowej (tradycyjnej)"
      "\n b. e-booki (książki elektroniczne) na komputerze"
      "\n c. e-booki na tablecie/telefonie"
      "\n d. e-booki na specjalnym czytniku (np. Kindle)")

pyt4 = input("Podaj odpowiedz: ")

if pyt4 == "a":
    pyt4 = "papierowej (tradycyjnej)"
elif pyt4 == "b":
    pyt4 = "e-booki (książki elektroniczne) na komputerze"
elif pyt4 == "c":
    pyt4 = "e-booki na tablecie/telefonie"
elif pyt4 == "d":
    pyt4 = "e-booki na specjalnym czytniku (np. Kindle)"

print(pyt4)

print("5. Ile książek czytasz średnio w ciągu roku?  "
      "\n a. 0"
      "\n b. żadnej w całości - jedynie fragmenty"
      "\n c. 2 lub 3"
      "\n d. 4-10"
      "\n e. powyżej 10")

pyt5 = input("Podaj odpowiedz: ")

if pyt5 == "a":
    pyt5 = "0"
elif pyt5 == "b":
    pyt5 = "żadnej w całości - jedynie fragmenty"
elif pyt5 == "c":
    pyt5 = "2 lub 3"
elif pyt5 == "d":
    pyt5 = "4-10"
elif pyt5 == "e":
    pyt5 = "powyzej 10"

print(pyt5)

print("6. Ile książek czytasz średnio w ciągu roku?  "
      "\n a. codziennie"
      "\n b. raz w tygodniu"
      "\n c. raz w miesiącu"
      "\n d. raz na kilka miesięcy"
      "\n e. raz na pół roku"
      "\n f. raz na rok"
      "\n g. wcale")

pyt6 = input("Podaj odpowiedz: ")

if pyt6 == "a":
    pyt6 = "codziennie"
elif pyt6 == "b":
    pyt6 = "raz w tygodniu"
elif pyt6 == "c":
    pyt6 = "raz w miesiącu"
elif pyt6 == "d":
    pyt6 = "raz na kilka miesięcy"
elif pyt6 == "e":
    pyt6 = "raz na pół roku"
elif pyt6 == "f":
    pyt6 = "raz na rok"
elif pyt6 == "g":
    pyt6 = "wcale"

print(pyt6)

print("7. Po jakie gatunki książek sięgasz najczęściej?  "
      "\n a. kryminały/thrillery"
      "\n b. horrory"
      "\n c. fantastykę"
      "\n d. science fiction"
      "\n e. przygodowe"
      "\n f. romanse"
      "\n g. naukowe"
      "\n h. biogrficzne"
      "\n i. podróżnicze"
      "\n j. poezję"
      "\n k. psychologiczne"
      "\n l. dla dzieci i młodzieży"
      "\n m. historyczne"
      "\n n. hobbystyczne (gotowanie, wędkarstwo itp.)"
      "\n o. inne, jakie?")

pyt7 = input("Podaj odpowiedz: ")
if pyt7 == "o":
    pyt7 = input("Wpisz jakie: ")
elif pyt7 == "a":
    pyt7 = "kryminały/thrillery"
elif pyt7 == "b":
    pyt7 = "horrory"
elif pyt7 == "c":
    pyt7 = "fantastykę"
elif pyt7 == "d":
    pyt7 = "science fiction"
elif pyt7 == "e":
    pyt7 = "przygodowe"
elif pyt7 == "f":
    pyt7 = "romanse"
elif pyt7 == "g":
    pyt7 = "naukowe"
elif pyt7 == "h":
    pyt7 = "biograficzne"
elif pyt7 == "i":
    pyt7 = "podróżnicze"
elif pyt7 == "j":
    pyt7 = "poezję"
elif pyt7 == "k":
    pyt7 = "psychologiczne"
elif pyt7 == "l":
    pyt7 = "dla dzieci i młodzieży"
elif pyt7 == "m":
    pyt7 = "historyczne"
elif pyt7 == "n":
    pyt7 = "hobbystyczne (gotowanie, wędkarstwo itp.)"

print(pyt7)

print("Odpowiedzi " + pyt0)

print("1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("Odpowiedź: " + pyt1)

print("2. W jakich okolicznościach czytasz książki najczęściej? ")
print("Odpowiedź: " + pyt2)

print("3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("Odpowiedź: " + pyt3)

print("4. Po książki w jakiej formie sięgasz najczęściej?")
print("Odpowiedź: " + pyt4)

print("5. Ile książek czytasz średnio w ciągu roku?")
print("Odpowiedź: " + pyt5)

print("6. Jak często średnio czytasz książki?")
print("Odpowiedź: " + pyt6)

print("7. Po jakie gatunki książek sięgasz najczęściej? ")
print("Odpowiedź: " + pyt7)







