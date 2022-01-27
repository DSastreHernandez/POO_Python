class Bowling:

    ## Globals ##
    STRIKE = 'X'
    SPARE = '/'
    NO_PINS_BOWLED = '-'

    def __init__(self,tabla=[]):
        self.puntuacion = 0
        self.tabla = tabla
            
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
                    puntos_turno = self.__spare(num_turno)

            self.puntuacion += puntos_turno
            num_turno += 1

    def __spare(self,num_turno):
        try:
            return 10 + self.tabla[num_turno + 1][0]
        except:
            return 10  

    def __strike(self,num_turno):
        try:
            if len(self.tabla[num_turno + 1]) >= 2:
                return  10 +  self.__puntos_netos_turno(self.tabla[num_turno + 1])
            else:
                return 10 + self.__puntos_netos_turno(self.tabla[num_turno + 1]) + self.__puntos_netos_tiro(self.tabla[num_turno + 2][0])
        except:
            return 10


        
    def __puntos_netos_turno(self,turno):
        if turno[0] == self.STRIKE:
            return 10
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

    bowling = Bowling([[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])
    bowling.set_puntuacion()
    assert  20 ==  bowling.get_puntuacion()
    
    bowling = Bowling([[9,0],[9,0],[9,0],[9,0],[9,0],[9,0],[9,0],[9,0],[9,0],[9,0]])
    bowling.set_puntuacion()
    assert 90 == bowling.get_puntuacion()

    bowling = Bowling([[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/'],[5,'/',5]])
    bowling.set_puntuacion()
    assert 150 == bowling.get_puntuacion()

    bowling = Bowling([[9,'-'],[3,'/'],[6,1],[3,'/'],[8,1],[5,'/'],['-','/'],[8,'-'],[7,'/'],[8,'/',8]])
    bowling.set_puntuacion()
    assert 131 == bowling.get_puntuacion()

    bowling = Bowling([['X'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-']])
    bowling.set_puntuacion()
    assert 100 == bowling.get_puntuacion()

    bowling = Bowling([['X'],['X'],[8,'-'],[4,4],[4,4],[4,4],[4,4],[4,4],[4,4],[4,4]])
    bowling.set_puntuacion()
    assert 110 == bowling.get_puntuacion()

    bowling = Bowling([['X'],['X'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-']])
    bowling.set_puntuacion()
    assert 120 == bowling.get_puntuacion()

    bowling = Bowling([['X'],['X'],['X'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-']])
    bowling.set_puntuacion()
    assert 141 == bowling.get_puntuacion()

    bowling = Bowling([[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],[9,'-'],['X','X','X']])
    bowling.set_puntuacion()
    assert 111 == bowling.get_puntuacion()

    bowling = Bowling([['X'],['X'],[8,'-'],[4,4],[4,4],[4,4],[4,4],[4,4],[4,4],[4,4]])
    bowling.set_puntuacion()
    assert 110 == bowling.get_puntuacion()