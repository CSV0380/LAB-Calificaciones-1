""" APARTADO E """
from calificaciones import*

def leer_nota(mensaje):
        valor = input(mensaje)
        return None if valor.strip() == "-" else float(valor)


def solicita_notas():
    nombre = input("Introduzca su nombre: ")
    teoricos = [
        leer_nota("Introduzca la nota del examen teórico 1 (- si no se ha presentado): "),
        leer_nota("Introduzca la nota del examen teórico 2 (- si no se ha presentado): "),
        leer_nota("Introduzca la nota del examen teórico 3 (- si no se ha presentado): "),
        leer_nota("Introduzca la nota del examen teórico 4 (- si no se ha presentado): ")]

    practicos = [
        leer_nota("Introduzca la nota del examen práctico 1 (- si no se ha presentado): "),
        leer_nota("Introduzca la nota del examen práctico 2 (- si no se ha presentado): ")]

    return (nombre, teoricos, practicos)


def mostrar_notas(datos):
    nombre, teoricos, practicos = datos

    print(f"Nombre del estudiante: {nombre}")
    print("Notas teóricas:", teoricos)
    print("Notas prácticas:", practicos)
