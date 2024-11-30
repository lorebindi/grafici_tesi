import json

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os


from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D


def json_parse_ffvsOS(nome):
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
                "max_batch": grafico.get("max_batch"),
                "titolo": grafico.get("titolo"),
                "dati_ff": grafico.get("dati_ff"),
                "dati_OS": grafico.get("dati_OS"),
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

def calcola_etichette_assey_profiling(max_value, step=1000000000):

    if max_value <= 0:
        raise ValueError("Il valore massimo deve essere maggiore di 0")

    # Crea la lista dei valori dei tick sull'asse Y
    yticks_values = [i * step for i in range(0, max_value // step + 1)]

    # Crea le etichette formattate per i tick sull'asse Y
    yticks_labels = [f'{i * step:,}' for i in range(0, max_value // step + 1)]

    return yticks_values, yticks_labels

def calcola_etichette_assey_app(app, max_value, step=1000000):
    yticks_values = []
    yticks_labels = []

    if max_value <= 0:
        raise ValueError("Il valore massimo deve essere maggiore di 0")

    # Determina il passo (step) dinamicamente in base a max_value
    match app:
        case "SD":
            # Cambia step a seconda del max_value
            if max_value > 30_000_000:
                step = 10_000_000
            elif max_value > 20_000_000:
                step = 5_000_000
            elif max_value > 10_000_000:
                step = 2_000_000
            else:
                step = 1_000_000
            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(0, max_value // step + 1)]

            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{i * step:,.0f}'.replace(",", ".") + " t/s" for i in range(0, max_value // step + 1)]

        case "WC":
            # Cambia step a seconda del max_value
            if max_value > 100:
                step = 20
            elif max_value > 30:
                step=10
            elif max_value > 20:
                step = 5
            elif max_value > 10:
                step = 2
            else:
                step=1
            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(0, max_value // step + 1)]
            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{i * step:,.0f}'.replace(",", ".") + " MB/s" for i in range(0, max_value // step + 1)]

        case "FD":
            # Cambia step a seconda del max_value
            if max_value < 1000000:
                step = 100000
            elif max_value == 1000000:
                step = 200000
            elif 1000000 < max_value <= 2000000:
                step = 500000
            elif max_value%1000 == 0:
                step = 1000000
            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(0, max_value // step + 1)]
            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{i * step:,.0f}'.replace(",", ".") + " t/s" for i in range(0, max_value // step + 1)]

        case "TM":
            # Cambia step a seconda del max_value
            if max_value <= 1000:
                step = 100
            elif 1000 < max_value <= 2000:
                step = 500
            elif max_value % 1000 == 0:
                step = 1000
            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(0, max_value // step + 1)]
            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{i * step:,.0f}'.replace(",", ".") + " t/s" for i in range(0, max_value // step + 1)]

    return yticks_values, yticks_labels

def crea_grafo_linee_ffvsOS(applicazione, parallelism, max_batch, titolo, datiff, datiOS, max_y):
    if not datiff or not datiOS:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = [str(2 ** i) for i in range(max_batch) if 2 ** i <= max_batch]
    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie_ff = [val['media'] for val in datiff.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std_ff = [val['dev_std'] for val in datiff.values()]  # Estrae il valore 'dev_std' per ogni elemento
    medie_OS = [val['media'] for val in datiOS.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std_OS = [val['dev_std'] for val in datiOS.values()]  # Estrae il valore 'dev_std' per ogni elemento
    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.008
    save_dir = '/home/lorenzo/Scrivania/Grafici_Tesi/ffvsOS'

    # Creazione del grafico
    plt.figure(figsize=(11, 6))

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y)
    if(yticks_values == [] or yticks_labels == []):
        raise ValueError("yticks vuoti")
    plt.yticks(yticks_values, yticks_labels, fontsize=12)

    # Aggiungere un margine extra al limite dell'asse Y
    plt.ylim(min(yticks_values), max(yticks_values))

    # Impostiamo i limiti dell'asse X in modo che parta da 0 e arrivi al massimo valore dei dati
    plt.xlim(-0.5,
             len(etichette_asse_x) - 0.5)  # L'asse X avrà solo 2 etichette, quindi va da -0.5 a 1.5 per centrare le barre

    #Disegnare le linee orizzontali per ogni valore di yticks_values
    for ytick in yticks_values:
        plt.hlines(ytick, -0.5, len(etichette_asse_x) - 0.5, colors='gray', linestyles='--', linewidth=0.6,
                   zorder=1)  # Linea tratteggiata, zorder basso per metterle sotto le barre
    # Aggiungere linee a metà tra ogni intervallo
    for i in range(1, len(yticks_values)):
        halfway = (yticks_values[i] + yticks_values[i - 1]) / 2  # Calcolare il punto centrale tra i tick
        plt.hlines(halfway, -0.5, len(etichette_asse_x) - 0.5, colors='lightgray', linestyles='--',
                   linewidth=0.8)  # Linea leggera tra i tick

    # Linea per datiff (FastFlow) con barre di errore
    plt.errorbar(
        etichette_asse_x, medie_ff, yerr=dev_std_ff,
        label=r'$\sigma$ prestazioni FastFlow pinning ', marker='s', color='#1B4F72',
        linestyle='-', linewidth=2, elinewidth=1.5, capsize=0
    )

    # Linea per datiOS con barre di errore
    plt.errorbar(
        etichette_asse_x, medie_OS, yerr=dev_std_OS,
        label=r'$\sigma$ prestazioni OS scheduler ', marker='s', color='#C41E3A',
        linestyle='-', linewidth=2, elinewidth=1, capsize=0
    )

    # Linea per datiff (FastFlow)
    plt.plot(etichette_asse_x, medie_ff, label=r'$\mu$ prestazioni FastFlow pinning', marker='s', color='#1B4F72', linestyle='-', linewidth=2)

    # Linea per datiOS
    plt.plot(etichette_asse_x, medie_OS, label=r'$\mu$ prestazioni OS scheduler', marker='s', color='#C41E3A', linestyle='-', linewidth=2)


    # Titoli e etichette
    plt.title(titolo, fontsize=16)
    plt.xlabel('Batch Size', fontsize=14)
    plt.ylabel('Prestazioni', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Legenda
    plt.legend(fontsize=12, loc='upper left')

    # Griglia
    #plt.grid(visible=True, linestyle='--', alpha=0.6)

    # Salvataggio del grafico
    save_path = os.path.join(save_dir, f"{applicazione+"_"+parallelism}.png")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_istogramma_app(applicazione, parallelism, batch, ff_queue_length, titolo, numanode, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = list(dati.keys())
    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie = [val['media'] for val in dati.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std = [val['dev_std'] for val in dati.values()]  # Estrae il valore 'dev_std' per ogni elemento
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.008

    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    save_dir = '/home/lorenzo/Scrivania/Grafici_Tesi/Pinning'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicazione,parallelism,"batch="+str(batch), "ff_queue_length="+str(ff_queue_length))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste


    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y)
    if(yticks_values == [] or yticks_labels == []):
        raise ValueError("yticks vuoti")

    # Creazione dell'istogramma
    if parallelism == "1,1,1,1":
        plt.figure(figsize=(7, 5))
    if parallelism == "2,2,2,2":
        plt.figure(figsize=(8, 5))
    if parallelism == "4,4,4,4":
        plt.figure(figsize=(11, 5))
    if parallelism == "8,8,8,8":
        plt.figure(figsize=(10, 5))

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
    colore_pin = '#1B4F72'  # Blu scuro. Prima: #2A6189
    colors = [colore_default] + [colore_pin] * (len(medie) - 1)

    # Aggiunta barre
    bars = plt.bar(
        range(len(etichette_asse_x)),
        medie,
        color=colors,
        alpha=1,
        width=0.6,
        zorder=2
    )

    # Lista per gli handle e le etichette della legenda
    handles = []
    labels = []

    # Aggiungi sempre la linea rossa (media FF) e la linea blu (media custom)
    bars_handle_1 = Line2D([0], [0], color=colore_default, lw=6, label=r'$\mu$ prestazioni FF')
    bars_handle_2 = Line2D([0], [0], color=colore_pin, lw=6, label=r'$\mu$ prestazioni strategie custom')
    handles.append(bars_handle_1)
    handles.append(bars_handle_2)
    labels.append(r'$\mu$ prestazioni FastFlow')
    labels.append(r'$\mu$ prestazioni strategie custom')

    # Flag per la presenza di simboli o errori
    has_err_bars = False
    has_deviation_symbol = False


    # Aggiunta delle barre di errore o simboli
    for i, (media, errore) in enumerate(zip(medie, dev_std)):
        rapporto_errore = errore / media if media != 0 else np.inf

        if rapporto_errore >= rapporto_soglia:
            # Barre di errore normali
            plt.errorbar(
                i,
                media,
                yerr=errore,
                fmt='none',
                ecolor='black',
                capsize=2,
                elinewidth=0.8,
                capthick=1.0,
                zorder=3,
                linestyle='--'
            )
            has_err_bars = True
        else:
            # Simbolo per deviazioni trascurabili
            plt.plot(
                i,
                media + 0.02 * media,  # Simbolo leggermente sopra la barra
                marker='o',
                color='black',
                markersize=5,
                label=r'$\sigma$' + ' prestazioni trascurabile' if not has_deviation_symbol else ''
            )
            has_deviation_symbol = True

    # Se ci sono barre di errore, aggiungi la linea nera nella legenda
    if has_err_bars:
        error_handle = Line2D([0], [0], color='black', lw=1, label='Deviazione standard')
        handles.append(error_handle)
        labels.append(r'$\sigma$ prestazioni')

    # Se ci sono simboli di deviazione trascurabile, aggiungi il punto nella legenda
    if has_deviation_symbol:
        symbol_handle = Line2D([0], [0], marker='o', color='black', lw=0, markersize=5,
                               label=r'$\sigma$ prestazioni trascurabile')
        handles.append(symbol_handle)
        labels.append(r'$\sigma$ prestazioni trascurabile')

    plt.legend(handles=handles, labels=labels, loc='upper left', fontsize=10)

    # Impostiamo il formato dei numeri sull'asse Y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels)

    # Impostiamo le etichette per l'asse X
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x)
    plt.title(titolo, fontsize=15)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, "--p=" + parallelism + "_" + "--b=" + str(batch) + '.png')
    plt.tight_layout()


    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_istogramma_ccx(applicazione, numero_coppia, numero_test, CCX, titolo, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = dati.keys()
    #plt.legend(etichette_asse_x)
    dati_asse_x = dati.values()
    save_dir = '/home/lorenzo/Scrivania/Grafici_Tesi/Profiling'

    # calcola il path completo
    complete_path = os.path.join(save_dir, applicazione, "coppia_test_" + str(numero_coppia), str(numero_test))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_profiling(max_y)

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

def crea_istogrammi_profiling():
    grafici = json_parse_profiling('istogrammi_profiling.json')
    prova = grafici[0]
    crea_istogramma_ccx(prova["applicazione"], prova["coppia_test"], prova["test"], prova["CCX"], prova["titolo"], prova["dati"], prova["max"])

def crea_grafi_linee_ffvsOS():
    grafici = json_parse_ffvsOS('ffvsOS.json')
    for grafico in grafici:
        crea_grafo_linee_ffvsOS(grafico["applicazione"], grafico["parallelism"], grafico["max_batch"], grafico["titolo"],
                            grafico["dati_ff"], grafico["dati_OS"], grafico["max"])


def crea_istogrammi_pinning_SD():
    grafici = json_parse_pinning('istogrammi_pinning_SD.json')
    for grafico in grafici:
        if grafico["applicazione"] == "SD":
            crea_istogramma_app(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"], grafico["max"])

def crea_istogrammi_pinning_WC():
    grafici = json_parse_pinning('istogrammi_pinning_WC.json')
    for grafico in grafici:
        if grafico["applicazione"] == "WC":
            crea_istogramma_app(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"], grafico["max"])

def crea_istogrammi_pinning_FD():
    grafici = json_parse_pinning('istogrammi_pinning_FD.json')
    for grafico in grafici:
        if grafico["applicazione"] == "FD":
            crea_istogramma_app(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"], grafico["max"])

def crea_istogrammi_pinning_TM():
    grafici = json_parse_pinning('istogrammi_pinning_TM.json')
    for grafico in grafici:
        if grafico["applicazione"] == "TM":
            crea_istogramma_app(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"], grafico["max"])

def main():

    #crea_istogrammi_pinning_SD()
    #crea_istogrammi_pinning_WC()
    #crea_istogrammi_pinning_FD()
    #crea_istogrammi_pinning_TM()
    crea_grafi_linee_ffvsOS()

# Questa parte è importante: assicura che la funzione main() venga eseguita solo
# quando il file viene eseguito come script, non quando viene importato come modulo
if __name__ == "__main__":
    main()
