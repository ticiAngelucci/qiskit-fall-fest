# Guion para estudiar

**De un flujo de red a un kernel cuántico**
Qiskit Fall Fest 2026 · CuyoConnect · Mendoza
Un QSVM mínimo con Qiskit

Ticiana Angelucci
titiangelucci08@gmail.com
https://github.com/ticiAngelucci/qiskit-fall-fest

| # | Diapositiva | 
|---|---|
| 01 | Portada |
| 02 | En estos 40 minutos |
| 03 | Qué es el aprendizaje automático cuántico |
| 04 | ¿Este tráfico es legítimo o es un DDoS? |
| 05 | No hace falta meter el flujo entero |
| 06 | El circuito no elige la clase |
| 07 | El kernel clásico mide cercanía |
| 08 | Qué pasa con cada par de muestras |
| 09 | Compuerta por compuerta |
| 10 | Por qué este circuito y no otro |
| 11 | El CSV ya es el recorte |
| 12 | Tres variables, tres qubits |
| 13 | K es una probabilidad |
| 14 | La SVM solo lee la matriz |
| 15 | Qué se puede concluir |
| 16 | Gracias por escuchar |

---

## 01 · Portada · 1 min

**De un flujo de red a un kernel cuántico**

“Un QSVM mínimo con Qiskit”

Buenas. Soy Ticiana Angelucci, de CuyoConnect, en Mendoza. En estos 40 minutos vamos a ir de un flujo de red a un kernel cuántico.

No hace falta que hayan usado Qiskit. La idea es una sola. Un circuito puede medir si dos flujos de red se parecen. Una máquina de vectores de soporte, que es un modelo clásico, usa ese parecido para decir si el tráfico es normal o si es un ataque. Eso es un QSVM mínimo: la Q es de cuántico, la SVM es clásica.

Al final se llevan el repositorio, con el pedazo de datos y el código, para repetir este mismo recorrido.

## 02 · Mapa de la hora · 2 min

**En la diapo.**

Vamos a ver cuatro cosas, y en este orden.

Primero, qué es el aprendizaje automático cuántico. No es reemplazar el modelo por un circuito. Es usar un circuito adentro del modelo.

Segundo, el mapa de 3 qubits. Es la forma en que cada flujo entra al circuito. Un flujo trae muchas columnas. El circuito no las acepta todas: acepta un número por qubit.

Tercero, el kernel de fidelidad. Es el parecido entre dos flujos, y ese parecido se mide como una probabilidad. Si se parece a 1, son parecidos. Si se parece a 0, no.

Cuarto, la SVM clásica. Es el algoritmo que, con esos parecidos ya calculados, pone la clase: tráfico normal o ataque.

Cuando terminemos, se llevan el repositorio de GitHub, con el recorte de CICIDS2017, para correr esto ustedes. No hace falta anotar el código ahora. El código está al final de la charla, y el enlace queda en la última diapositiva.

---

## 03 · Concepto · 4 min

**Qué es el aprendizaje automático cuántico**

El aprendizaje automático, el de siempre, hace esto: mira ejemplos que ya tienen etiqueta y ajusta una regla. Después, con esa regla, clasifica un caso nuevo. Si los ejemplos son correos ya marcados como spam o no spam, la regla aprende a marcar el próximo correo.

En el aprendizaje automático cuántico, una parte de esa cuenta sale de un circuito. El dato no se “mete” como un archivo. Entra como el parámetro de una compuerta, o sea como un número que cambia cómo gira el qubit. Cuando se mide el circuito, esa medición devuelve un número. Ese número es lo que el modelo usa.

Acá el circuito no pone la clase. No dice “esto es un ataque”. Lo que hace es escribir cada flujo en un estado cuántico, para poder comparar dos flujos entre sí. Por eso el método es híbrido. La comparación es cuántica. La regla que elige BENIGN o DDoS sigue siendo una SVM clásica.

