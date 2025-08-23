estados=["HIDRATADA", "SECA"]
estado_actual="SECA"
estado_meta="HIDRATADA"
def acciones(estado):
    return ["AGUA", "SOL"]
def cambiar_estado(estado, accion):
    if accion == "AGUA":
        return "HIDRATADA"
    elif accion== "SOL":
        return "SECA"

print(f"Estado Inicial:{estado_actual}")
accion= "AGUA"
estado_actual =cambiar_estado(estado_actual, accion)
print (f"despues de {accion}:{estado_actual}")

if estado_actual==estado_meta:
    print("PLANTA FELIZ :D")