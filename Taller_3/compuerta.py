'''Este módulo contiene el código fuente para crear compuertas lógicas.
   Define una clase padre (Compuerta) y dos clases hijas (CompuertaAND
   y CompuertaOR) así como sus atributos y métodos.
'''


class Compuerta():
    '''La clase Compuerta contiene la definición básica de una compuerta
       lógica, sus atributos (entradas y salida) así como los métodos para
       las asignación y consulta de los atributos

    Args:
        __entrada_a (int): Entada A de Compuerta. Debe ser 1 o 0
        __entrada_b (int): Entada B de Compuerta. Debe ser 1 o 0
        __salida_x (int): Salida X de Compuerta luego de operar
                          entradas A y B. Debe ser 1 o 0
    '''

    __entrada_a = 0
    __entrada_b = 0
    __salida_x = 0

    def set_entrada_a(self, valor_a):
        '''Asignar el valor ingresado (valor_a) al atributo __entrada_a de la
           compuerta. Se valida que sea un valor válido (1 o 0)

        Args:
            valor_a (int): valor que se asignar a entrada A de la compuerta
        '''
        if not isinstance(valor_a, int) or valor_a != 1 or valor_a != 0:
            print("Valor entrada A No válido. Debe ser 1 o 0")
        else:
            self.__entrada_a = valor_a

    def get_entrada_a(self):
        '''Consulta el valor de la entrada A de la compuerta. Retorna el
           valor de __entrada_a

        Returns:
            __entrada_a (int): valor asignado a entrada A de la compuerta
        '''
        return self.__entrada_a

    def set_entrada_b(self, valor_b):
        '''Asignar el valor ingresado (valor_b) al atributo __entrada_b de la
           compuerta. Se valida que sea un valor válido (1 o 0)

        Args:
            valor_b (int): valor que se asigna a entrada B de la compuerta
        '''
        if not isinstance(valor_b, int) or valor_b != 1 or valor_b != 0:
            print("Valor entrada B No válido. Debe ser 1 o 0")
        else:
            self.set_entrada_b(valor_b)

    def get_entrada_b(self):
        '''Consulta el valor de la entrada B de la compuerta. Retorna el
           valor de __entrada_b

        Returns:
            __entrada_b (int): valor asignado a entrada B de la compuerta
        '''
        return self.__entrada_b

    def get_salida_x(self):
        '''Consulta el valor de la salida de la compuerta. Retorna el
           valor de __salida_x

        Returns:
            __salida_x (int): resultado de operar las entradas de la compuerta
        '''
        return self.__salida_x


class CompuertaAND(Compuerta):
    '''La clase CompuertaAND es hija de la clase Compuerta, además de los
       atributos y métodos de la clase padre, contiene el método Operar
       que define el funcionamiento de una compuerta lógica AND

    Args:
        __entrada_a (int): Entada A de Compuerta. Debe ser 1 o 0
        __entrada_b (int): Entada B de Compuerta. Debe ser 1 o 0
        __salida_x (int): Salida X de Compuerta luego de operar
                          entradas A y B. Debe ser 1 o 0
    '''
    def operar(self):
        '''Realiza las operaciones lógicas de la compuerta AND tomando
           como parámetros las entradas (A y B) de la compuerta y el
           resultado lo asigna a la salida de la compuerta (__salida_x)
        '''
        if self.__entrada_a == 1 and self.__entrada_b == 1:
            self.__salida_x = 1
        else:
            self.__salida_x = 0


class CompuertaOR(Compuerta):
    '''La clase CompuertaOR es hija de la clase Compuerta, además de los
       atributos y métodos de la clase padre, contiene el método Operar
       que define el funcionamiento de una compuerta lógica OR

    Args:
        __entrada_a (int): Entada A de Compuerta. Debe ser 1 o 0
        __entrada_b (int): Entada B de Compuerta. Debe ser 1 o 0
        __salida_x (int): Salida X de Compuerta luego de operar
                          entradas A y B. Debe ser 1 o 0
    '''

    def operar(self):
        '''Realiza la operaciones lógicas de la compuerta OR tomando
           como parámetros las entradas (A y B) de la compuerta y el
           resultado lo asigna a la salida de la compuerta (__salida_x)
        '''
        if self.__entrada_a == 0 and self.__entrada_b == 0:
            self.__salida_x = 0
        else:
            self.__salida_x = 1
