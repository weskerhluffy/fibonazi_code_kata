'''
Created on 03/01/2016

@author: ernesto
'''
from bitch_heap.MontonBinario import MontonBinario
from bitch_heap.NodoColaPrioridad import NodoColaPrioridad, NodoColaPrioridades

class ColaPrioridad(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.monton = MontonBinario("auto_apuntador", NodoColaPrioridad.comparar_nodos, min=False)

    def push(self, valor, prioridad):
        nuevo_nodo = None
        
#        print("la prioridad es %s"% prioridad)
        assert(isinstance(prioridad, NodoColaPrioridades))
        
        nuevo_nodo = NodoColaPrioridad(valor, prioridad)
        self.monton.insertar(nuevo_nodo)
        print("los nodos al insertar %s" % nuevo_nodo)
        print("%s" % self.monton)
    
    def pop(self):
        nodo_cima = None
        
        nodo_cima = self.monton.pop_o()
#        print("lo q regresa el monton %s"%nodo_cima)

        print("los nodos al remover %s" % nodo_cima)
        print("%s" % self.monton)
        
        return nodo_cima
