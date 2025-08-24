from Laberinto import Laberinto
from AnalizadorLaberinto import AnalizadorLaberinto

class EjemplosLaberinto:
    @staticmethod
    def ejemplo_sin_obstaculos():
        """Ejemplo de laberinto sin obstáculos"""
        print("\n1. LABERINTO SIN OBSTÁCULOS")
        laberinto = Laberinto()
        analizador = AnalizadorLaberinto(laberinto)
        
        laberinto.mostrar_laberinto()
        analizador.analizar_caminos()
        
        return laberinto, analizador
    
    @staticmethod
    def ejemplo_con_obstaculos():
        """Ejemplo de laberinto con obstáculos"""
        print("\n2. LABERINTO CON OBSTÁCULOS")
        laberinto = Laberinto(obstaculos=[(0,1), (1,1), (2,0)])
        analizador = AnalizadorLaberinto(laberinto)
        
        laberinto.mostrar_laberinto()
        caminos = analizador.analizar_caminos()
        
        return laberinto, analizador, caminos
    
    @staticmethod
    def ejemplo_movimientos_individuales():
        """Ejemplo de movimientos individuales"""
        print("\n3. PRUEBAS DE MOVIMIENTOS INDIVIDUALES")
        print("-" * 40)

        laberinto = Laberinto(obstaculos=[(1,1)])
        estado = (0,0)
        print(f"Estado inicial: {estado}")

        acciones = ["→", "↓", "→", "↓"]
        for accion in acciones:
            nuevo_estado, recompensa, terminado = laberinto.mover(estado, accion)
            print(f"{estado} + {accion} -> {nuevo_estado} (Recompensa: {recompensa}, Terminado: {terminado})")
            estado = nuevo_estado
            if terminado:
                break
        
        return laberinto
    
    @staticmethod
    def ejemplo_movimientos_aleatorios():
        """Ejemplo de movimientos aleatorios"""
        print("\n4. SIMULACIÓN CON MOVIMIENTOS ALEATORIOS")
        laberinto = Laberinto(obstaculos=[(1,0), (1,2)])
        laberinto.mostrar_laberinto()
        laberinto.probar_movimientos_aleatorios(15)
        
        return laberinto


def demostracion_completa():
    """Función de demostración completa del sistema"""
    print("🎯 LABERINTO 3x3 - IMPLEMENTACIÓN COMPLETA")
    print("="*60)
    
    # Ejemplo 1: Sin obstáculos
    laberinto1, analizador1 = EjemplosLaberinto.ejemplo_sin_obstaculos()
    
    # Ejemplo 2: Con obstáculos
    laberinto2, analizador2, caminos = EjemplosLaberinto.ejemplo_con_obstaculos()
    
    # Ejemplo 3: Movimientos individuales
    laberinto3 = EjemplosLaberinto.ejemplo_movimientos_individuales()
    
    # Ejemplo 4: Movimientos aleatorios
    laberinto4 = EjemplosLaberinto.ejemplo_movimientos_aleatorios()
    
    # Mostrar información completa del sistema
    analizador1.mostrar_informacion_completa()
    
    print("\n" + "="*60)
    print("🎯 IMPLEMENTACIÓN COMPLETA - LISTA PARA ENTREGAR")
    print("="*60)
    
    return {
        "laberinto_sin_obstaculos": laberinto1,
        "laberinto_con_obstaculos": laberinto2,
        "laberinto_movimientos": laberinto3,
        "laberinto_aleatorio": laberinto4
    }

# Si se ejecuta este archivo directamente, mostrar la demostración
if __name__ == "_main_":
    demostracion_completa()



# Crear un laberinto personalizado
mi_laberinto = Laberinto(
    filas=4, 
    columnas=4, 
    inicio=(0,0), 
    meta=(3,3), 
    obstaculos=[(1,1), (2,2)]
)

# Analizarlo
analizador = AnalizadorLaberinto(mi_laberinto)
mi_laberinto.mostrar_laberinto()
caminos = analizador.analizar_caminos()

# Probar movimientos
mi_laberinto.probar_movimientos_aleatorios(10)