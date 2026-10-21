pila = []
print("Pila inicializada:", pila)
print("-" * 50)

for i in range(1, 11):
    pila.append(f"Plato {i}")

print("Pila después de apilar 10 elementos:")
print(pila)
print("-" * 50)

cima = pila[-1]
print(f"El elemento en la cima top es: {cima}")
print("-" * 50)

print("Desapilando 4 elementos lifo")
for _ in range(4):
    element_eliminado = pila.pop()
    print(f"Se retiró: {element_eliminado}")

print("(Estado actual de la pila):", pila)
print("-" * 50)

tamano = len(pila)
esta_vacia = len(pila) == 0
print(f"Tamaño de la pila sise: {tamano}")
print(f"¿La pila está vacía? empty: {esta_vacia}")
print("-" * 50)

while len(pila) > 0:
    retirado = pila.pop()
    print(f"Vaciando: {retirado}")

print("\nEstado final de la pila:", pila)