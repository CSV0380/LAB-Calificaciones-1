""" APARTADO A """

def nota_teoria(teorico1, teorico2):
    
    nota1 = nota_cero(teorico1)
    nota2 = nota_cero(teorico2)
    media = (nota1 + nota2) / 2

    return media


def nota_cero(nota):
    res = nota
    if res == None:
        res = 0
    return res


""" APARTADO B """

def nota_cuatrimestre(teorico1, teorico2, practico):
    media_teoricos = nota_teoria(teorico1, teorico2)
    p = nota_cero(practico)

    if media_teoricos < 4:
        nota_final = 0
    else:
        nota_final = (0.15 * nota_cero(teorico1)) + (0.15 * nota_cero(teorico2)) + (0.7 * p)
    
    return nota_final



""" APARTADO C """

def nota_continua(nota_teoria1, nota_teoria2, nota_practico1,nota_teoria3, nota_teoria4, nota_practico2):
    nota_cuatrimestre1 = nota_cuatrimestre(nota_teoria1, nota_teoria2, nota_practico1)
    nota_cuatrimestre2 = nota_cuatrimestre(nota_teoria3, nota_teoria4, nota_practico2)

    media = (nota_cuatrimestre1 + nota_cuatrimestre2) / 2

    if nota_cuatrimestre1 >= 5 and nota_cuatrimestre2 >= 5:
        nota_final = media
    else:
        nota_final = min(4, media)

    return nota_final


""" APARTADO D """

def genera_mensaje(nota_cuatrimestre1, nota_cuatrimestre2, nota_final):
    if nota_final >= 5:
        return "¡Enhorabuena! Has aprobado la asignatura."
    elif nota_cuatrimestre1 < 5 and nota_cuatrimestre2 >= 5:
        return "Debes recuperar el primer cuatrimestre."
    elif nota_cuatrimestre2 < 5 and nota_cuatrimestre1 >= 5:
        return "Debes recuperar el segundo cuatrimestre."
    elif nota_cuatrimestre1 < 5 and nota_cuatrimestre2 < 5:
        return "Debes recuperar toda la asignatura."




