from Laberinto import Laberinto

class AnalizadorLaberinto:
    def _init_(self, laberinto):
        self.laberinto = laberinto
    
    def mostrar_informacion_completa(self):
        """Muestra información completa del sistema"""
        print("\n" + "="*60)
        print("INFORMACIÓN COMPLETA DEL SISTEMA")
        print("="*60)

        print("\nACCIONES DISPONIBLES:")
        for accion, movimiento in self.laberinto.acciones.items():
            print(f"  {accion}: {movimiento}")

        print("\nRECOMPENSAS:")
        for tipo, valor in self.laberinto.recompensas.items():
            print(f"  {tipo}: {valor}")

        print("\nTABLA DE TRANSICIONES (partial):")
        for estado, transiciones in list(self.laberinto.transiciones.items())[:3]:
            print(f"  {estado}: {transiciones}")
    
    def analizar_caminos(self):
        """Analiza y muestra todos los caminos posibles"""
        caminos = self.laberinto.encontrar_todos_caminos()
        print(f"\nSe encontraron {len(caminos)} caminos posibles:")
        
        for i, camino_info in enumerate(caminos[:3]):  # Mostrar solo los 3 más cortos
            print(f"\nCamino {i+1}:")
            print(f"  Longitud: {camino_info['longitud']} pasos")
            print(f"  Recompensa: {camino_info['recompensa']}")
            print(f"  Ruta: {' → '.join(map(str, camino_info['camino']))}")
        
        return caminos