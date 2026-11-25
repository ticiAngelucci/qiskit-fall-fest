# De dónde sale este CSV

`cicids_benign_ddos.csv` es un recorte de CICIDS2017, no el dataset entero y no la cohorte de la tesina.

- Archivo original: `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`
- Publicación: Canadian Institute for Cybersecurity, University of New Brunswick. [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)
- Quedaron 120 flujos BENIGN y 120 DDoS, elegidos al azar entre las filas con todos los valores numéricos y finitos. Semilla 7.
- La columna de clase se llama `Label`.

El ZIP oficial pesa mucho más que esto. Para el taller alcanza este recorte. Si más adelante quieren otra muestra, parten del CSV del viernes y vuelven a muestrear. No mezclen este archivo con el tráfico Live de la tesina: un flujo no es una ventana de captura.
