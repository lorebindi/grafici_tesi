# grafici_tesi

Questo script python l'ho usato per creare i grafici da inserire nella tesi.

Cosa contengono i file `.json`:

- `ffvsOS.json`: contiene i throughtut medi raccolti dalle esecuzioni di SpikeDetection e WordCount sia con l'utilizzo dello scheduler del sistema operativo che con il pinning del livello FastFlow.
- `scelta_numanode.json`: contienemedia e deviazione standard dei throughput delle diverse strategie di pinning al variare del nodo NUMA utilizzato.
- `istogrammi_pinning_SD.json`: contiene media e deviazione standard dei throughput delle diverse strategie di pinning al variare del parallelismo e del batch solo dell'applicazione SpikeDetection.
- `istogrammi_pinning_WC.json`: contiene media e deviazione standard dei throughput delle diverse strategie di pinning al variare del parallelismo e del batch solo dell'applicazione WordCount.
- `istogrammi_pinning_FD.json`: contiene media e deviazione standard dei throughput delle diverse strategie di pinning al variare del parallelismo e del batch solo dell'applicazione FraudDetection.
- `istogrammi_pinning_TM.json`: contiene media e deviazione standard dei throughput delle diverse strategie di pinning al variare del parallelismo e del batch solo dell'applicazione Traffic monitoring.
- `istogrammi_profiling.json`: contiene gli accessi e i miss totali per ogni CCX coinvolto da ciascun test di profiling effettuato.
- `istogrammi_profiling_2.json`: contiene SOLO un sottoinsieme dei test di profiling con informazioni aggiuntive come parallelismo, batch e strategia di pinning oltre ad ccessi e i miss totali per ogni CCX coinvolto.
- `profiling_strategie_non_previste.json`: contiene il la parte dei risultati di profiling su strategie di pinning che non rientrano in quelle identificate. 
- `istogrammi_strategie_per_profiling.json`: contiene il sottoinsieme dei dati di `istogrammi_pinning_SD.json`, `istogrammi_pinning_WC.json`, `istogrammi_pinning_FD.json`, `istogrammi_pinning_TM.json`, che sono coinvolti nelle coppie di strategie previste per il profiling.
- `noKeyBy.json`: contiene la media e la deviazione standard del throughput delle applicazioni senza collegamento KeyBy al variare del grado di parallelismo e della dimensione del batch.
- `ff_queue_lenght.json`: contiene la media e la deviazione standard del throughput delle applicazioni con dimensione delle code fastflow pari a 16 elementi al variare del grado di parallelismo e della dimensione del batch.
- `copy_of_the_dataset.json`: contiene la media e la deviazione standard del throughput di SD con "custom dataset allocation" come politica di allocazione del dataset.
- `SD_key_window.json`: contiene la media e la deviazione standard del throughput di SD al variare del numero di chiavi, dimensione delle finestre dell'operatore map, grado di parallelismo e dimensione del batch.

In `graphs_generator.py` usare solo le funzioni indicate nel main e non quelle identificate come *"di sistema"*.
