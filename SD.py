import json

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os


from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap


def json_parse_pinning(nome):
    file_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(file_path)
    file_path = os.path.join(directory_path, nome)
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
                "parallelism": grafico.get("parallelism"),
                "batch": grafico.get("batch"),
                "ff_queue_length": grafico.get("ff_queue_length"),
                "titolo": grafico.get("titolo"),
                "numanode": grafico.get("numanode"),
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

def json_parse_profiling(nome):
    file_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(file_path)
    file_path = os.path.join(directory_path, nome)
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

def calcola_etichette_assey_app(max_value, step=1000000):
    if max_value <= 0:
        raise ValueError("Il valore massimo deve essere maggiore di 0")

    # Determina il passo (step) dinamicamente in base a max_value
    if max_value > 20_000_000:
        step = 5_000_000
    elif max_value > 10_000_000:
        step = 2_000_000

    # Crea la lista dei valori dei tick sull'asse Y
    yticks_values = [i * step for i in range(0, max_value // step + 1)]

    # Crea le etichette formattate per i tick sull'asse Y
    yticks_labels = [f'{i * step:,.0f}'.replace(",", ".") + " t/s" for i in range(0, max_value // step + 1)]

    return yticks_values, yticks_labels

def crea_istogramma_app(applicatione, parallelism, batch, ff_queue_length, titolo, numanode, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = list(dati.keys())
    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    #plt.legend(etichette_asse_x)
    dati_asse_x = list(dati.values())
    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    save_dir = '/home/lorenzo/Scrivania/Grafici_Tesi/Pinning'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicatione,parallelism,"batch="+str(batch), "ff_queue_length="+str(ff_queue_length))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(max_y)

    # Creazione dell'istogramma
    if parallelism == "1,1,1,1":
        plt.figure(figsize=(5, 4))
    if parallelism == "2,2,2,2":
        plt.figure(figsize=(8, 4))
    if parallelism == "8,8,8,8":
        plt.figure(figsize=(10, 4))

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
    #cmap=matplotlib.colormaps['Blues']
    #colors = cmap(np.linspace(1.0, 0.4, len(dati_asse_x)))  # Evita estremi per miglior visibilità
    colore_default = '#C41E3A'  # Rosso cardinale/porpora
    colore_pin = '#1B4F72'  # Blu scuro
    colors = [colore_default] + [colore_pin] * (len(dati_asse_x) - 1)
    bars = plt.bar(range(len(etichette_asse_x)), dati_asse_x, color=colors, alpha=1, width=0.6, zorder=2)  # barre in primo piano

    '''# Aggiungi linee tratteggiate dalla parte superiore delle barre fino all'asse y
    for i, bar in enumerate(bars):
        # Ottieni l'altezza della barra
        height = bar.get_height()
        # Disegna la linea tratteggiata verticale che parte dalla parte superiore della barra fino all'asse y
        plt.hlines(height, -0.5,bar.get_x(), colors='lightgray', linestyles='--', linewidth=0.8)'''

    # Impostiamo il formato dei numeri sull'asse y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels)

    # Impostiamo le etichette per l'asse X (le categorie)
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x)
    # Aggiungiamo il titolo
    plt.title(titolo, fontsize=16)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, "--p="+parallelism+"_"+"--b="+str(batch)+'.png')
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()


def crea_istogramma_ccx(applicatione, numero_coppia, numero_test, CCX, titolo, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = dati.keys()
    #plt.legend(etichette_asse_x)
    dati_asse_x = dati.values()
    save_dir = '/home/lorenzo/Scrivania/Grafici_Tesi/Profiling'

    # calcola il path completo
    complete_path = os.path.join(save_dir, applicatione, "coppia_test_" + str(numero_coppia), str(numero_test))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey(max_y)

    # Creazione dell'istogramma
    plt.figure(figsize=(5, 4))

    # Impostiamo i limiti dell'asse X in modo che parta da 0 e arrivi al massimo valore dei dati
    plt.xlim(-0.5,
             len(etichette_asse_x) - 0.5)

    # Disegnare le linee orizzontali per ogni valore di yticks_values
    for ytick in yticks_values:
        plt.hlines(ytick, -0.5, len(etichette_asse_x) - 0.5, colors='gray', linestyles='--', linewidth=0.6,
                   zorder=1)  # Linea tratteggiata, zorder basso per metterle sotto le barre
    # Aggiungere linee a metà tra ogni intervallo
    for i in range(1, len(yticks_values)):
        halfway = (yticks_values[i] + yticks_values[i - 1]) / 2  # Calcolare il punto centrale tra i tick
        plt.hlines(halfway, -0.5, len(etichette_asse_x) - 0.5, colors='lightgray', linestyles='--',
                   linewidth=0.8)  # Linea leggera tra i tick

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
    save_path = os.path.join(complete_path, 'istogramma_' + CCX + '.png')
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def main():
    #grafici = json_parse_profiling('istogrammi_profiling.json')
    #prova = grafici[0]
    #crea_istogramma_ccx(prova["applicazione"], prova["coppia_test"], prova["test"], prova["CCX"],
    #                    prova["titolo"], prova["dati"], prova["max"])
    grafici = json_parse_pinning('istogrammi_pinning_SD.json')
    for grafico in grafici:
        #if grafico["applicazione"] == "SD" and grafico["parallelism"] == "2,2,2,2" and grafico["ff_queue_length"] != 16:
         crea_istogramma_app(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"], grafico["max"] )

# Questa parte è importante: assicura che la funzione main() venga eseguita solo
# quando il file viene eseguito come script, non quando viene importato come modulo
if __name__ == "__main__":
    main()
