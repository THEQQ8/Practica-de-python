import datetime
def saludar():
    print("Hola, Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
resultado = calcular_area_triangulo(10, 5)
print(f"El área del triángulo es: {resultado}")

def saludar_persona(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")
saludar_persona("Raul", 19)

print("SIN PARAMATROS")

def dar_bienvenida():
    print("bienvenido a python")
dar_bienvenida()

def obtener_anio_actual():
    anio = datetime.datetime.now().year
    print(f"Estamos en el año: {anio}")
obtener_anio_actual()

print("CON PARAMATROS")

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area
resultado = calcular_area_rectangulo(8, 5)
print(f"El área del rectángulo es: {resultado}")

def calcular_promedio(calificacion1, calificacion2, calificacion3):
    promedio = (calificacion1 + calificacion2 + calificacion3) / 3
    return promedio
resultado = calcular_promedio(8, 9, 10)
print(f"El promedio es: {resultado}")
