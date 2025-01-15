import json
import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib import ticker
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def json_parse_scelta_numanode(nome):
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
                "strategy": grafico.get("strategy"),
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

def json_parse_WinKey(nome):
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
                "titolo": grafico.get("titolo"),
                "dati": grafico.get("dati"),
                "max": grafico.get("max"),
                "min": grafico.get("min")
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
                "parallelismo": grafico.get("parallelismo"),
                "batch": grafico.get("batch"),
                "coppia_test": grafico.get("coppia_test"),
                "strategia": grafico.get("strategia"),
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

def calcola_etichette_assey_profiling(max_value, step=1_000_000_000):
    yticks_values = []
    yticks_labels = []

    if max_value <= 0:
        raise ValueError("Il valore massimo deve essere maggiore di 0")

    if(max_value <= 2_000_000_000):
        step = 500_000_000
    if (max_value > 2_000_000_000):
        step = 1_000_000_000
    if(max_value >= 20_000_000_000):
        step = 2_000_000_000
        if(max_value % 2 != 0):
            max_value += 1_000_000_000
        max_value += step
    if(max_value > 24_000_000_000):
        step = 5_000_000_000
        if (max_value % 2 != 0):
            max_value = (max_value // step + 1) * step
        max_value += step



    yticks_values = [i * step for i in range(max_value // step + 1)]
    yticks_labels = [f'{float(value / 1_000_000_000)}' for value in yticks_values]



    return yticks_values, yticks_labels

def calcola_etichette_assey_app(app, max_value, min_value=0, step=1000000):
    yticks_values = []
    yticks_labels = []

    if max_value <= 0:
        raise ValueError("Il valore massimo deve essere maggiore di 0")

    # Determina il passo (step) dinamicamente in base a max_value
    match app:
        case "SD":
            # Cambia step a seconda del max_value
            if max_value-min_value >= 30_000_000:
                step = 10_000_000
            elif max_value-min_value >= 20_000_000:
                step = 5_000_000
            elif max_value-min_value >= 10_000_000:
                step = 2_000_000
            elif max_value-min_value > 2_000_000:
                step = 1_000_000
            elif max_value-min_value >= 1_500_000:
                step = 500_000
            elif max_value - min_value <= 1_000_000:
                step = 200_000

            # Aggiungi il primo valore (min_value) e continua fino a max_value
            value = min_value
            while value <= max_value:
                yticks_values.append(value)
                value += step  # Aggiungi il passo

            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{value / 1_000_000:.1f}' for value in yticks_values]

        case "WC":
            # Cambia step a seconda del max_value
            if max_value-min_value >= 100:
                step = 20
            elif max_value-min_value >= 30:
                step=10
            elif max_value-min_value >= 20:
                step = 5
            elif max_value-min_value >= 10:
                step = 2
            else:
                step=1
            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(min_value // step, max_value // step + 1)]
            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{i * step:,.0f}'.replace(",", ".") for i in range(min_value // step, max_value // step + 1)]

        case "FD":
            # Cambia step a seconda del max_value
            if max_value-min_value > 2_000_000:
                step = 1_000_000
            elif max_value-min_value > 1_000_000:
                step = 500_000
            elif max_value-min_value <= 1_000_000:
                step = 100_000

            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(min_value // step, max_value // step + 1)]
            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{value / 1_000_000:.1f}' for value in yticks_values]

        case "TM":
            # Cambia step a seconda del max_value
            if max_value <= 1000:
                step = 100
            elif 1000 < max_value <= 2000:
                step = 500
            elif max_value % 1000 == 0:
                step = 1000
            # Crea la lista dei valori dei tick sull'asse Y
            yticks_values = [i * step for i in range(min_value // step, max_value // step + 1)]
            # Crea le etichette formattate per i tick sull'asse Y
            yticks_labels = [f'{value / 1_000:.1f}' for value in yticks_values]

    return yticks_values, yticks_labels

def crea_istogramma_scelta_numanode(applicazione, parallelism, batch, ff_queue_length, titolo, strategy, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = list(dati.keys())
    etichette_asse_x = [etichetta.replace(' ', '\n', 1) for etichetta in etichette_asse_x]
    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie = [val['media'] for val in dati.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std = [val['dev_std'] for val in dati.values()]  # Estrae il valore 'dev_std' per ogni elemento
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.01

    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/Scelta_Numanode'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicazione,parallelism,"batch="+str(batch), "ff_queue_length="+str(ff_queue_length))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste


    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y)
    if(yticks_values == [] or yticks_labels == []):
        raise ValueError("yticks vuoti")

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
    #cmap=matplotlib.colormaps['Blues']
    #colors = cmap(np.linspace(0.9, 0.4, len(medie)))  # Evita estremi per miglior visibilità
    #colore_default = '#C41E3A'  # Rosso cardinale/porpora
    colore_pin = '#1B4F72'  # Blu scuro. Prima: #2A6189
    #colors = '''[colore_default] +''' [colore_pin] '''* (len(medie) - 1)

    # Aggiunta barre
    bars = plt.bar(
        range(len(etichette_asse_x)),
        medie,
        color=colore_pin,
        alpha=1,
        width=0.6,
        zorder=2
    )

    # Lista per gli handle e le etichette della legenda
    handles = []
    labels = []

    # Aggiungi sempre la linea rossa (media FF) e la linea blu (media custom)
    #bars_handle_1 = Line2D([0], [0], color=colore_default, lw=6, label=r'$\mu$ throughput FF')
    #bars_handle_2 = Line2D([0], [0], color=colore_pin, lw=6, label=r'$\mu$ throughput strategie custom')
    #handles.append(bars_handle_1)
    #handles.append(bars_handle_2)
    #labels.append(r'$\mu$ throughput FastFlow')
    #labels.append(r'$\mu$ throughput strategie custom')

    gradient_patch = Patch(color=colore_pin, label="Sfumatura valori", lw=0)
    handles.append(gradient_patch)
    labels.append('Throughput ')

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
    #if has_err_bars:
    #    error_handle = Line2D([0], [0], color='black', lw=1, label='Deviazione standard')
    #    handles.append(error_handle)
    #    labels.append(r'$\sigma$ throughput')

    # Se ci sono simboli di deviazione trascurabile, aggiungi il punto nella legenda
    if has_deviation_symbol:
        symbol_handle = Line2D([0], [0], marker='o', color='black', lw=0, markersize=5,
                               label=r'$\sigma$ prestazioni trascurabile')
        handles.append(symbol_handle)
        labels.append(r'$\sigma$ negligible')

    plt.legend(handles=handles, labels=labels, loc='upper left', fontsize=10)

    # Impostiamo il formato dei numeri sull'asse Y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels, fontsize=12)

    # Impostiamo le etichette per l'asse X
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=11)
    plt.title(titolo+ "\n Strategy: " + strategy, fontsize=13)
    plt.xlabel('Used NUMA nodes', fontsize=11)
    if applicazione == 'SD':
        plt.ylabel('Throughput (M t/s)', fontsize=11)
    if applicazione == 'WC':
        plt.ylabel('Throughput (MB/s)', fontsize=11)
    if applicazione == 'FD':
        plt.ylabel('Throughput (M t/s)', fontsize=11)
    if applicazione == 'TM':
        plt.ylabel('Throughput (K t/s)', fontsize=11)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, "--p=" + parallelism + "_" + "--b=" + str(batch) + '.png')
    plt.tight_layout()


    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_grafo_linee_ffvsOS(applicazione, parallelism, max_batch, titolo, datiff, datiOS, max_y):
    if not datiff or not datiOS:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = ['0'] + [str(2 ** i) for i in range(1, max_batch) if 2 ** i <= max_batch]
    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie_ff = [val['media'] for val in datiff.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std_ff = [val['dev_std'] for val in datiff.values()]  # Estrae il valore 'dev_std' per ogni elemento
    medie_OS = [val['media'] for val in datiOS.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std_OS = [val['dev_std'] for val in datiOS.values()]  # Estrae il valore 'dev_std' per ogni elemento
    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.008
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/ffvsOS'

    # Creazione del grafico
    plt.figure(figsize=(6, 4))

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
        label='FastFlow pinning throughput', marker='s', color='#1B4F72',
        linestyle='-', linewidth=2, elinewidth=1.5, capsize=0
    )

    # Linea per datiOS con barre di errore
    plt.errorbar(
        etichette_asse_x, medie_OS, yerr=dev_std_OS,
        label='OS Scheduler throughput ', marker='s', color='#C41E3A',
        linestyle='-', linewidth=2, elinewidth=1, capsize=0
    )

    # Linea per datiff (FastFlow)
    #plt.plot(etichette_asse_x, medie_ff, label=r'$\mu$ throughput FastFlow pinning', marker='s', color='#1B4F72', linestyle='-', linewidth=2)

    # Linea per datiOS
    #plt.plot(etichette_asse_x, medie_OS, label=r'$\mu$ throughput OS scheduler', marker='s', color='#C41E3A', linestyle='-', linewidth=2)


    # Titoli e etichette
    plt.title(titolo, fontsize=16)
    plt.xlabel('Batch Size', fontsize=14)
    if applicazione == "SD":
        plt.ylabel('Throughput (M t/s)', fontsize=14)
    if applicazione == "WC":
        plt.ylabel('Throughput (MB/s)', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Legenda
    plt.legend(fontsize=10, loc='upper left')

    # Griglia
    #plt.grid(visible=True, linestyle='--', alpha=0.6)

    # Salvataggio del grafico
    save_path = os.path.join(save_dir, f"{applicazione+"_"+parallelism}.png")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_grafo_linee_WinKey(applicazione, parallelism, batch, titolo, dati, max_y, min_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/WinKey'

    #etichette asse x
    etichette_asse_x = ['Win=10k \n Key=10k', 'Win=10k \n Key=50k', 'Win=10k \n Key=100k', 'Win=100k \n Key=10k', 'Win=100k \n Key=50k', 'Win=100k \n Key=100k', 'Win=500k \n Key=10k', 'Win=500k \n Key=50k', 'Win=500k \n Key=100k' ]

    # Combinazioni di Win e Key
    combinazioni = [
        ('Win=10k', 'Key=10k'), ('Win=10k', 'Key=50k'), ('Win=10k', 'Key=100k'),
        ('Win=100k', 'Key=10k'), ('Win=100k', 'Key=50k'), ('Win=100k', 'Key=100k'),
        ('Win=500k', 'Key=10k'), ('Win=500k', 'Key=50k'), ('Win=500k', 'Key=100k')
    ]

    # Estrazione dinamica delle strategie dalla struttura
    strategie = list(dati['Win=100k']['Key=100k'].keys())  # Prende le chiavi di una combinazione di 'Win' e 'Key'
    #strategie.pop(0)

    # Raggruppiamo i valori per ciascuna strategia
    y_values = {strategy: [] for strategy in strategie}
    yerr_values = {strategy: [] for strategy in strategie}

    # Riempire i dati per ogni combinazione di Win e Key
    for win, key in combinazioni:
        for strategy in strategie:
            media = dati[win][key].get(strategy, {}).get('media', 0)
            dev_std = dati[win][key].get(strategy, {}).get('dev_std', 0)
            y_values[strategy].append(media)
            yerr_values[strategy].append(dev_std)

    # Creazione del grafico
    plt.figure(figsize=(7, 5))

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y, min_y)
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

    sns_colors = sns.color_palette("deep", len(strategie))

    # Tracciare una linea per ogni strategia con barre di errore
    for idx, (strategy, y) in enumerate(y_values.items()):
        plt.errorbar(
            range(len(etichette_asse_x)), y, yerr=yerr_values[strategy], label=strategy,
            marker='s', capsize=2, color=sns_colors[idx], linestyle='-', linewidth=1.5
        )

    # Titoli e etichette
    plt.title(titolo, fontsize=14)
    plt.xlabel('Key-Window configuration', fontsize=12)
    plt.ylabel('Throughput (M t/s)', fontsize=12)
    plt.xticks(fontsize=10)
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=10, rotation=30)
    plt.yticks(fontsize=10)

    # Legenda
    if parallelism == "8,8,8,8":
        plt.legend(fontsize=10, loc='upper left', ncol=3)
    else:
        plt.legend(fontsize=10, loc='upper left', ncol=2)

    # Griglia
    #plt.grid(visible=True, linestyle='--', alpha=0.6)

    # Salvataggio del grafico
    save_path = os.path.join(save_dir, f"{applicazione+"_-p"+parallelism+"_-b"+str(batch)}.png")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_grafo_linee_copyDataset(applicazione, parallelism, batch, titolo, dati, max_y, min_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/copyDataset'

    #etichette asse x
    etichette_asse_x = list(dati['ff_queue_len=32786']['constructor'].keys())
    etichette_asse_x = [
        label.replace('Src-Snk grouping', 'Src-Snk\ngrouping')
        .replace('Pipeline grouping', 'Pipeline\ngrouping')
        .replace('A2A grouping', 'A2A\ngrouping')
        .replace('A2A splitting', 'A2A\nsplitting')
        .replace('Stage grouping', 'Stage\ngrouping')
        .replace('Semipipeline grouping', 'Semipipeline\ngrouping')
        for label in etichette_asse_x]

    fullLen_constructor = list(dati['ff_queue_len=32786']['constructor'].values())
    fullLen_operator = list(dati['ff_queue_len=32786']['operator'].values())
    #smallLen_constructor = list(dati['ff_queue_len=16']['constructor'].values())
    #smallLen_operator = list(dati['ff_queue_len=16']['operator'].values())

    # Creazione del grafico
    plt.figure(figsize=(6, 4))

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y, min_y)
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

    sns_colors = sns.color_palette("deep", 4)

    # Tracciare una linea per ogni strategia con barre di errore
    plt.errorbar(
        range(len(etichette_asse_x)),
        [d['media'] for d in fullLen_constructor],
        yerr=[d['dev_std'] for d in fullLen_constructor],
        label='Local memory policy',
        marker='s', capsize=2, color=sns_colors[0], linestyle='-', linewidth=1.5
        )
    plt.errorbar(
        range(len(etichette_asse_x)),
        [d['media'] for d in fullLen_operator],
        yerr=[d['dev_std'] for d in fullLen_operator],
        label='Custom dataset allocation',
        marker='s', capsize=2, color=sns_colors[3], linestyle='-', linewidth=1.5
    )
    '''plt.errorbar(
        range(len(etichette_asse_x)),
        [d['media'] for d in smallLen_constructor],
        yerr=[d['dev_std'] for d in smallLen_constructor],
        label='code ff=16, copia dataset-->costruttore',
        marker='o', capsize=2, color=sns_colors[3], linestyle='-', linewidth=1.5
    )
    plt.errorbar(
        range(len(etichette_asse_x)),
        [d['media'] for d in smallLen_operator],
        yerr=[d['dev_std'] for d in smallLen_operator],
        label='code ff=16, copia dataset-->operator',
        marker='o', capsize=2, color=sns_colors[3], linestyle='--', linewidth=1.5
    )'''

    # Titoli e etichette
    plt.title(titolo, fontsize=14)
    plt.xlabel('Pinning strategies', fontsize=11)
    plt.ylabel('Throughput (M t/s)', fontsize=12)
    plt.xticks(fontsize=11)
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=10, rotation=0)
    plt.yticks(fontsize=11)

    # Legenda
    plt.legend(fontsize=10, loc='upper left', ncol=1)

    # Griglia
    #plt.grid(visible=True, linestyle='--', alpha=0.6)

    # Salvataggio del grafico
    save_path = os.path.join(save_dir, f"{applicazione+"_-p"+parallelism+"_-b"+str(batch)}.png")
    plt.tight_layout()
    print(f"Grafico salvato in: {save_path}")
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_grafo_linee_ff_queue_length(applicazione, parallelism, batch, titolo, dati, max_y, min_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/ff_queue_length/'

    #etichette asse x
    etichette_asse_x = list(dati['ff_queue_len=32786'].keys())
    etichette_asse_x = [
        label.replace('Src-Snk grouping', 'Src-Snk\ngrouping')
        .replace('Pipeline grouping', 'Pipeline\ngrouping')
        .replace('A2A grouping', 'A2A\ngrouping')
        .replace('A2A splitting', 'A2A\nsplitting')
        .replace('Stage grouping', 'Stage\ngrouping')
        .replace('Semipipeline grouping', 'Semipipeline\ngrouping')
        for label in etichette_asse_x]

    fullLen = list(dati['ff_queue_len=32786'].values())
    smallLen= list(dati['ff_queue_len=16'].values())

    # Creazione del grafico
    plt.figure(figsize=(6, 4))

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y, min_y)
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

    sns_colors = sns.color_palette("deep", 4)

    # Tracciare una linea per ogni strategia con barre di errore
    plt.errorbar(
        range(len(etichette_asse_x)),
        [d['media'] for d in fullLen],
        yerr=[d['dev_std'] for d in fullLen],
        label='Queue size = 32786',
        marker='s', capsize=2, color=sns_colors[0], linestyle='-', linewidth=1.5
        )
    plt.errorbar(
        range(len(etichette_asse_x)),
        [d['media'] for d in smallLen],
        yerr=[d['dev_std'] for d in smallLen],
        label='Queue size = 16',
        marker='s', capsize=2, color=sns_colors[3], linestyle='-', linewidth=1.5
    )

    # Titoli e etichette
    plt.title(titolo, fontsize=14)
    plt.xlabel('Pinning strategies', fontsize=12)
    if applicazione == "SD" or applicazione == "FD":
        plt.ylabel('Throughput (M t/s)', fontsize=12)
    if applicazione == "WC":
        plt.ylabel('Throughput (MB/s)', fontsize=12)
    if applicazione == "TM":
        plt.ylabel('Throughput (K t/s)', fontsize=12)
    plt.xticks(fontsize=12)
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=11, rotation=0)
    plt.yticks(fontsize=12)

    # Legenda
    plt.legend(fontsize=12, loc='upper left', ncol=2)

    # Griglia
    #plt.grid(visible=True, linestyle='--', alpha=0.6)

    # Salvataggio del grafico
    save_path = os.path.join(save_dir, f"{applicazione+"_-p"+parallelism+"_-b"+str(batch)}.png")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_istogramma_app(applicazione, parallelism, batch, ff_queue_length, titolo, numanode, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = list(dati.keys())
    etichette_asse_x = [
        label.replace('Src-Snk grouping', 'Src-Snk\ngrouping')
        .replace('Pipeline grouping', 'Pipeline\ngrouping')
        .replace('A2A grouping', 'A2A\ngrouping')
        .replace('A2A splitting', 'A2A\nsplitting')
        .replace('Stage grouping', 'Stage\ngrouping')
        .replace('Semipipeline grouping', 'Semipipeline\ngrouping')
        for label in etichette_asse_x]

    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie = [val['media'] for val in dati.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std = [val['dev_std'] for val in dati.values()]  # Estrae il valore 'dev_std' per ogni elemento
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.015

    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/Pinning'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicazione,parallelism,"batch="+str(batch), "ff_queue_length="+str(ff_queue_length))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste


    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y)
    if(yticks_values == [] or yticks_labels == []):
        raise ValueError("yticks vuoti")

    # Creazione dell'istogramma
    if parallelism == "1,1,1,1":
        plt.figure(figsize=(5, 4))
    if parallelism == "2,2,2,2":
        plt.figure(figsize=(5, 4))
    if parallelism == "4,4,4,4":
        plt.figure(figsize=(6, 5))
    if parallelism == "8,8,8,8":
        plt.figure(figsize=(6, 5))

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
    bars_handle_1 = Line2D([0], [0], color=colore_default, lw=6, label=r'$\mu$ throughput FF')
    bars_handle_2 = Line2D([0], [0], color=colore_pin, lw=6, label=r'$\mu$ throughput strategie custom')
    handles.append(bars_handle_1)
    handles.append(bars_handle_2)
    labels.append('FastFlow throughput')
    labels.append('Custom strategies throughput')

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
                label=r'$\sigma$' + ' negligible' if not has_deviation_symbol else ''
            )
            has_deviation_symbol = True

    # Se ci sono barre di errore, aggiungi la linea nera nella legenda
    #if has_err_bars:
    #    error_handle = Line2D([0], [0], color='black', lw=1, label='Deviazione standard')
    #    handles.append(error_handle)
    #    labels.append(r'$\sigma$ throughput')

    # Se ci sono simboli di deviazione trascurabile, aggiungi il punto nella legenda
    if has_deviation_symbol:
        symbol_handle = Line2D([0], [0], marker='o', color='black', lw=0, markersize=5,
                               label=r'$\sigma$ negligible')
        handles.append(symbol_handle)
        labels.append(r'$\sigma$ negligible')


    plt.legend(handles=handles, labels=labels, loc='upper left', fontsize=10)

    # Impostiamo il formato dei numeri sull'asse Y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels, fontsize = 11)

    # Impostiamo le etichette per l'asse X
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=10)
    plt.title(titolo, fontsize=12)
    plt.xlabel('Pinning strategies', fontsize=11)
    if applicazione == "TM":
        plt.ylabel('Throughput (K t/s)', fontsize=11)
    else:
        if applicazione == "WC":
            plt.ylabel('Throughput (MB/s)', fontsize=11)
        else:
            plt.ylabel('Throughput (M t/s)', fontsize=11)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, "--p=" + parallelism + "_" + "--b=" + str(batch) + '.png')
    plt.tight_layout()


    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_istogramma_strategie_profiling(applicazione, parallelism, batch, ff_queue_length, titolo, numanode, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = list(dati.keys())
    etichette_asse_x = [
        label.replace('Src-Snk grouping', 'Src-Snk\ngrouping')
        .replace('Pipeline grouping', 'Pipeline\ngrouping')
        .replace('A2A grouping', 'A2A\ngrouping')
        .replace('A2A splitting', 'A2A\nsplitting')
        .replace('Stage grouping', 'Stage\ngrouping')
        .replace('Semipipeline grouping', 'Semipipeline\ngrouping')
        for label in etichette_asse_x]

    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie = [val['media'] for val in dati.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std = [val['dev_std'] for val in dati.values()]  # Estrae il valore 'dev_std' per ogni elemento
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.015

    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/istogrammi_strategie_profiling/'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicazione)
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste


    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y)
    if(yticks_values == [] or yticks_labels == []):
        raise ValueError("yticks vuoti")

    # Creazione dell'istogramma
    if parallelism == "1,1,1,1":
        plt.figure(figsize=(5, 4))
    if parallelism == "2,2,2,2":
        plt.figure(figsize=(5, 4))
    if parallelism == "4,4,4,4":
        plt.figure(figsize=(6, 5))
    if parallelism == "8,8,8,8":
        plt.figure(figsize=(6, 5))

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
    bars_handle_1 = Line2D([0], [0], color=colore_default, lw=6, label=r'$\mu$ throughput FF')
    bars_handle_2 = Line2D([0], [0], color=colore_pin, lw=6, label=r'$\mu$ throughput strategie custom')
    handles.append(bars_handle_1)
    handles.append(bars_handle_2)
    labels.append('FastFlow throughput')
    labels.append('Custom strategies throughput')

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
                label=r'$\sigma$' + ' negligible' if not has_deviation_symbol else ''
            )
            has_deviation_symbol = True

    # Se ci sono barre di errore, aggiungi la linea nera nella legenda
    #if has_err_bars:
    #    error_handle = Line2D([0], [0], color='black', lw=1, label='Deviazione standard')
    #    handles.append(error_handle)
    #    labels.append(r'$\sigma$ throughput')

    # Se ci sono simboli di deviazione trascurabile, aggiungi il punto nella legenda
    if has_deviation_symbol:
        symbol_handle = Line2D([0], [0], marker='o', color='black', lw=0, markersize=5,
                               label=r'$\sigma$ negligible')
        handles.append(symbol_handle)
        labels.append(r'$\sigma$ negligible')


    plt.legend(handles=handles, labels=labels, loc='upper left', fontsize=10)

    # Impostiamo il formato dei numeri sull'asse Y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels, fontsize = 11)

    # Impostiamo le etichette per l'asse X
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=10)
    plt.title(titolo, fontsize=12)
    plt.xlabel('Pinning Strategies', fontsize=11)
    if applicazione == "TM":
        plt.ylabel('Throughput (K t/s)', fontsize=11)
    else:
        if applicazione == "WC":
            plt.ylabel('Throughput (MB/s)', fontsize=11)
        else:
            plt.ylabel('Throughput (M t/s)', fontsize=11)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, "--p=" + parallelism + "_" + "--b=" + str(batch) + '.png')
    plt.tight_layout()


    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_istogramma_no_KeyBy(applicazione, parallelism, batch, ff_queue_length, titolo, numanode, dati, max_y):
    if not dati:
        raise ValueError("Il parametro 'dati' è vuoto o non valido.")
    etichette_asse_x = list(dati.keys())
    etichette_asse_x = [
        label.replace('Src-Snk grouping', 'Src-Snk\ngrouping')
        .replace('Pipeline grouping', 'Pipeline\ngrouping')
        .replace('A2A grouping', 'A2A\ngrouping')
        .replace('A2A splitting', 'A2A\nsplitting')
        .replace('Stage grouping', 'Stage\ngrouping')
        .replace('Semipipeline grouping', 'Semipipeline\ngrouping')
        .replace('Pipeline grouping (no keyby)', 'Pipeline\ngrouping\n(no keyby)')
        for label in etichette_asse_x]

    #etichette_asse_x = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Scenario 6","Scenario 7"]
    medie = [val['media'] for val in dati.values()]  # Estrae il valore 'media' per ogni elemento
    dev_std = [val['dev_std'] for val in dati.values()]  # Estrae il valore 'dev_std' per ogni elemento
    # Calcolo del rapporto media/deviazione standard
    rapporto_soglia = 0.015

    #dati_asse_x = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 6_999_999]
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/no_KeyBy/'

    # calcola il path completo
    complete_path = os.path.join(save_dir,applicazione)
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste


    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_app(applicazione, max_y)
    if(yticks_values == [] or yticks_labels == []):
        raise ValueError("yticks vuoti")

    # Creazione dell'istogramma
    if parallelism == "1,1,1,1":
        plt.figure(figsize=(5, 4))
    if parallelism == "2,2,2,2":
        plt.figure(figsize=(5, 4))
    if parallelism == "4,4,4,4":
        plt.figure(figsize=(5, 4))
    if parallelism == "8,8,8,8":
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
    #cmap=matplotlib.colormaps['Blues']
    #colors = cmap(np.linspace(1.0, 0.4, len(dati_asse_x)))  # Evita estremi per miglior visibilità
    colore_default = '#C41E3A'  # Rosso cardinale/porpora
    colore_pin = '#1B4F72'  # Blu scuro. Prima: #2A6189
    colors = [colore_pin] * (len(medie) - 1) + [colore_default]

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
    bars_handle_1 = Line2D([0], [0], color=colore_default, lw=6, label=r'$\mu$ throughput FF')
    bars_handle_2 = Line2D([0], [0], color=colore_pin, lw=6, label=r'$\mu$ throughput strategie custom')
    handles.append(bars_handle_1)
    handles.append(bars_handle_2)
    labels.append('No key-by throughput')
    labels.append('Key-by throughput')

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
                label=r'$\sigma$' + ' negligible' if not has_deviation_symbol else ''
            )
            has_deviation_symbol = True

    # Se ci sono barre di errore, aggiungi la linea nera nella legenda
    #if has_err_bars:
    #    error_handle = Line2D([0], [0], color='black', lw=1, label='Deviazione standard')
    #    handles.append(error_handle)
    #    labels.append(r'$\sigma$ throughput')

    # Se ci sono simboli di deviazione trascurabile, aggiungi il punto nella legenda
    if has_deviation_symbol:
        symbol_handle = Line2D([0], [0], marker='o', color='black', lw=0, markersize=5,
                               label=r'$\sigma$ prestazioni trascurabile')
        handles.append(symbol_handle)
        labels.append(r'$\sigma$ negligible')


    plt.legend(handles=handles, labels=labels, loc='upper left', fontsize=10)

    # Impostiamo il formato dei numeri sull'asse Y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.yticks(yticks_values, yticks_labels, fontsize = 11)

    # Impostiamo le etichette per l'asse X
    plt.xticks(range(len(etichette_asse_x)), etichette_asse_x, fontsize=10)
    plt.title(titolo, fontsize=12)
    plt.xlabel('Pinning Strategies', fontsize=11)
    if applicazione == "TM":
        plt.ylabel('Throughput (K t/s)', fontsize=11)
    else:
        if applicazione == "WC":
            plt.ylabel('Throughput (MB/s)', fontsize=11)
        else:
            plt.ylabel('Throughput (M t/s)', fontsize=11)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, "--p=" + parallelism + "_" + "--b=" + str(batch) + '.png')
    plt.tight_layout()


    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()


