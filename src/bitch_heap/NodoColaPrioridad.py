'''
Created on 03/01/2016

@author: ernesto
'''
import time
from enum import unique, IntEnum


@unique
class NodoColaPrioridades(IntEnum):
    INVALIDA = -1
    ALTA = 2
    MEDIA_PENDEJA = 1
    BAJA = 0
    
class NodoColaPrioridad(object):
    '''
    classdocs
    '''

    def __init__(self, valor, prioridad):
        '''
        Constructor
        '''
        self.prioridad = prioridad
        self.valor = valor
        self.estampa_tiempo = time.time()
        self.auto_apuntador = self
        
    @staticmethod
    def comparar_timestamp(valor_1, valor_2):
        res = 0
        ts1 = None
        ts2 = None
        
        ts1 = valor_1.estampa_tiempo
        ts2 = valor_2.estampa_tiempo
        
        res = ts1 - ts2
        
        return res
    
    @staticmethod
    def comparar_nodos(nodo_1, nodo_2):
        resultado = 0
        prioridad_1 = NodoColaPrioridades.INVALIDA
        prioridad_2 = NodoColaPrioridades.INVALIDA
        
        prioridad_1 = nodo_1.prioridad
        prioridad_2 = nodo_2.prioridad
        
        print("comparando nodo 1 %s con nodo 2 %s" % (nodo_1, nodo_2))
        print("sus prioridades %d, %d" % (prioridad_1, prioridad_2))
        resultado = prioridad_1 - prioridad_2
        print("la resta es %d" % resultado)
        
#        if(not resultado):
#            resultado = NodoColaPrioridad.comparar_timestamp(nodo_1, nodo_2)
        
#        assert(resultado)
        
        return resultado
    
    def __str__(self):
        return "prioridad %s, valor %s, estampa tiempo %10.6f" % (self.prioridad, self.valor, self.estampa_tiempo)
