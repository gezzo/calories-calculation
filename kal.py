def leggi_float(enter: str) -> float:
    while True:
        try:
            return float(input(enter))
        except ValueError:
            print("Errore: inserisci un numero valido. Usa il punto per i decimali")

def leggi_intero(enter: str) -> float:
    while True:
        try:
            return int(input(enter))
        except ValueError:
            print("Errore: inserisci un numero intero valido.")


def leggi_sesso(enter: str) -> str:
    while True:
        sesso = input(enter).strip().upper()
        if sesso in ("M", "F"):
            return sesso
        else:
             print("Input non valido. Inserisci solo 'M' o 'F'.") 


sesso = leggi_sesso("Inserisci il Sesso (M/F): ")
altezza = leggi_intero("Inserisci l'altezza in cm:")
peso = leggi_float("Inserisci il Peso: ")
passi = leggi_intero ("numero di passi giornaliero medio: ")
eta = leggi_intero("Inserisci l'eta': ")
KmPercorsi = leggi_float("Km percorsi: ")
dislivello = leggi_intero("Dislivello: ")

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
def calcolo_MBR(sesso: str, peso: float, altezza: int, eta: int) -> float:
    if sesso == 'M':
        MBR = 66.4730 + (13.7516*peso) + (5.0033*altezza) - (6.7550 * eta)

    else:
        MBR = 655.0955 + (9.5634*peso) + (1.8496*altezza) - (4.6756 *eta)
    return MBR

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

def calcolo_coefficiente_NEAT(sesso: str, passi: int) -> float:
    if sesso == "M":
        if passi < 4000:
            return 0.2
        elif passi < 8000:
            return 0.4
        elif passi < 12000:
            return 0.6
        else:
            return 0.8
    elif sesso == "F":
        if passi < 4000:
            return 0.1
        elif passi < 8000:
            return 0.3
        elif passi < 12000:
            return 0.5
        else:
            return 0.7


MBR = calcolo_MBR(sesso, peso, altezza, eta)
Coefficiente_NEAT = calcolo_coefficiente_NEAT(sesso, passi)
NEAT = MBR * Coefficiente_NEAT

if dislivello == 0:
    ALLENAMENTO = peso * KmPercorsi
else:
    ALLENAMENTO = peso * (KmPercorsi + dislivello/100)
FabbisognoCaloricoGiornaliero = MBR + NEAT + ALLENAMENTO


# 2.0g di proteine per peso coporeo
GrammiProteine = 2 * peso
# tra 0.8 e 1.2g per peso coporeo, quindi faccio una media
GrammiGrassi = (0.8 * peso + 1.2 * peso)/2

KCalorieProteine = 4 * GrammiProteine
KCalorieGrassi = 8 * GrammiGrassi
FabbisognoCaloricoCarboidrati = FabbisognoCaloricoGiornaliero - KCalorieGrassi - KCalorieProteine
GrammiCarboidrati = FabbisognoCaloricoCarboidrati/4

print("\n==================== MBR, NEAT ====================")
print("MBR: {} Kcal".format(int(MBR)))
print("NEAT: {} Kcal".format(int(NEAT)))
print ("===================================================")
print("")
print("========== Fabbisogno giornaliero e allenamento =========")
print("Fabbisogno calorico giornaliero: {} KCal".format(int(FabbisognoCaloricoGiornaliero)))
print("Fabbisogno calorico da allenamento: {} KCal".format(int(ALLENAMENTO)))
print ("======================================================")
print("")
print("================= Macronutrienti ==================")
print("Target proteine: {} grammi".format(int(GrammiProteine)))
print("Target grassi: {} grammi".format(int(GrammiGrassi)))
print("Target carboidrati: {} grammi".format(int(GrammiCarboidrati)))
print("====================================================")
