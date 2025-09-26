
from calificaciones import*
from calificaciones_ui import*


if __name__=="__main__":
    # print(f"{nota_teoria(9,0)}")
    # print(f"La nota del cuatrimestre es: {nota_cuatrimestre(7, 5,4)}")
    datos = solicita_notas()
    mostrar_notas(datos)


