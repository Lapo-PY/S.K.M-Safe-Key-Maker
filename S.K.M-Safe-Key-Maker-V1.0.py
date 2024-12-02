# Importiamo il modulo random per generare numeri e indici casuali
import random

# Definizione dei caratteri utilizzati per generare la password
lettere = "abcdefghilmnopqrstuywxvz"  # Lettere alfabetiche
numeri = "0123456789"                # Numeri
caratteri_spec = "!@#$%^&*()_+-=[]|;:,.<>?/`~"  # Caratteri speciali

# Codici ANSI per i colori e lo stile del testo
RED = "\033[91m"       # Colore rosso
GREEN = "\033[92m"     # Colore verde
YELLOW = "\033[93m"    # Colore giallo
RESET = "\033[0m"      # Resetta lo stile
GRASSETT0 = "\033[1m"  # Stile grassetto

# Variabili contatori (anche se non necessarie, sono mantenute per compatibilità)
count = 0
count2 = 0
count3 = 0

# Messaggi introduttivi per l'utente
print(f"{GREEN}{GRASSETT0}PASSWORD GENERATOR{RESET}{YELLOW} V-1.0{RESET}")
print(f"Il programma si interrompe quando si inserisce {GRASSETT0}{RED}STOP{RESET}\n")

# Ciclo principale per generare più password
while True:
    password = ""  # Variabile che conterrà la password generata
    a = True  # Flag per abilitare l'uso dei numeri
    b = True  # Flag per abilitare l'uso dei caratteri speciali
    stampa = True  # Flag per controllare se stampare la password

    # Richiesta del livello di sicurezza
    sicurezza = input(f"Inserire il livello di sicurezza di cui vuoi avere la password ({RED}basso{RESET},{YELLOW} medio{RESET}, {GREEN}alto{RESET}):\n").lower()

    # Verifica se l'utente vuole uscire
    if sicurezza == "stop":
        stampa = False  # Disattiva la stampa
        print(f"{RED}FINITO{RESET}")  # Messaggio di fine programma
        break

    # Controllo per input non valido
    elif sicurezza not in ["basso", "medio", "alto"]:
        print(f"{RED}{GRASSETT0}ERRORE DURANTE L'INSERIMENTO DEL LIVELLO{RESET}")
        continue

    # Configurazione delle impostazioni in base al livello di sicurezza
    else:
        if sicurezza == "basso":
            colore = RED  # Colore rosso per basso
            lunghezza_consigliata = "6/8"  # Lunghezza consigliata
            a = False  # Disabilita i numeri
            b = False  # Disabilita i caratteri speciali

        elif sicurezza == "medio":
            colore = YELLOW  # Colore giallo per medio
            lunghezza_consigliata = "8/12"  # Lunghezza consigliata
            a = True  # Abilita i numeri
            b = False  # Disabilita i caratteri speciali

        else:  # Livello "alto"
            colore = GREEN  # Colore verde per alto
            lunghezza_consigliata = "12/16+"  # Lunghezza consigliata
            a = True  # Abilita i numeri
            b = True  # Abilita i caratteri speciali

        # Richiesta della lunghezza della password
        lunghezza = int(input(f"{colore}Inserire la lunghezza della password{RESET}\n{GRASSETT0}{RED}lunghezza consigliata {lunghezza_consigliata} {RESET}:\n"))

        # Controllo su input non valido (non necessario, ma incluso per sicurezza)
        if type(lunghezza) == "<class 'str'>":
            print(f"{RED}{GRASSETT0}HAI INSERITO UNA VARIABILE NON VALIDA{RESET}")
            continue

        # Controllo che la lunghezza sia valida
        elif lunghezza <= 0:
            print(f"{RED}{GRASSETT0}LUNGHEZZA INVALIDA{RESET}")
            continue

        # Generazione della password
        else:
            for i in range(0, lunghezza, 1):
                # Scelta casuale del tipo di carattere
                num = random.randrange(0, 4)
                # Scelta casuale di un carattere dal rispettivo set
                count = random.randrange(0, len(lettere))
                count2 = random.randrange(0, len(numeri))
                count3 = random.randrange(0, len(caratteri_spec))

                # Aggiunge un carattere speciale se consentito
                if num == 0 and b:
                    password += caratteri_spec[count3]

                # Aggiunge una lettera minuscola
                elif num == 1:
                    password += lettere[count].lower()

                # Aggiunge un numero se consentito
                elif num == 2 and a:
                    password += numeri[count2]

                # Aggiunge una lettera maiuscola
                else:
                    password += lettere[count].upper()

    # Stampa la password generata se il flag 'stampa' è attivo
    if stampa:
        print(f"{YELLOW}La password è{RESET}: {password}")
        print(f"Il programma si interrompe quando si inserisce {RED}STOP{RESET}\n")
    else:
        print()