Miren el dibujo. Arriba están los datos. Bajan al circuito, que son estos tres qubits. El circuito no es el clasificador: es el lugar donde el flujo queda escrito. Abajo está la SVM, y ahí sí hay una sola decisión. No hay dos modelos compitiendo. Hay una sola decisión, y el circuito solo cambia cómo se mide el parecido.

El circuito no clasifica, ni el modelo cuántico reemplaza al clásico.

---

## 04 · Los datos · 4 min

**¿Este tráfico es legítimo o es un DDoS?**

La pregunta de este trabajo es binaria. ¿Este tráfico es legítimo, o es un DDoS?

BENIGN es el tráfico legítimo: lo que pasa en la red cuando alguien navega, manda un mail o usa un servicio, sin atacar. DDoS es denegación de servicio distribuida. Es un ataque. Muchas peticiones, coordinadas, buscan agotar un servicio hasta dejarlo inaccesible. No es un virus que entra a una máquina. Es volumen: tantas peticiones que el servicio deja de responder.

Lo que se clasifica no es un paquete suelto. Es un flujo. Un flujo es el resumen de una conexión: cuánto duró, cuántos paquetes fueron, cuántos bytes, y otros conteos. Una fila de la tabla es un flujo. La última columna dice si ese flujo era BENIGN o DDoS.

Esos flujos salen de CICIDS2017. Es un conjunto público, ya etiquetado, de una red de laboratorio. Lo publicó el Canadian Institute for Cybersecurity, de la Universidad de New Brunswick. Trae varias clases de ataque. Acá se dejan solo dos, BENIGN y DDoS, porque la pregunta es esa: tráfico normal o este ataque. No estamos clasificando todos los ataques del dataset.

El dibujo es para ver la idea, no los números. A la izquierda, BENIGN queda más suelto. A la derecha, DDoS se amontona. El modelo tiene que separar esas dos nubes.

El archivo original es el viernes a la tarde, `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`. El recorte que se llevan tiene 240 flujos: 120 BENIGN y 120 DDoS, 78 columnas, elegidos al azar entre las filas con todos los valores numéricos y finitos. Semilla 7. No es el dataset entero y no es tráfico capturado en vivo.

---

## 05 · Concepto · 3 min

**No hace falta meter el flujo entero**

Un qubit es la unidad del circuito. Hasta que se mide, no está obligado a ser 0 o 1: puede estar en una combinación de los dos. Esa combinación es la superposición. Cuando se mide, el resultado sí es 0 o 1.

Un flujo real tiene decenas de columnas. El mapa cuántico no acepta una tabla. Acepta tantos números como qubits tiene, uno por variable. Si hay tres qubits, entran tres números.

Para pasar de muchas columnas a tres números se usan componentes principales. Son coordenadas nuevas. No son tres columnas elegidas a ojo. Son tres direcciones que concentran la variación del flujo, y reemplazan a las columnas originales. La primera se queda con la variación más grande. La segunda, con lo que quedó. La tercera, con el resto que todavía importa.

Tres no es un óptimo teórico. Nadie demostró que tres sea el mejor número para detectar DDoS. Tres es el tamaño en el que el circuito sigue siendo corto, se puede leer de punta a punta, y todavía mezcla información entre qubits. Con eso alcanza para estimar si dos flujos se parecen, sin meter el vector original de decenas de columnas.

---

## 06 · Concepto · 3 min

**El circuito no elige la clase**

Una SVM, máquina de vectores de soporte, separa dos clases. No busca cualquier frontera. Busca la que deja el margen más amplio entre los ejemplos más difíciles de cada lado. Esos ejemplos, los que quedan pegados a la frontera, son los vectores de soporte. El resto casi no importa: la frontera la definen los que están en el borde.

Para armar esa frontera, la SVM no dibuja la curva a mano. Usa un kernel. El kernel es una función, K de x y z, que devuelve el parecido entre dos ejemplos. x es un flujo, z es otro. K es un número entre 0 y 1.

Cuando ese K no sale de una fórmula clásica, sino de un circuito, la misma SVM se llama QSVM. El circuito no cambia de trabajo. Sigue sin imprimir la etiqueta. Calcula K. Si el valor se acerca a 1, los flujos se parecen. Si se acerca a 0, no. La clase la elige después la SVM clásica, leyendo esos números.

