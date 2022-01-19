class Tabla:    
    
    def __init__(self,puntos = ""):
        self.tabla_ordenada = []
        self.puntos = puntos

    def ordenar_tabla(self):
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
        Tabla.ordenar_tabla(self)
        return self.tabla_ordenada