def crea_istogramma_profiling(applicazione, coppia, parallelismo, batch, strategia1, total_accesses1, total_misses1, strategia2, total_accesses2, total_misses2, max_y):

    etichette_asse_x = ["Total accesses", "Total misses"]
    save_dir = '/home/lorenzo/Desktop/Grafici_Tesi/Profiling'

    # calcola il path completo
    complete_path = os.path.join(save_dir, applicazione, "coppia_test_" + str(coppia))
    os.makedirs(complete_path, exist_ok=True)  # Crea la cartella se non esiste

    # Calcola le etichette e i valori dei ticks per l'asse Y
    yticks_values, yticks_labels = calcola_etichette_assey_profiling(max_y)

    # Creazione dell'istogramma
    plt.figure(figsize=(5, 4))

    # Impostiamo i limiti dell'asse X in modo che parta da 0 e arrivi al massimo valore dei dati
    plt.xlim(-0.5, len(etichette_asse_x) - 0.5)

    # Disegnare le linee orizzontali per ogni valore di yticks_values
    for ytick in yticks_values:
        plt.hlines(ytick, -0.5, len(etichette_asse_x) - 0.5, colors='gray', linestyles='--', linewidth=0.6,
                   zorder=1)  # Linea tratteggiata, zorder basso per metterle sotto le barre
    # Aggiungere linee a metà tra ogni intervallo
    if(max_y <= 8_000_000_000):
        for i in range(1, len(yticks_values)):
            halfway = (yticks_values[i] + yticks_values[i - 1]) / 2  # Calcolare il punto centrale tra i tick
            plt.hlines(halfway, -0.5, len(etichette_asse_x) - 0.5, colors='lightgray', linestyles='--',
                       linewidth=0.8)  # Linea leggera tra i tick

    # Impostiamo la posizione delle barre
    bar_width = 0.30  # Larghezza delle barre
    offset = 0.75  # Distanza tra le due coppie di barre

    #sns_colors = sns.color_palette("deep", 8)

    #blue_palette = plt.cm.Blues  # Scala di blu
    #red_palette = plt.cm.Reds  # Scala di rosso
    color1 = '#63993D'
    color2 = '#204D00'

    # Creazione delle barre per il gruppo 1 (total_accesses1 e total_misses1)
    plt.bar(0, total_accesses1, width=bar_width, color=color2, alpha=1, zorder=2)  # Total accesses 1
    plt.bar(0.30, total_accesses2, width=bar_width, color=color1, alpha=1, zorder=2)  # Total misses 1

    # Creazione delle barre per il gruppo 2 (total_accesses2 e total_misses2)
    plt.bar(0.80, total_misses1, width=bar_width, color=color2, alpha=1, zorder=2)
    plt.bar(1.10, total_misses2, width=bar_width, color=color1, alpha=1, zorder=2)

    # Impostiamo il formato dei numeri sull'asse y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.ylim(bottom=0)
    plt.ylabel('Billions', fontsize=10)
    plt.yticks(yticks_values, yticks_labels, fontsize = 10)

    # Personalizzazione delle etichette sull'asse X
    plt.xticks([np.mean([0, 0.30]), np.mean([0.80, 1.10])], etichette_asse_x)  # Centra le etichette dei gruppi
    # Aggiungiamo il titolo
    if(applicazione == "SD"):
        plt.title("Spike Detection; " + "Parallelism: " + parallelismo + "; " + "Batch: " + str(batch), fontsize=11)
    elif (applicazione == "WC"):
            plt.title("Word Count; " + "Parallelism: " + parallelismo + "; " + "Batch: " + str(batch), fontsize=11)
    elif (applicazione == "FD"):
            plt.title("Fraud Detection; " + "Parallelism: " + parallelismo + "; " + "Batch: " + str(batch), fontsize=11)
    elif (applicazione == "TM"):
        plt.title("Traffic Monitoring; " + "Parallelism: " + parallelismo + "; " + "Batch: " + str(batch), fontsize=11)


    # Aggiungi la legenda per i colori
    plt.bar(0, 0, color=color2, alpha=1, label=strategia1)  # Barra invisibile per il colore blu
    plt.bar(0, 0, color=color1, alpha=1, label=strategia2)  # Barra invisibile per il colore blu scuro
    plt.legend(loc='upper left', ncol=2, fontsize=9)

    # Salvataggio del grafico
    save_path = os.path.join(complete_path, 'istogramma_coppia' + str(coppia) + '.png')
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Grafico salvato in: {save_path}")

    # Mostra il grafico
    plt.show()