En el dibujo, arriba está esa cuenta: dos flujos y, en el medio, K. Abajo ya no está el circuito. Está la decisión. BENIGN de un lado, DDoS del otro, y la línea dorada es el margen. El circuito fabricó los parecidos. La línea la pone la SVM.

---

## 07 · Concepto · 3 min

**El kernel clásico mide cercanía**

Antes del qubit, el kernel ya existe. K de x y z es el producto entre una transformación de x y la misma transformación de z. No hace falta construir esa transformación. Alcanza con evaluar K. Por eso se llama el truco del kernel: se obtiene el parecido en un espacio más cómodo sin mudarse a ese espacio.

El kernel RBF hace eso con la distancia. La fórmula es K igual a e elevado a menos gamma por la distancia al cuadrado entre x y z. No hace falta escribirla. Lo que dice es simple. Si los dos flujos están cerca, la distancia es chica, la exponencial vale casi 1, y K se acerca a 1. Si están lejos, la exponencial se aplasta y K cae a 0. Gamma fija qué tan rápido cae. Gamma grande: solo se parecen los que están muy pegados. Gamma chica: se toleran flujos más separados.

La decisión de la SVM es el signo de una suma. Cada ejemplo de entrenamiento aporta tres cosas: su clase, un peso, y el K contra el flujo nuevo. Si la suma da positivo, una clase. Si da negativo, la otra. El circuito reemplaza únicamente el cálculo de K. Los pesos y el signo los resuelve la SVM clásica. Cambia la cuenta del parecido. No cambia el clasificador.

La curva de la diapo es esa idea. Cerca, K vale 1. Lejos, K vale 0. El kernel cuántico va a ocupar exactamente este mismo lugar. Donde antes había una distancia, ahora hay una probabilidad medida en el circuito.

---

## 08 · El recorrido · 2 min

**Qué pasa con cada par de muestras**

Para llenar una sola celda de la matriz hay que comparar dos flujos. El recorrido es siempre el mismo.

Primero se carga. El mapa U de x escribe el primer flujo en los tres qubits. U es el circuito que ya vimos: Hadamard, rotación y el cruce entre vecinos. x son las tres variables de ese flujo.

Después se invierte. Se aplica el mapa inverso del segundo flujo, U daga de z. Es el mismo circuito, dado vuelta, con las variables del otro flujo. Si los dos flujos fueran iguales, cargar uno y deshacer el otro dejaría los qubits otra vez en cero.

Después se mide. K es la fidelidad: la probabilidad de medir 000. Si esa probabilidad es alta, el segundo circuito casi deshizo al primero, así que los flujos se parecían. Si es baja, no.

Ese número se anota en una celda de la matriz de kernel. Fila i, columna j, flujo i contra flujo j. Cuando la matriz está llena, la SVM la usa ya calculada y asigna la clase. El circuito no vuelve a entrar en esa decisión.

---

## 09 · El circuito · 4 min

**Compuerta por compuerta**

Se lee de izquierda a derecha, como una partitura. Cada línea horizontal es un qubit y no se corta.

H es Hadamard. Deja cada qubit en superposición, a mitad de camino entre 0 y 1. Sin eso, la fase que viene después no cambia lo que se mide. Si el qubit ya está fijo en 0, girar su fase es como girar un punto que no se mueve: la medición sigue dando 0.

RZ escribe en ese qubit la variable del flujo, como un ángulo. El primer RZ recibe la primera componente. El segundo, la segunda. El tercero, la tercera. Dos flujos distintos dejan ángulos distintos en el mismo circuito. Por eso el estado final depende de quién entró.

Después solo se cruzan vecinos. Primero q0 con q1. Cada cruce es un CNOT, una fase ZZ y otro CNOT. El CNOT es el puntito y el más adentro del círculo: un qubit controla al otro. La caja ZZ es una fase que depende de los dos. El segundo CNOT cierra el bloque. Ese sándwich hace que el estado de un qubit dependa del otro. Si no estuviera, las tres variables vivirían en tres cables separados y el parecido no mezclaría información.

