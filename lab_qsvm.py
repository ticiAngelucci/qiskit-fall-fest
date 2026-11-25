"""Laboratorio corto para el Qiskit Fall Fest.

Carga un recorte real de CICIDS2017 (BENIGN contra DDoS), lo baja a 3
variables y entrena un QSVM mínimo. No es la tesina.

El kernel cuántico no se calcula sobre las 240 filas: cada par de muestras
es un circuito. N_TRAIN y N_TEST están chicos a propósito.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from qiskit.circuit.library import ZZFeatureMap
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.state_fidelities import ComputeUncompute

SEED = 7
N_TRAIN = 24
N_TEST = 8
CSV = Path(__file__).resolve().parent / "data" / "cicids_benign_ddos.csv"


def cargar(path: Path) -> tuple[np.ndarray, np.ndarray]:
    tabla = pd.read_csv(path)
    tabla.columns = [c.strip() for c in tabla.columns]
    y = (tabla["Label"].str.strip() == "DDoS").astype(int).to_numpy()
    x = tabla.drop(columns=["Label"]).apply(pd.to_numeric, errors="coerce")
    x = x.replace([np.inf, -np.inf], np.nan).dropna()
    y = y[x.index]
    return x.to_numpy(dtype=float), y


def main() -> None:
    x, y = cargar(CSV)
    print(f"filas {len(y)}  columnas {x.shape[1]}  DDoS {int(y.sum())}")

    # 1–3. Misma escala y 3 componentes: una por qubit.
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=SEED, stratify=y
    )
    scaler = StandardScaler().fit(x_train)
    pca = PCA(n_components=3, random_state=SEED).fit(scaler.transform(x_train))
    z_train = pca.transform(scaler.transform(x_train))
    z_test = pca.transform(scaler.transform(x_test))
    print("varianza que conservan las 3 componentes:", np.round(pca.explained_variance_ratio_, 3))

    # El circuito siempre usa 3 qubits. Estas N filas son las que se comparan.
    z_train, y_train = z_train[:N_TRAIN], y_train[:N_TRAIN]
    z_test, y_test = z_test[:N_TEST], y_test[:N_TEST]

    # 4. H, RZ y cruce solo entre vecinos. El circuito no clasifica.
    feature_map = ZZFeatureMap(feature_dimension=3, reps=1, entanglement="linear")
    print(feature_map.decompose())

    # 5. K es la probabilidad de medir 000. El simulador no tiene ruido.
    kernel = FidelityQuantumKernel(
        feature_map=feature_map,
        fidelity=ComputeUncompute(sampler=StatevectorSampler()),
    )
    k_train = kernel.evaluate(z_train)
    k_test = kernel.evaluate(z_test, z_train)

    # 6. La SVM lee la matriz ya calculada y asigna BENIGN o DDoS.
    qsvm = SVC(kernel="precomputed")
    qsvm.fit(k_train, y_train)
    pred = qsvm.predict(k_test)
    print("QSVM  aciertos", int((pred == y_test).sum()), "de", len(y_test))

    # Misma cohorte chica, kernel clásico. No es el Random Forest de la tesina.
    clasico = SVC(kernel="rbf")
    clasico.fit(z_train, y_train)
    pred_c = clasico.predict(z_test)
    print("RBF   aciertos", int((pred_c == y_test).sum()), "de", len(y_test))
    print("clases QSVM", pred.tolist())
    print("clases RBF ", pred_c.tolist())
    print("reales    ", y_test.tolist())


if __name__ == "__main__":
    main()
