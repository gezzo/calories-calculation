sesso = input("Inserisci il Sesso (M/F): ").strip().upper()

while sesso not in ("M", "F"):
    print("Input non valido. Inserisci solo 'M' o 'F'.")
    sesso = input("Inserisci il Sesso (M/F): ").strip().upper()

altezza = input("Inserisci l'altezza in cm:")
peso = input("Inserisci il Peso: ")
passi = input ("numero di passi giornaliero medio: ")
eta = input("Inserisci l'eta': ")
KmPercorsi = input("Km percorsi: ")
Dislivello = input("Dislivello: ")

'''
Calcolo Fabbisogno calorico: MBR(Metabolismo Basale) + NEAT(quello che viene dall'attivita') + Allenamento
NEAT = 0.6 * MBR (ho fatto una media dei passi fatti a settimana)
Allenamento = peso corporeo * km fatti + dislivello
'''

'''
MBR Calcolato con la Formula di Harris Benedict
Uomo MBR = 66,4730 + (13,7516 x peso in kg) + (5,0033 x statura in cm) – (6,7550 x età in anni)
Donna MBR = 655,0955 + (9,5634 x peso in kg) + (1,8496 x statura in cm) – (4,6756 x età in anni)
'''
if sesso == 'M':
    MBR = (66,4730 + (13.7516*int(peso)) + (5.0033*int(altezza))) - (6.7550 *int(eta))

else:
    MBR = (655.0955 + (9.5634*int(peso)) + (1.8496*int(altezza))) - (4.6756 *int(eta))

'''
NEAT 
Il NEAT si calcola a partire dal MBR e si moltiplica per il numero sotto dato dal numero di passi.
Uomini
0 - 4000 --> 0.2
4000 - 8000 --> 0.4
8000 - 12000 --> 0.6
> 12000 --> 0.8

Donne 
0 - 4000 --> 0.1
4000 - 8000 --> 0.3
8000 - 12000 --> 0.5
> 12000 --> 0.7
'''

NEAT = MBR * 0.6

if Dislivello == 0:
    ALLENAMENTO = int(peso) * float(KmPercorsi)
else:
    ALLENAMENTO = int(peso) * (float(KmPercorsi) + int(Dislivello)/100)
FabbisognoCaloricoGiornaliero = MBR + NEAT + ALLENAMENTO


# 2.0g di proteine per peso coporeo
GrammiProteine = 2 * int(peso)
# tra 0.8 e 1.2g per peso coporeo, quindi faccio una media
GrammiGrassi = (0.8 * int(peso) + 1.2 * int(peso))/2

KCalorieProteine = 4 * GrammiProteine
KCalorieGrassi = 8 * GrammiGrassi
FabbisognoCaloricoCarboidrati = FabbisognoCaloricoGiornaliero - KCalorieGrassi - KCalorieProteine
GrammiCarboidrati = FabbisognoCaloricoCarboidrati/4

print("Fabbisogno calorico giornaliero: {} KCal".format(int(FabbisognoCaloricoGiornaliero)))
print("Fabbisogno calorico da allenamento: {} KCal".format(int(ALLENAMENTO)))
print("Target proteine: {} grammi".format(int(GrammiProteine)))
print("Target grassi: {} grammi".format(int(GrammiGrassi)))
print("Target carboidrati: {} grammi".format(int(GrammiCarboidrati)))