Lo mismo se repite entre q1 y q2. q1 queda en el medio y une a los otros dos. No hay cruce directo entre q0 y q2. No es un olvido del dibujo. Es el entrelazado lineal: solo vecinos.

Y el cierre, otra vez, porque es el error fácil: el circuito no elige la clase. Deja el flujo escrito en el estado, listo para compararlo con otro.

---

## 10 · Por qué este mapa · 3 min

**Por qué este circuito y no otro**

Esta diapo dice por qué el circuito es este y no otro más largo.

H pone al qubit en superposición. Sin eso, la fase de RZ no cambia la medición. RZ guarda la variable como un ángulo: dos flujos distintos, dos fases distintas. El bloque ZZ entrelaza vecinos, así el estado de un qubit depende del otro. Sin ese cruce, las tres variables no se combinan y el circuito las miraría por separado. Sería como tres reglas sueltas, no un parecido entre flujos.

El entrelazado de este mapa es lineal, no completo. Lineal une solo q0 con q1, y q1 con q2. El circuito queda corto y se puede leer de punta a punta, que es lo que acabamos de hacer.

El completo une todos los pares. Además de los vecinos, cruza q0 con q2. En el dibujo de abajo ese cruce está en dorado, y es el único que el lineal no tiene. Dice casi lo mismo, con más compuertas. Se elige el lineal porque alcanza para que el parecido dependa de más de una variable, y porque en 40 minutos se puede seguir con el ojo.

En el código es `ZZFeatureMap` con `feature_dimension=3`, `reps=1` y `entanglement="linear"`. `reps=1` quiere decir que el bloque se escribe una sola vez. Más repeticiones alargan el mapa, no cambian la idea.

---

## 11 · Código · 2 min

**El CSV ya es el recorte**


A partir de acá el relato es el del repositorio. Son pocas líneas, y cada una corresponde a algo que ya dijimos.

El CSV ya es el recorte. No hay que filtrar el dataset entero. `Label` es la clase, el texto BENIGN o DDoS. `y` vale 1 si el flujo es DDoS y 0 si es BENIGN. Los modelos quieren un número, no una palabra. `x` se queda con las columnas numéricas: se tira `Label` porque la etiqueta no puede entrar como variable. Si entrara, el modelo haría trampa: estaría mirando la respuesta.

En esta diapo todavía no hay circuito. Hay una tabla y dos vectores: las variables y la clase.

---

## 12 · Código · 2 min

**Tres variables, tres qubits**

`StandardScaler` pone cada columna en la misma escala. Si una columna es una duración de millones de microsegundos y otra es un conteo de 0 o 1, sin esto la grande se come a la chica. La escala se aprende con el entrenamiento y se aplica igual al resto. No se vuelve a calcular con los datos de prueba, porque eso sería espiar el examen.

`PCA` deja tres coordenadas. Esas tres son las que entran al circuito.

`ZZFeatureMap` es el circuito de la diapositiva 9. El 3 de `feature_dimension` no es un parámetro suelto: es la cantidad de variables, una por qubit. `reps=1` es una sola pasada. `entanglement="linear"` es el cruce solo entre vecinos.

---

## 13 · Código · 2 min

**K es una probabilidad**

La fidelidad es el solapamiento entre los dos estados. En este circuito, ese solapamiento es la probabilidad de medir 000 después de cargar un flujo y deshacer el otro. Por eso K es una probabilidad, no una distancia en kilómetros de paquetes.

`ComputeUncompute` es justo ese procedimiento: aplicar U y después U daga. `StatevectorSampler` es un simulador ideal. Calcula el estado exacto. No hay ruido de un aparato, ni cola de un procesador real. Sirve para ver la cuenta limpia.

