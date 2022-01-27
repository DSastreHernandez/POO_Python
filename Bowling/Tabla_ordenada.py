class Tabla():   

    def __init__(self,puntos = ""):
        self.tabla = []
        self.puntos = puntos
        self.tabla_limpia = []

    def set_tabla(self):
        puntos = self.tabla_limpia
        tabla_turno = []
        tiros = 0
        while len(self.tabla) < 9:
            if len(tabla_turno) == 2:
                self.tabla.append(tabla_turno)
                tabla_turno = [puntos[tiros]]
            else:
                tabla_turno.append(puntos[tiros])
            tiros += 1
        
        self.tabla.append(puntos[tiros - 1:])

    def get_tabla(self):
        return self.tabla

    def set_tabla_limpia(self):
        for element in self.puntos:
            try:
                if int(element):
                    self.tabla_limpia.append(int(element))
            except:
                self.tabla_limpia.append(element)

if __name__ == '__main__':

    tabla = Tabla("9-9-9-9-9-9-9-9-9-9-")
    tabla.set_tabla_limpia()
    tabla.set_tabla()
    assert tabla.get_tabla() == [[9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-'], [9,'-']] 

    tabla = Tabla("5/5/5/5/5/5/5/5/5/5/5")  
    tabla.set_tabla_limpia()
    tabla.set_tabla()
    assert tabla.get_tabla() == [[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/',5]]