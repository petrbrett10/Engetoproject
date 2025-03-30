jmeno = input ("Zadej jméno:")
print (jmeno)
print ("Vítej v systému, ", jmeno)
vstupni_cislo = float(input ("Zadej jakékoliv destiné číslo:"))
zaokrouhleni = int(input ("Na kolik míst ho chceš zaokrouhlit? Zadej číslo:"))
vystup = round(vstupni_cislo,zaokrouhleni)
absolutni_hodnota_vystupu = abs(vystup)
print (vystup)
print ("Absolutni hodnota vystupu je: ", absolutni_hodnota_vystupu)
textova_hodnota_vystupu = str(absolutni_hodnota_vystupu)
print (3*textova_hodnota_vystupu)
#print (min (textova_hodnota_vystupu))
print ("Výsledny retezec má ",len(textova_hodnota_vystupu), "znaků.")
print ("A jsou to tyto znaky:",  list(textova_hodnota_vystupu))
print ("První 3 znaky jsou:", textova_hodnota_vystupu[:3])

# Ulož jméno Lukáš
jmeno = "Lukáš"

# Ulož příjmení Dvořák
prijmeni = "Dvořák"

# Vytvoř proměnnou "cele_jmeno" obsahující mezeru
cele_jmeno = jmeno + " " + prijmeni

# Vytvoř a vypiš hodnotu délky uložené proměnné "cele_jmeno"
delka_jmena = len(cele_jmeno)
print("Délka jmena:", delka_jmena)

# Vypiš celé jméno ohraničené oddělovači
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)