def crea_istogrammi_profiling():
    grafici = json_parse_profiling('istogrammi_profiling_2.json')

    strategia1 = ""
    strategia2 = ""
    total_accesses1 = 0
    total_accesses2 = 0
    total_misses1 = 0
    total_misses2 = 0
    i = 0

    while i <= len(grafici) :
        applicazione = grafici[i]['applicazione']
        parallelismo = grafici[i]['parallelismo']
        batch = grafici[i]['batch']
        coppia = grafici[i]['coppia_test']
        test = grafici[i]['test']
        j = i
        while(grafici[j]['applicazione'] == applicazione and grafici[j]['coppia_test'] == coppia and grafici[j]['test'] == test) :
            if(strategia1 == ""):
                strategia1 = grafici[j]['strategia']
            total_accesses1 += grafici[j]['dati']['Total accesses']
            total_misses1 += grafici[j]['dati']['Total misses']
            j+=1
        test = grafici[j]['test']
        while(grafici[j]['applicazione'] == applicazione and grafici[j]['coppia_test'] == coppia and grafici[j]['test'] == test) :
            if(strategia2 == ""):
                strategia2 = grafici[j]['strategia']
            total_accesses2 += grafici[j]['dati']['Total accesses']
            total_misses2 += grafici[j]['dati']['Total misses']
            j+=1
            if(j == len(grafici)): break;

        max_y = (math.ceil(max(total_accesses1, total_accesses2) / 1_000_000_000) * 1_000_000_000)
        if(applicazione == "SD" and parallelismo == "2,2,2,2" and batch == 0):
            max_y += 1_000_000_000
        if(applicazione == "TM" and parallelismo == "4,4,4,4" and batch == 32):
            max_y += 1_000_000_000
        # Chiamata al metodo per creare l'istogramma
        crea_istogramma_profiling(applicazione, coppia, parallelismo, batch, strategia1, total_accesses1, total_misses1, strategia2, total_accesses2, total_misses2, max_y)
        total_accesses1 = 0
        total_accesses2 = 0
        total_misses1 = 0
        total_misses2 = 0
        strategia1 = ""
        strategia2 = ""
        i = j


