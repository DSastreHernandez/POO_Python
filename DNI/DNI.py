from tabla_asignacion import *
import string

class DNI:
    
    def __init__(self,cadena = ''):    
        self.dni = cadena
        self.numero_sano = False
        self.letra_sana = False
        self.tabla = tabla_asignacion()

    ### Interfaz Publica ###
    
    def set_dni(self, cadena):
        self.dni = cadena

    def get_dni(self):
        return self.dni

    def set_numero_sano(self, valor):
        self.numero_sano = valor

    def get_numero_sano(self):
        return self.numero_sano

    def set_letra_sana(self,valor):
        self.letra_sana = valor

    def get_letra_sana(self):
        return self.letra_sana

    def check_cif(self):
        return self.check_dni() and self.check_letra()

    def check_dni(self):
        self.set_numero_sano( self.check_longitud() and self.check_numero())
        return self.numero_sano

    def check_letra(self):
        if self.dni[-1] == self.get_letra():
            self.set_letra_sana(True)
        return self.letra_sana

    def get_letra(self):
        if self.get_numero_sano():
            return self.tabla.calcular_letra(self.get_parte_numerica())
        else:
            return False

    ### Interfaz Privada ###

    def check_longitud(self):
        return len(self.dni) == 9

    def check_numero(self):
        try:
            int(self.dni[:-1])
            return True
        
        except:
            return False

    def get_parte_alfabetica(self):    
        
        if self.get_letra_sana():
            return self.dni[-1] 
        
        solo_letras = ""
        alfabeto = string.ascii_letters
        for element in self.dni:

            if alfabeto.find(element)>-1:
                solo_letras += element

        return solo_letras  


    def get_parte_numerica(self):
        
        if self.get_numero_sano() and self.get_letra_sana():
            return self.dni[:-1]
        
        solo_num = ""
        for element in self.dni:
        
            try:
                int(element)
                solo_num += str(element)
        
            except:
                pass
        
        return solo_num

if __name__ == 	'__main__':  

    casos_test = [ #casos OK
				 "78484464T","72376173A","01817200Q","95882054E","63587725Q",
				 "26861694V","21616083Q","26868974Y","40135330P","89044648X",
				 "80117501Z","34168723S","76857238R","66714505S","66499420A"]

    for dni in casos_test:
		
        objeto = DNI(dni)
		
        assert (objeto.get_dni()== dni)
		
        assert (objeto.check_cif()== True)
		
        assert (objeto.get_numero_sano()== objeto.numero_sano)
		
        assert (objeto.get_letra()== dni[-1])
		
        assert (objeto.get_letra_sana()== objeto.letra_sana)
		
        assert (objeto.get_parte_numerica()== objeto.dni[:-1])

        assert (objeto.get_parte_alfabetica()== objeto.dni[-1])

    casos_test = [ #casos letra mal
				 "78484464I","72376173B","01817200T","95882054S","63587725A",
				 "26861694W","21616083S","26868974A","40135330S","89044648P",
				 "80117501X","34168723A","76857238S","66714505R","66499420Q"]

    for dni in casos_test:

        objeto = DNI(dni)

        assert (objeto.get_dni()== dni)

        assert (objeto.check_cif()== False)

        assert (objeto.get_numero_sano()== objeto.numero_sano)

        assert (objeto.get_letra() == objeto.tabla.tabla[int(dni[:-1])%23])
		
        assert (objeto.get_letra_sana()== objeto.letra_sana)
		
        assert (objeto.get_parte_numerica()== objeto.dni[:-1])

        assert (objeto.get_parte_alfabetica()== objeto.dni[-1])

    casos_test = [ #casos longitud MAL
				 "78444T","72173A","018100Q","9582054E","6357787725Q",
				 "26694V","21083Q","2674Y","40330P","8948X",
				 "80117222201Z","3416833333333723S","7657238R","667143333505S","664333399420A"]

    for dni in casos_test:

        objeto = DNI(dni)

        assert (objeto.get_dni()== dni)

        assert (objeto.check_cif()== False)

        assert (objeto.get_numero_sano()== objeto.numero_sano)

        assert (objeto.get_letra() == False)
		
        assert (objeto.get_letra_sana()== objeto.letra_sana)
		
        assert (objeto.get_parte_numerica()== objeto.dni[:-1])

        assert (objeto.get_parte_alfabetica()== objeto.dni[-1])

    casos_test = [ #casos todo numeros
				 "784844641","723761731","018172001","958820541","635877251",
				 "268616941","216160831","268689741","401353301","890446481",
				 "801175011","341687231","768572381","667145051","664994201"]

    for dni in casos_test:

        objeto = DNI(dni)

        assert (objeto.get_dni()== dni)

        assert (objeto.check_cif()== False)

        assert (objeto.get_numero_sano()== objeto.numero_sano)

        assert (objeto.get_letra() == objeto.tabla.calcular_letra(dni))
		
        assert (objeto.get_letra_sana()== False)
		
        assert (objeto.get_parte_numerica()== objeto.dni)

        assert (objeto.get_parte_alfabetica()== "")

    casos_test = [ #casos todo LETRAS
				 "ALOALOAAO","BBOOBBOOP","AKSKCLERP"]
        
    for dni in casos_test:

        objeto = DNI(dni)

        assert (objeto.get_dni()== dni)

        assert (objeto.check_cif()== False)

        assert (objeto.get_numero_sano()== False)

        assert (objeto.get_letra() == False)
		
        assert (objeto.get_letra_sana()== False)
		
        assert (objeto.get_parte_numerica()== "")

        assert (objeto.get_parte_alfabetica()== objeto.dni)