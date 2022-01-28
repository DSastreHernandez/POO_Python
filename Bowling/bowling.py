from tabla import Tabla

class Bowling:

    ## Globals ##
    STRIKE = 'X'
    SPARE = '/'
    NO_PINS_BOWLED = '-'

    def __init__(self,tabla=""):
        self.puntuacion = 0
        self.tabla = Tabla(tabla).get_tabla()
        self.set_puntuacion()
            
    def set_puntuacion(self):
        num_turno = 0
        while num_turno + 1 <= len(self.tabla):
            puntos_turno = 0

            for tirada in self.tabla[num_turno]:
            
                if isinstance(tirada, int):
                    puntos_turno += tirada
            
                elif tirada == self.STRIKE:
                    puntos_turno += self.__strike(num_turno)
            
                elif tirada == self.SPARE:
                    puntos_turno += self.__spare(num_turno) + (10 - self.__puntos_netos_tiro(tiro_anterior))
                
                tiro_anterior = tirada

            self.puntuacion += puntos_turno
            num_turno += 1

    def __spare(self,num_turno):
        try:
            return self.__puntos_netos_tiro(self.tabla[num_turno + 1][0])
        except:
            return 0  

    def __strike(self,num_turno):
        try:
            if len(self.tabla[num_turno + 1]) >= 2:
                return  10 +  self.__puntos_netos_turno(self.tabla[num_turno + 1][:2])
            else:
                return 10 + self.__puntos_netos_turno(self.tabla[num_turno + 1]) + self.__puntos_netos_tiro(self.tabla[num_turno + 2][0])
        except:
            return 10


        
    def __puntos_netos_turno(self,turno):
        if turno[0] == self.STRIKE:
            return 10 * turno.count(self.STRIKE)
        elif turno[-1] == self.SPARE:
            return 10
        else:
            return sum(filter(lambda tiro: isinstance(tiro, int),turno))

    def __puntos_netos_tiro(self,tiro):
        if tiro == self.STRIKE:
            return 10
        elif tiro == self.NO_PINS_BOWLED:
            return 0
        else:
            return tiro




    def get_puntuacion(self):
        return self.puntuacion 

                


if __name__ == '__main__':

    bowling = Bowling("11111111111111111111")
    assert  20 ==  bowling.get_puntuacion()
    
    bowling = Bowling("9-9-9-9-9-9-9-9-9-9-")
    assert 90 == bowling.get_puntuacion()

    bowling = Bowling("5/5/5/5/5/5/5/5/5/5/5")
    assert 150 == bowling.get_puntuacion()

    bowling = Bowling("9-3/613/815/-/8-7/8/8")
    assert 131 == bowling.get_puntuacion()

    bowling = Bowling('X9-9-9-9-9-9-9-9-9-')
    assert 100 == bowling.get_puntuacion()

    bowling = Bowling('XX8-44444444444444')
    assert 110 == bowling.get_puntuacion()

    bowling = Bowling('XX9-9-9-9-9-9-9-9-')
    assert 120 == bowling.get_puntuacion()

    bowling = Bowling('XXX9-9-9-9-9-9-9-')
    assert 141 == bowling.get_puntuacion()

    bowling = Bowling('9-9-9-9-9-9-9-9-9-XXX')
    assert 111 == bowling.get_puntuacion()

    bowling = Bowling('XX8-44444444444444')
    assert 110 == bowling.get_puntuacion()

    bowling = Bowling('XXXXXXXXXXXX')
    assert 300 == bowling.get_puntuacion()

    assert 111 == Bowling("9-9-9-9-9-9-9-9-9-XXX").get_puntuacion()

    assert 149 == Bowling("8/549-XX5/53639/9/X").get_puntuacion()

    assert 175 == Bowling("X5/X5/XX5/--5/X5/").get_puntuacion()

    assert 165 == Bowling("-/X9/5/33X33XX9/X").get_puntuacion()