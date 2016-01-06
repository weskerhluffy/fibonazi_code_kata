'''
Created on 03/01/2016

@author: ernesto
'''
from bitch_heap.ColaPrioridad import ColaPrioridad
from bitch_heap.NodoColaPrioridad import NodoColaPrioridades

if __name__ == '__main__':
    colita=ColaPrioridad()
    valor_actual=None
    
    colita.push("primero", NodoColaPrioridades.ALTA)
    colita.push("2", NodoColaPrioridades.BAJA)
#    colita.push("3", NodoColaPrioridades.MEDIA_PENDEJA)
    colita.push("4", NodoColaPrioridades.MEDIA_PENDEJA)
    colita.push("5", NodoColaPrioridades.MEDIA_PENDEJA)
    colita.push("6", NodoColaPrioridades.BAJA)
    colita.push("7", NodoColaPrioridades.BAJA)
#    colita.push("8", NodoColaPrioridades.MEDIA_PENDEJA)
    colita.push("9", NodoColaPrioridades.ALTA)

    valor_actual=colita.pop()
#    print("el valor %s con prioridad %s"%(valor_actual.valor,valor_actual.prioridad))
    while(valor_actual):
        print("el valor %s con prioridad %s"%(valor_actual.valor,valor_actual.prioridad))
        valor_actual=colita.pop()
