import random

tentativi = 5 #Modifica il numero per scegliere i tentativi
casuale = random.randint(1 , 100)
print(casuale) #Commenta questa stringa se vuoi giocare!

while tentativi > -1: #Condizione tentativi

    n = int(input("Numero? "))

    if n < casuale: #Controlla se è minore
        print("Troppo basso!")
        tentativi = tentativi - 1
    
    if n == casuale: #Condizione se è uguale
        tentativi = -2
    
    if n > casuale: #Controlla se è troppo alto
        print("Troppo alto!")
        tentativi = tentativi - 1
    

    if tentativi > 1: #Controllo tentativi
       print("Attenzione! ti rimangono" , tentativi , "tentativi!")
    
    if tentativi == 1: #Controllo tentativi
       print("Attenzione! ti rimane" , tentativi , "tentativo!")
    
    elif tentativi == 0: #Controllo tentativi
       print("Attenzione! ti rimane l'ultimo tentativo!")
        

if tentativi == -1: #GameOver
    print("Hai perso!")

if tentativi == -2: #Vittoria
    print("Complimenti hai indovinato!")