import datetime

def mostrar_encabezado_escuela():
    print("-----------------------------------------------")
    print("Universidad Tecnológica de Xicotepec de Juárez")
    print("-----------------------------------------------")

def obtener_nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    else:  # De 9.5 a 10.0
        return "Excelente"

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    mostrar_encabezado_escuela()
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    necesita_extra = "Sí" if nota_final < nota_minima else "No"

    # Los prints dentro de la función (con sangría)
    print(f"Nombre del Alumno:              {nombre_alumno}")
    print(f"Nota exámenes 70%:              {nota_examenes}")
    print(f"Nota tareas 30%:                {nota_tareas}")
    print("----------------------------------------------------------------------")
    print(f"Calificación final ponderada:   {nota_final}")
    print(f"Estado académico:               {estado}")
    print(f"Requiere examen extraordinario: {necesita_extra}")

if __name__ == "__main__":
    generar_boleta("Carlos Gómez", 9.8, 9.5)