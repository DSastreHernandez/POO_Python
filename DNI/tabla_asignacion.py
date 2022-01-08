class tabla_asignacion:

    def __init__(self):
        self.tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J','Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]

    def get_letra(self, posicion):
        return self.tabla[posicion]

    def letra_permitida(self,letra):
        return letra in self.tabla 
    
    def get_longitud(self):
        return len(self.tabla)

    def calcular_letra(self,dni):
        posicion = int(dni) % self.get_longitud()
        return self.get_letra(posicion)

if __name__ == '__main__':
    
    import random

    contador = 0

    asignacion = tabla_asignacion()
    
    for letra in asignacion.tabla:
        assert(asignacion.get_letra(contador),letra)
        contador += 1

    letras_no_permitidas = ['I','Ñ','O','U','Ç']

    for letra in letras_no_permitidas:
        assert (asignacion.letra_permitida(letra),False)
    
    casos_validos = [ #casos OK
				 "78484464T","72376173A","01817200Q","95882054E","63587725Q",
				 "26861694V","21616083Q","26868974Y","40135330P","89044648X",
				 "80117501Z","34168723S","76857238R","66714505S","66499420A"]
    
    num_casos = 15

    for i in range(0, num_casos):
        caso=''
        
        for j in range(0,8):
            num_aleatorio = random.randrange(48, 57 + 1, 1)
            caso += chr(num_aleatorio)
        
        caso+= asignacion.tabla[int(caso) % 23]

        casos_validos.append(caso)

    for dni in casos_validos:
        assert(asignacion.calcular_letra(dni[:-1]), dni[-1])
 
        
