# QSVM mínimo con CICIDS2017

Base para seguir después del Qiskit Fall Fest. El circuito compara dos flujos. La SVM clásica pone la clase.

No hay captura en vivo, ni hardware, ni un Random Forest. Es el mismo recorrido de la charla, en un archivo que se puede correr.

Repositorio: [github.com/ticiAngelucci/qiskit-fall-fest](https://github.com/ticiAngelucci/qiskit-fall-fest)

Ticiana Angelucci · [LinkedIn](https://www.linkedin.com/in/ticiana-angelucci-12098b23a/)

## Qué pregunta responde

¿Este flujo es tráfico normal o es un DDoS?

- **BENIGN** es el tráfico legítimo.
- **DDoS** es un ataque de denegación de servicio: muchas peticiones coordinadas para dejar un servicio inaccesible.
- Un **flujo** es el resumen de una conexión (duración, paquetes, bytes), no el paquete suelto.

Los datos están en `data/cicids_benign_ddos.csv`: 120 BENIGN y 120 DDoS, recortados del viernes de [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html). El detalle está en `data/ORIGEN.md`. Si al clonar el CSV no está suelto, `lab_qsvm.py` lo junta solo desde `data/parts/`.

## Cómo correrlo

Hace falta Python 3.10 o más nuevo.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python lab_qsvm.py
```

En Windows, el entorno se activa con `.venv\Scripts\activate`.

La primera corrida tarda, porque cada par de flujos es un circuito. Por eso el kernel no se calcula sobre las 240 filas: usa `N_TRAIN = 24` y `N_TEST = 8`. No suban esos números sin mirar el reloj.

## Qué hace `lab_qsvm.py`, en orden

1. Lee el CSV. La columna `Label` es la clase. `y` vale 1 si el flujo es DDoS y 0 si es BENIGN.
2. Estandariza cada columna con lo aprendido en el entrenamiento, para que ninguna domine por la escala.
3. Se queda con 3 componentes principales. El mapa no acepta la tabla entera: acepta un número por qubit.
4. Arma un `ZZFeatureMap` de 3 qubits, una repetición y entrelazado lineal.
   - **H** pone el qubit en superposición. Sin eso, la fase que viene después no cambia la medición.
   - **RZ** escribe la variable de ese qubit como un ángulo.
   - El cruce lineal une solo vecinos: q0 con q1, y q1 con q2. Cada cruce es un CNOT, una fase ZZ y otro CNOT. No hay cruce directo entre q0 y q2.
5. Estima el kernel de fidelidad en un simulador sin ruido. `K[i, j]` es la probabilidad de medir `000` al comparar el flujo i con el j. Cerca de 1, se parecen. Cerca de 0, no.
6. Ajusta una SVM con `kernel="precomputed"`. La matriz ya está calculada: la SVM no arma otro circuito y no elige la clase dentro del circuito.
7. En la misma cohorte chica corre una SVM de kernel RBF, para ver la versión clásica de esa cuenta.

## Qué pueden cambiar

En `lab_qsvm.py`:

- `N_TRAIN` y `N_TEST`. Cada fila de más multiplica la cantidad de circuitos.
- `entanglement="linear"` por `"full"`. El completo cruza todos los pares. Dice casi lo mismo, con más compuertas.
- `reps=1`. Más repeticiones alargan el mapa.

Los aciertos de esta corrida no se comparan con un modelo clásico entrenado sobre todo CICIDS2017. Acá las dos SVM ven las mismas pocas filas.
