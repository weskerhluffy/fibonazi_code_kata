'''
Created on 02/01/2016

@author: ernesto
'''
class NodoMonton(object):
    '''
    classdocs
    '''

    def __init__(self, valor, llave):
        '''
        Constructor
        '''
        self.valor = valor
        self.llave = llave
            
    @staticmethod
    def intercambia_nodos(nodo_1, nodo_2):
        llave_tmp = None
        valor_tmp = None
        print("antes de intercambiar")
        print("nodo 1 %s"%nodo_1)
        print("nodo 2 %s"%nodo_2)
        
        llave_tmp = nodo_1.llave
        valor_tmp = nodo_1.valor
        
        nodo_1.llave = nodo_2.llave
        nodo_1.valor = nodo_2.valor
        
        nodo_2.llave = llave_tmp
        nodo_2.valor = valor_tmp
        
        print("despues de intercambiar")
        print("nodo 1 %s"%nodo_1)
        print("nodo 2 %s"%nodo_2)
    
    def __str__(self):
        return "NM llave %s, NM valor %s" % (self.llave, self.valor)
    
    def __repr__(self, *args, **kwargs):
        return "NodoMonton:" + object.__repr__(self, *args, **kwargs) + " " + self.__str__()
