
def resolve(input):
    input += "\nFIN"
    list_input = input.split("\n")
    index_input = 0
    output = "\n"
    exit = False
    while not exit:
        categoria = list_input[index_input]
        index_input += 1
        if categoria == "FIN":
            exit = True
        else:
            reset = False
            equipos = {}
            partidos_jugados = 0
            ganador = ""
            ganador_puntos = 0
            while not reset:
                teclado = list_input[index_input]
                index_input += 1
                if teclado == "FIN":
                    reset = True
                else:
                    equipo1, puntaje1, equipo2, puntaje2 = teclado.split()
                    puntaje1 = int(puntaje1)
                    puntaje2 = int(puntaje2)
                    if not (equipo1 in equipos):
                        equipos[equipo1] = 0
                    if not (equipo2 in equipos):
                        equipos[equipo2] = 0
                    if puntaje1 > puntaje2:
                        equipos[equipo1] = equipos[equipo1] + 2
                        if equipos[equipo1] > ganador_puntos:
                            ganador_puntos = equipos[equipo1]
                            ganador = equipo1
                        equipos[equipo2] = equipos[equipo2] + 1
                        if equipos[equipo2] > ganador_puntos:
                            ganador_puntos = equipos[equipo2]
                            ganador = equipo2
                    else:
                        equipos[equipo1] = equipos[equipo1] + 1
                        if equipos[equipo1] > ganador_puntos:
                            ganador_puntos = equipos[equipo1]
                            ganador = equipo1
                        equipos[equipo2] = equipos[equipo2] + 2
                        if equipos[equipo2] > ganador_puntos:
                            ganador_puntos = equipos[equipo2]
                            ganador = equipo2
                    partidos_jugados += 1
            partidos_total = len(equipos)
            partidos_total = (partidos_total - 1) * partidos_total
            partidos_no_jugados = partidos_total - partidos_jugados
            del equipos[ganador]
            for entry in equipos:
                if ganador_puntos == equipos[entry]:
                    ganador = "EMPATE"
                    break
            output += "%s %s\n" % (ganador, partidos_no_jugados)
    return output


