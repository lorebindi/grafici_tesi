import json

import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib import ticker

def json_parse():
    file_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(file_path)
    file_path = os.path.join(directory_path, 'istogrammi.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Carica il file JSON

        grafici = data.get("grafici", [])  # Estrai la lista di grafici
        if not grafici:
            raise ValueError("Il file JSON non contiene grafici nella sezione 'grafici'.")

        parsed_data = []
        for grafico in grafici:
            # Costruisci un dizionario con le informazioni di ogni grafico
            parsed_data.append({
                "applicazione": grafico.get("applicazione"),
                "coppia_test": grafico.get("coppia_test"),
                "test": grafico.get("test"),
                "CCX": grafico.get("CCX"),
                "titolo": grafico.get("titolo"),
                "dati": grafico.get("dati"),
                "max": grafico.get("max")
            })

        return parsed_data

    except FileNotFoundError:
        print(f"Errore: Il file {file_path} non è stato trovato.")
        return []
    except json.JSONDecodeError:
        print(f"Errore: Il file {file_path} non è un JSON valido.")
        return []
    except Exception as e:
        print(f"Errore sconosciuto: {e}")
        return []

def calcola_etichette_assey(max_value, step=1000000000):

    if max_value <= 0:
        raise ValueError("Il valore massimo deve essere maggiore di 0")

    # Crea la lista dei valori dei tick sull'asse Y
    yticks_values = [i * step for i in range(0, max_value // step + 1)]

    # Crea le etichette formattate per i tick sull'asse Y
    yticks_labels = [f'{i * step:,}' for i in range(0, max_value // step + 1)]

    return yticks_values, yticks_labels

def crea_istogramma_ccx(applicatione, numero_coppia, numero_test, CCX, titolo, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = dati.keys()
    plt.legend(etichette_asse_x)
    dati_asse_x = dati.values()
    save_dir = '/home/lorenzo/Scrivania/Grafici_Tesi'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicatione,"coppia_test_"+str(numero_coppia),str(numero_test))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey(max_y)

    # Creazione dell'istogramma
    plt.figure(figsize=(5, 4))

    # Impostiamo i limiti dell'asse X in modo che parta da 0 e arrivi al massimo valore dei dati
    plt.xlim(-0.5,
             len(etichette_asse_x) - 0.5)  # L'asse X avrà solo 2 etichette, quindi va da -0.5 a 1.5 per centrare le barre

    # Disegnare le linee orizzontali per ogni valore di yticks_values
    for ytick in yticks_values:
        plt.hlines(ytick, -0.5, len(etichette_asse_x) - 0.5, colors='gray', linestyles='--', linewidth=0.6,
                   zorder=1)  # Linea tratteggiata, zorder basso per metterle sotto le barre
    # Aggiungere linee a metà tra ogni intervallo
    for i in range(1, len(yticks_values)):
        halfway = (yticks_values[i] + yticks_values[i - 1]) / 2  # Calcolare il punto centrale tra i tick
        plt.hlines(halfway, -0.5, len(etichette_asse_x)-0.5, colors='lightgray', linestyles='--', linewidth=0.8)  # Linea leggera tra i tick

    # Creazione delle barre dell'istogramma (due colonne affiancate)
    bars = plt.bar(range(len(etichette_asse_x)), dati_asse_x, color=['#4a86e8', '#ea4335'], alpha=1, width=0.7,
                   zorder=2)  # barre in primo piano

    '''# Aggiungi linee tratteggiate dalla parte superiore delle barre fino all'asse y
    for i, bar in enumerate(bars):
        # Ottieni l'altezza della barra
        height = bar.get_height()
        # Disegna la linea tratteggiata verticale che parte dalla parte superiore della barra fino all'asse y
        plt.hlines(height, -0.5,bar.get_x(), colors='lightgray', linestyles='--', linewidth=0.8) '''

    # Impostiamo il formato dei numeri sull'asse y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels)

    # Impostiamo le etichette per l'asse X (le categorie)
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x)
    # Aggiungiamo il titolo
    plt.title(titolo, fontsize=16)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, 'istogramma_'+CCX+'.png')
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def main():
    grafici = json_parse()
    prova = grafici[0]
    #crea_istogramma_ccx(prova["applicazione"], prova["coppia_test"], prova["test"], prova["CCX"],
    #                    prova["titolo"], prova["dati"], prova["max"])
    for grafico in grafici:
         crea_istogramma_ccx(grafico["applicazione"], grafico["coppia_test"], grafico["test"], grafico["CCX"], grafico["titolo"], grafico["dati"], grafico["max"] )

# Questa parte è importante: assicura che la funzione main() venga eseguita solo
# quando il file viene eseguito come script, non quando viene importato come modulo
if __name__ == "__main__":
    main()