`K[i, j]` compara el flujo i con el j. La diagonal, un flujo contra sí mismo, tiene que quedar cerca de 1. Acá todavía no se elige la clase. Solo se llena la matriz.
En el repositorio el kernel no se calcula sobre las 240 filas. Cada par es un circuito, y la cantidad de pares crece con el cuadrado. Por eso `N_TRAIN` es 24 y `N_TEST` es 8. Es a propósito, para que se pueda correr. No es el tamaño del resultado que vamos a citar en la diapositiva 15.

---

## 14 · Código · 2 min

**La SVM solo lee la matriz**

`precomputed` quiere decir que la matriz ya está calculada. La SVM no arma otro circuito y no vuelve a pedir el kernel. Recibe números y ajusta los pesos.

Un flujo nuevo no se clasifica solo. Primero se compara contra cada flujo del entrenamiento: esa es la fila `k_new`. Esa fila entra a `predict`, y ahí sale la clase, 0 o 1, BENIGN o DDoS.

En el mismo lugar donde está este kernel se puede poner el RBF de la diapositiva 7. Misma SVM, misma cohorte chica, otra forma de medir el parecido. Eso muestra que el circuito ocupa un lugar que ya existía. No es un clasificador nuevo al lado del viejo.

---

## 15 · Cierre · 3 min

**Qué se puede concluir**

El Random Forest es un modelo clásico. Muchos árboles de decisión votan una clase. Cada árbol mira el flujo y vota. La mayoría gana. Ese modelo ve el flujo completo, no solo las tres componentes que entran al circuito. Por eso no es el mismo partido: el clásico tiene más información de entrada.

El número de la barra es el F1. El F1 junta en un solo número dos cosas. La precisión: de lo que marqué como ataque, cuánto lo era de verdad. Y la sensibilidad: de los ataques que había, cuántos encontré. Vale 1 cuando se detectan los ataques y, además, lo marcado como ataque realmente lo es. Vale 0 cuando esa cuenta se desarma.

Sobre estos datos de CICIDS2017, el Random Forest llega a un F1 de 0,9997. Casi no se equivoca. La QSVM simulada llega a 0,8571. Detecta los ataques, y la precisión baja a 0,75: de cada cuatro flujos que marca como DDoS, uno no lo era.

La frase para cerrar es esta. Un kernel cuántico sí entra en esta tarea. Se puede usar. Con estos datos y este circuito, no reemplaza al modelo clásico.

---

## 16 · Cierre · 1 min

**Gracias por escuchar**

Si se llevan una sola frase: el circuito no clasifica. Mide si dos flujos se parecen. La SVM pone la clase. Y en estos datos, ese kernel se puede usar, pero no reemplaza al modelo clásico.

Quedo para las preguntas.

---

## Para no mezclar

- Dos clases nada más: BENIGN, tráfico legítimo, y DDoS, denegación de servicio distribuida.
- Un flujo es el resumen de una conexión, no un paquete suelto.
- CICIDS2017, Canadian Institute for Cybersecurity. El recorte es el viernes a la tarde: 240 filas, 120 y 120, 78 columnas, semilla 7.
- Tres qubits porque entra una variable por qubit, no porque tres sea el óptimo.
- El circuito es un mapa de atributos: H, después RZ, después CNOT–ZZ–CNOT solo entre vecinos. No hay cruce directo q0–q2.
- K es la probabilidad de medir 000. Cerca de 1, se parecen. Cerca de 0, no.
- La SVM con `kernel="precomputed"` pone la clase. El RBF ocupa ese mismo lugar cuando la cuenta es clásica.
- Random Forest, F1 0,9997. QSVM simulada, F1 0,8571, con precisión 0,75.
- Frase de cierre: se puede usar un kernel cuántico en esta tarea, y no reemplaza al modelo clásico en estos datos.
- Repositorio: github.com/ticiAngelucci/qiskit-fall-fest. Mail: titiangelucci08@gmail.com.

**Lo que esta charla no es.** No es una captura en vivo. No es una corrida en hardware. No hay dos clasificadores. El circuito no elige BENIGN o DDoS. El laboratorio del repositorio usa 24 flujos de entrenamiento y 8 de prueba para que el kernel termine: esos aciertos no son el F1 de la diapositiva 15.
