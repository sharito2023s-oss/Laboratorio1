# 🧭 Laberinto Solver - BFS Pathfinding Implementation

## 📋 Descripción del Proyecto
Este proyecto implementa un solucionador de laberintos utilizando el algoritmo de Búsqueda en Amplitud (BFS) para encontrar todos los caminos posibles desde un punto de inicio hasta una meta, evitando obstáculos.

El sistema incluye un modelo de recompensas que penaliza movimientos no óptimos y premia llegar a la meta, simulando un entorno de aprendizaje por refuerzo.

---

## 🎯 Características Principales

#### 🔍 Búsqueda Completa de Caminos

- Algoritmo BFS para encontrar todos los caminos posibles

- Detección de ciclos para evitar caminos infinitos

- Ordenamiento por longitud de caminos

- Cálculo de recompensas acumuladas

---

## 🎮 Sistema de Recompensas

self.recompensas = {

    "inicio": 0,
    "meta": 100,
    "normal": -1,
    "obstaculo": -50,
    "fuera_limites": -10
}
---

## 🧭 Movimientos Permitidos

- → Derecha (0, 1)

- ↓ Abajo (1, 0)

- ← Izquierda (0, -1)

- ↑ Arriba (-1, 0)

## 🏗️ Estructura del Proyecto

### Clases Principales

#### 1. Laberinto

Clase principal que representa el entorno del laberinto.

##### Funcionalidades:

- Creación de laberintos personalizados

- Sistema de transiciones entre estados

- Ejecución de movimientos y cálculo de recompensas

- Búsqueda de todos los caminos posibles

#### 2. AnalizadorLaberinto

Clase auxiliar para análisis y visualización.

##### Funcionalidades:

- Mostrar información completa del sistema

- Analizar y mostrar caminos encontrados

- Visualización de transiciones posibles

---

## 🖼️ Ejemplos de Ejecución

#### 1. Laberinto Sin Obstáculos


REPRESENTACIÓN DEL LABERINTO

==================================================

S  .  . 

.  .  .

.  .  G 

Leyenda: S = Inicio, G = Meta, X = Obstáculo, . = Normal

==================================================

Se encontraron 12 caminos posibles:

Camino 1:
  Longitud: 5 pasos
  Recompensa: 96
  Ruta: (0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2)

#### 2. Laberinto Con Obstáculos

REPRESENTACIÓN DEL LABERINTO

==================================================

S X .

. X .

X . G 

Leyenda: S = Inicio, G = Meta, X = Obstáculo, . = Normal

==================================================

Se encontraron 0 caminos posibles:

#### 3. Movimientos Aleatorios

Probando 15 movimientos aleatorios:

----------------------------------------

Mov 1: (0, 0) + ↓ -> (0, 0) (Recompensa: -10)

Mov 2: (0, 0) + ↑ -> (0, 0) (Recompensa: -10)

...

Recompensa total: -123

## 📊 Resultados Esperados

El programa proporciona:

1. Visualización del laberinto en formato grid

2. Lista de todos los caminos posibles ordenados por longitud

3. Recompensa acumulada para cada camino

4. Simulación de movimientos aleatorios con recompensas en tiempo real

5. Tabla de transiciones completa para cada estado

## 🧠 Aplicaciones

Este sistema puede ser utilizado como:

- Base para algoritmos de planificación de rutas

- Entorno de prueba para algoritmos de reinforcement learning

- Herramienta educativa para enseñar BFS y teoría de grafos

- Simulador para sistemas de navegación autónoma

## 👥 Autores

- Carlos Andrés Suárez Torres - Carlos23Andres

- Saira Sharid Sanabria Muñoz - sharito202
