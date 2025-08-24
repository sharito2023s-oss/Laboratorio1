# ⚓🌊 Barco Pirata & 🌱 Planta - Simulaciones en Python

## 📋 Descripción del Proyecto
Este repositorio contiene dos simulaciones educativas en **Python** diseñadas para ilustrar conceptos de **sistemas de estados finitos** y **transiciones entre estados**:

1. **Barco Pirata** → Navegación en una cuadrícula 3x3 hasta encontrar un tesoro.  
2. **Planta** → Este proyecto simula el estado de una planta que puede cambiar entre diferentes condiciones basadas en las acciones aplicadas. La planta comienza en estado "SECA" y mediante la aplicación de "AGUA" puede transformarse a estado "HIDRATADA", culminando en un estado final de "PLANTA FELIZ".

Ambos programas son simples, didácticos y fáciles de ejecutar.  

---

## 🏴‍☠️ Barco Pirata - Simulación de Navegación

### 📝 Descripción
El **barco pirata** navega en una **cuadrícula 3x3** partiendo de la posición **(0,0)** (esquina superior izquierda) con el objetivo de llegar al **tesoro en (2,2)** (esquina inferior derecha) mediante movimientos estratégicos.

---

### 🗺️ Sistema de Cuadrícula
- **Matriz 3x3** → Espacio de navegación limitado  
- **Coordenadas (x,y)** → Sistema de posiciones  
- **Estado inicial** → (0,0)  
- **Estado meta** → (2,2)  

---

### Estado Inicial: 0,0

Después de →: 0,1

Después de →: 0,2

Después de ↓: 1,2

Después de ↓: 2,2

¡El barco encontró el destino!

### 📷 Visualización


![Algoritmo Concepto Espacio](https://github.com/Sharito2023s-oss/Laboratorio1/blob/main/Algoritmo-Concepto-Espacio/barco.png?raw=true)

---

# 🌱 Simulación: Planta

La planta cambia de estado según la acción aplicada:

- Estado inicial: SECA

- Acción: AGUA

- Estado final: HIDRATADA → 🌱 PLANTA FELIZ :D


## 🎯 Estados de la Planta

- SECA: Estado inicial de la planta
- HIDRATADA: Estado después de recibir agua
- PLANTA FELIZ: Estado final alcanzado

## 🚀 Ejecución del Programa

#### Resultado de la simulación:

Estado Inicial: SECA

despues de AGUA: HIDRATADA

PLANTA FELIZ :D

## 📦 Estructura del Código

El programa sigue una secuencia lineal de transiciones:

1. Inicialización en estado "SECA"

2. Aplicación de acción "AGUA"

3. Transición a estado "HIDRATADA"

4. Finalización en estado "PLANTA FELIZ"

### 📷 Visualización


![Algoritmo Concepto Espacio](https://github.com/Sharito2023s-oss/Laboratorio1/blob/main/Algoritmo-Concepto-Espacio/Planta.png?raw=true)


## 👥 Autores

- Carlos Andrés Suárez Torres - Carlos23Andres

- Saira Sharid Sanabria Muñoz - sharito202
