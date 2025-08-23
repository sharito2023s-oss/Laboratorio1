# --- Definición de estados ---
estados = ["0,0", "0,1", "0,2",
           "1,0", "1,1", "1,2",
           "2,0", "2,1", "2,2"]

estado_actual = "0,0"   # El pirata empieza aquí
estado_meta   = "2,2"   # El tesoro está aquí

# --- Acciones posibles ---
def acciones(estado):
    x, y = map(int, estado.split(","))
    posibles = []
    if x > 0: posibles.append("↑")
    if x < 2: posibles.append("↓")
    if y > 0: posibles.append("←")
    if y < 2: posibles.append("→")
    return posibles

# --- Función de transición ---
def cambiar_estado(estado, accion):
    x, y = map(int, estado.split(","))
    if accion == "↑":
        return f"{x-1},{y}"
    elif accion == "↓":
        return f"{x+1},{y}"
    elif accion == "←":
        return f"{x},{y-1}"
    elif accion == "→":
        return f"{x},{y+1}"
    return estado

# --- Simulación (camino elegido a mano) ---
print(f"Estado Inicial: {estado_actual}")
camino = ["→", "→", "↓", "↓"]  # ejemplo de camino válido

for accion in camino:
    estado_actual = cambiar_estado(estado_actual, accion)
    print(f"Después de {accion}: {estado_actual}")

if estado_actual == estado_meta:
    print("¡El barco encontro el destino!")
else:
    print("El barco sigue perdido...")