def crea_istogrammi_strategie_per_profiling():
    grafici = json_parse_pinning('istogrammi_strategie_per_profiling.json')
    for grafico in grafici:
        #if grafico["applicazione"] == "TM":
            crea_istogramma_strategie_profiling(grafico["applicazione"], grafico["parallelism"], grafico["batch"],
                                grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"],
                                grafico["max"])

def crea_grafi_linee_ffvsOS():
    grafici = json_parse_ffvsOS('ffvsOS.json')
    for grafico in grafici:
        crea_grafo_linee_ffvsOS(grafico["applicazione"], grafico["parallelism"], grafico["max_batch"], grafico["titolo"],
                            grafico["dati_ff"], grafico["dati_OS"], grafico["max"])

def crea_grafi_linee_copyDataset():
    grafici = json_parse_WinKey('copy_of_the_dataset.json')
    for grafico in grafici:
        crea_grafo_linee_copyDataset(grafico["applicazione"], grafico["parallelism"], grafico["batch"],
                                grafico["titolo"], grafico["dati"], grafico["max"], grafico["min"])

def crea_grafi_linee_ff_queue_length():
    grafici = json_parse_WinKey('ff_queue_lenght.json')
    for grafico in grafici:
        crea_grafo_linee_ff_queue_length(grafico["applicazione"], grafico["parallelism"], grafico["batch"],
                                grafico["titolo"], grafico["dati"], grafico["max"], grafico["min"])

def crea_grafi_linee_WinKey():
    grafici = json_parse_WinKey('SD_key_window.json')
    for grafico in grafici:
        crea_grafo_linee_WinKey(grafico["applicazione"], grafico["parallelism"], grafico["batch"],
                                grafico["titolo"], grafico["dati"], grafico["max"], grafico["min"])

def crea_grafi_scelta_numanode():
    grafici = json_parse_scelta_numanode('scelta_numanode.json')
    for grafico in grafici:
        crea_istogramma_scelta_numanode(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["strategy"], grafico["dati"], grafico["max"])

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

def crea_istogrammi_no_KeyBy():
    grafici = json_parse_pinning('no_keyby.json')
    for grafico in grafici:
        crea_istogramma_no_KeyBy(grafico["applicazione"], grafico["parallelism"], grafico["batch"], grafico["ff_queue_length"], grafico["titolo"], grafico["numanode"], grafico["dati"], grafico["max"])

def main():

    crea_istogrammi_profiling()

# Questa parte è importante: assicura che la funzione main() venga eseguita solo
# quando il file viene eseguito come script, non quando viene importato come modulo
if __name__ == "__main__":
    main()
