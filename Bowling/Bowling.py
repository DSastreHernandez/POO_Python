class Bowling:

    def __init__(self,puntos=""):
        self.tabla_ordenada = []
        self.puntuacion = 0
        self.puntos = puntos

    def ordenar_tabla(self):
        Bowling.sanear_putnos(self)
        puntos = self.puntos
        tabla_ordenada = []
        tabla_turno = []
        for element in puntos:
            if len(tabla_turno) < 2:
                tabla_turno.append(element)
            else:
                tabla_ordenada.append(tabla_turno)
                tabla_turno = [element]
        if len(tabla_turno) == 1:
            tabla_ordenada[-1] += tabla_turno
        elif len(tabla_turno) == 2:
            tabla_ordenada.append(tabla_turno)
        self.tabla_ordenada = tabla_ordenada


            

    def get_tabla_ordenada(self):
        Bowling.ordenar_tabla(self)
        return self.tabla_ordenada

    def sanear_putnos(self):
        puntos = self.puntos
        puntos_saneados = []
        for element in puntos:
            try:
                puntos_saneados.append(int(element))
            except:
                puntos_saneados.append(element)
        self.puntos = puntos_saneados
                


if __name__ == '__main__':

    bowling = Bowling('11111111111111111111')
    assert [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]] == bowling.get_tabla_ordenada()

    bowling = Bowling('1/111111111111111111')
    