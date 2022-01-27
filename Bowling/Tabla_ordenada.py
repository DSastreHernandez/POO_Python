class Tabla:    
    
    def __init__(self,puntos = ""):
        self.tabla_ordenada = []
        self.puntos = puntos

    def set_tabla_ordenada(self):
        puntos = self.puntos
        tabla_ordenada = []
        tabla_turno = []
        for element in puntos:
            if len(tabla_turno) < 2:
                turno = element
                tabla_turno.append(turno)
            else:
                tabla_ordenada.append(tabla_turno)
                tabla_turno = [element]
        if len(tabla_turno) == 1:
            tabla_ordenada[-1] += tabla_turno
        elif len(tabla_turno) == 2:
            tabla_ordenada.append(tabla_turno)
        self.tabla_ordenada = tabla_ordenada

    def get_tabla_ordenada(self):
        return self.tabla_ordenada

if __name__ == '__main__':

    Tabla("9-9-9-9-9-9-9-9-9-9-")
    Tabla.set_tabla_ordenada()
    assert Tabla.get_tabla_ordenada() == [[9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-']] 