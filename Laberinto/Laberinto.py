import numpy as np
from collections import deque
import random

class Laberinto:
    def _init_(self, filas=3, columnas=3, inicio=(0,0), meta=(2,2), obstaculos=None):
        self.filas = filas
        self.columnas = columnas
        self.inicio = inicio
        self.meta = meta
        self.obstaculos = obstaculos if obstaculos else []
        
        # Definir acciones posibles
        self.acciones = {
            "→": (0, 1),   # derecha
            "↓": (1, 0),   # abajo
            "←": (0, -1),  # izquierda
            "↑": (-1, 0)   # arriba
        }
        
        # Inicializar laberinto
        self.laberinto = self.crear_laberinto()
        self.transiciones = self.crear_tabla_transiciones()
        
        # Sistema de recompensas
        self.recompensas = {
            "inicio": 0,
            "meta": 100,
            "normal": -1,
            "obstaculo": -50,
            "fuera_limites": -10
        }
    
    def crear_laberinto(self):
        """Crea la representación del laberinto"""
        laberinto = {}
        for fila in range(self.filas):
            for columna in range(self.columnas):
                estado = (fila, columna)
                if estado == self.inicio:
                    laberinto[estado] = "inicio"
                elif estado == self.meta:
                    laberinto[estado] = "meta"
                elif estado in self.obstaculos:
                    laberinto[estado] = "obstaculo"
                else:
                    laberinto[estado] = "normal"
        return laberinto
    
    def crear_tabla_transiciones(self):
        """Crea la tabla de transiciones para todos los estados"""
        transiciones = {}
        for estado in self.laberinto:
            if self.laberinto[estado] == "obstaculo":
                transiciones[estado] = {}
                continue
                
            transiciones[estado] = {}
            for accion, (df, dc) in self.acciones.items():
                nueva_fila = estado[0] + df
                nueva_columna = estado[1] + dc
                nuevo_estado = (nueva_fila, nueva_columna)
                
                # Verificar límites
                if (0 <= nueva_fila < self.filas and 
                    0 <= nueva_columna < self.columnas and 
                    self.laberinto.get(nuevo_estado, "obstaculo") != "obstaculo"):
                    transiciones[estado][accion] = nuevo_estado
                else:
                    transiciones[estado][accion] = None
        
        return transiciones
    
    def mover(self, estado_actual, accion):
        """Realiza un movimiento y retorna resultado"""
        if estado_actual not in self.transiciones or accion not in self.transiciones[estado_actual]:
            return estado_actual, -2, False  # Acción no válida
        
        nuevo_estado = self.transiciones[estado_actual][accion]
        
        if nuevo_estado is None:
            return estado_actual, self.recompensas["fuera_limites"], False
        
        tipo_estado = self.laberinto[nuevo_estado]
        
        if tipo_estado == "obstaculo":
            return estado_actual, self.recompensas["obstaculo"], False
        
        if tipo_estado == "meta":
            return nuevo_estado, self.recompensas["meta"], True
        
        return nuevo_estado, self.recompensas["normal"], False
    
    def encontrar_todos_caminos(self):
        """Encuentra todos los caminos posibles usando BFS"""
        caminos = []
        cola = deque([(self.inicio, [], 0)])  # (estado, camino, recompensa)
        
        while cola:
            estado_actual, camino_actual, recompensa_actual = cola.popleft()
            
            if estado_actual == self.meta:
                caminos.append({
                    'camino': camino_actual + [estado_actual],
                    'recompensa': recompensa_actual + self.recompensas["meta"],
                    'longitud': len(camino_actual) + 1
                })
                continue
            
            if estado_actual in camino_actual:  # Evitar ciclos
                continue
            
            for accion in self.transiciones[estado_actual]:
                if self.transiciones[estado_actual][accion] is not None:
                    nuevo_estado = self.transiciones[estado_actual][accion]
                    if self.laberinto[nuevo_estado] != "obstaculo":
                        nueva_recompensa = recompensa_actual + self.recompensas["normal"]
                        cola.append((nuevo_estado, camino_actual + [estado_actual], nueva_recompensa))
        
        return sorted(caminos, key=lambda x: x['longitud'])
    
    def mostrar_laberinto(self):
        """Muestra una representación visual del laberinto"""
        print("\n" + "="*50)
        print("REPRESENTACIÓN DEL LABERINTO")
        print("="*50)
        
        for fila in range(self.filas):
            fila_str = ""
            for columna in range(self.columnas):
                estado = (fila, columna)
                if estado == self.inicio:
                    fila_str += "S "  # Start
                elif estado == self.meta:
                    fila_str += "G "  # Goal
                elif estado in self.obstaculos:
                    fila_str += "X "  # Obstacle
                else:
                    fila_str += ". "  # Normal
            print(fila_str)
        print("Leyenda: S=Inicio, G=Meta, X=Obstáculo, .=Normal")
        print("="*50)
    
    def probar_movimientos_aleatorios(self, num_movimientos=10):
        """Prueba movimientos aleatorios desde el inicio"""
        print(f"\nProbando {num_movimientos} movimientos aleatorios:")
        print("-" * 40)
        
        estado_actual = self.inicio
        total_recompensa = 0
        
        for i in range(num_movimientos):
            acciones_posibles = list(self.transiciones[estado_actual].keys())
            if not acciones_posibles:
                break
                
            accion = random.choice(acciones_posibles)
            nuevo_estado, recompensa, terminado = self.mover(estado_actual, accion)
            
            print(f"Mov {i+1}: {estado_actual} + {accion} -> {nuevo_estado} "
                  f"(Recompensa: {recompensa})")
            
            total_recompensa += recompensa
            estado_actual = nuevo_estado
            
            if terminado:
                print("¡Llegó a la meta!")
                break
        
        print(f"Recompensa total: {total_recompensa}")