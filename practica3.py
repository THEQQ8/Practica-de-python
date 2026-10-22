from collections import deque
import time

cola = deque()

cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")

atendido = cola.popleft()

print("Atendido:", atendido)
print("Cola restante:", cola)
print("-" * 30)  # Separador visual


cola_reproduccion = deque()

cola_reproduccion.append("1- Solare")
cola_reproduccion.append("2- Arcoloria")
cola_reproduccion.append("3- Merteora")

print("Canciones en espera:")
for cancion in cola_reproduccion:
    print(" _", cancion)

print("\nIniciando reproducción...\n")

while cola_reproduccion:
    cancion_actual = cola_reproduccion.popleft()
    print(f"Sonando ahora: {cancion_actual}")
    time.sleep(1)  # Simula la duración de la canción
    print(f"Finaliza: {cancion_actual}\n")

print(f"Quedan {len(cola_reproduccion)} canciones en la cola.")
print("LA COLA DE REPRODUCCIÓN HA FINALIZADO")