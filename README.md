# 🧩 8-Puzzle Solver - BFS Algorithm Implementation

## 📋 Descripción del Proyecto
Este proyecto implementa un **solucionador para el clásico juego 8-Puzzle** utilizando el algoritmo de **Búsqueda en Amplitud (BFS)**.  

El **espacio vacío se representa con el número `0`**.  
El objetivo es transformar un estado inicial del tablero hasta alcanzar un estado meta, moviendo las fichas una posición a la vez (arriba, abajo, izquierda o derecha).

El programa está desarrollado en **Python** y estructurado en tres componentes principales, organizados en ramas separadas de Git y luego fusionados.

---

## 🏗️ Estructura del Proyecto

<img width="671" height="258" alt="Captura estructura Git" src="https://github.com/user-attachments/assets/f49213ae-a2c7-45e0-91fc-ae0061eacfe1" />

---

## 🔷 Ramas de Desarrollo
El proyecto se desarrolló utilizando tres ramas principales:

- **PuzzleState** → Representa el estado del tablero  
- **PuzzleSolver** → Implementa el algoritmo BFS para resolver el puzzle  
- **PuzzleGame** → Proporciona la interfaz y lógica del juego  

---

## 📊 Estructura de Commits


main (rama principal)

├── PuzzleState (rama para representación de estados)

├── PuzzleSolver (rama para algoritmo de solución)

└── PuzzleGame (rama para interfaz de juego)

---

## 🧠 Componentes Principales

### 1. PuzzleState
Clase encargada de representar el estado del tablero.  
**Funcionalidades:**
- Localizar la posición del espacio vacío (`0`)
- Verificar si un estado es igual al estado objetivo
- Generar los posibles movimientos (arriba, abajo, izquierda, derecha)
- Implementar comparación y hashing para evitar estados repetidos

---

### 2. PuzzleSolver
Implementa el algoritmo **BFS (Breadth-First Search)** para explorar los estados posibles hasta encontrar la solución.  
**Características del algoritmo:**
- Evita ciclos mediante un conjunto de estados visitados
- Reconstruye la ruta de movimientos desde el estado inicial hasta el estado meta
- Garantiza la **solución óptima en el menor número de pasos**

---

### 3. PuzzleGame
Controla la ejecución del juego y la impresión de los resultados.  
**Funcionalidades:**
- Ejecutar el algoritmo BFS sobre el tablero
- Mostrar el estado inicial y cada paso de la solución
- Visualizar la secuencia de movimientos hasta llegar al estado objetivo

---

## 🎮 Ejemplo de Ejecución

**Estado inicial:**

![Puzzle 8](https://github.com/Sharito2023s-oss/Puzzle_8/blob/main/Puzzle_8.png?raw=true)

### Prerrequisitos
- Python 3.6 o superior  
- Git (para clonar el repositorio)  

---

## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  
- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)
