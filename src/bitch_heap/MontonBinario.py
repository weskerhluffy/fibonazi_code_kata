'''
Created on 02/01/2016

@author: ernesto
'''
from bitch_heap.NodoMonton import NodoMonton
import math
from bitch_heap.NodoColaPrioridad import NodoColaPrioridad

class MontonBinario(object):
    '''
    classdocs
    '''
    def __init__(self, atributo_llave=None, funcion_comparar=None, min=False):
        '''
        Constructor
        '''
        self.nodos = []
        self.atributo_llave = atributo_llave
        self.funcion_comparar = funcion_comparar
        self.min = min
        self._inicializar()

    def _inicializar(self):
        assert(self.atributo_llave and self.funcion_comparar)
        
    def insertar(self, valor):
        idx_ancestro_actual = 0
        idx_nodo_actual = 0
        idx_nodo_insertado = 0
        num_nodos = 0
        llave = None
        nodo_nuevo = None

        assert(hasattr(valor, self.atributo_llave))
        llave = getattr(valor, self.atributo_llave)
            
        nodo_nuevo = NodoMonton(valor, llave)
        self.nodos.append(nodo_nuevo)
        num_nodos = len(self.nodos)
        idx_nodo_insertado = num_nodos - 1
        idx_ancestro_actual = math.floor((idx_nodo_insertado - 1) / 2)
        idx_nodo_actual = idx_nodo_insertado
        
        while(idx_ancestro_actual > -1):
            desorden_detectado = False
            resultado_comp = 0
            nodo_ancestro_actual = None
            nodo_actual = None
            
            nodo_ancestro_actual = self.nodos[idx_ancestro_actual]
            nodo_actual = self.nodos[idx_nodo_actual]
            
            resultado_comp = self.funcion_comparar(nodo_actual.llave, nodo_ancestro_actual.llave)
            if(not resultado_comp):
                resultado_comp = NodoColaPrioridad.comparar_timestamp(nodo_actual.llave, nodo_ancestro_actual.llave) 
                if(not self.min):
                    resultado_comp *= -1
                
            print("comparando para insertar %s con %s" % (nodo_actual.llave, nodo_ancestro_actual.llave))
            print("resultado comp %s" % resultado_comp)
            
            assert(resultado_comp)
            if(self.min):
                desorden_detectado = resultado_comp < 0
            else:
                desorden_detectado = resultado_comp > 0
                
            print("desordenados %s" % desorden_detectado)
            if(desorden_detectado):
                NodoMonton.intercambia_nodos(nodo_actual, nodo_ancestro_actual)
            else:
                break
            
            idx_nodo_actual = idx_ancestro_actual
            idx_ancestro_actual = math.floor((idx_ancestro_actual - 1) / 2)
                
    def pop_o(self):
        idx_nodo_actual = 0
        idx_nodo_hijo_izq = 0
        idx_nodo_hijo_der = 0
        num_nodos = 0
        valor = None
        ultimo_nodo = None
        primer_nodo = None
        nodo_actual = None
        nodo_hijo_izq = None
        nodo_hijo_der = None
        
        num_nodos = len(self.nodos)
        if(not num_nodos):
            return None
        
        ultimo_nodo = self.nodos.pop()
        
        num_nodos = len(self.nodos)
        if(not num_nodos):
            return ultimo_nodo.valor
        
        primer_nodo = self.nodos[0]
        
        
        valor = primer_nodo.valor
        
        NodoMonton.intercambia_nodos(primer_nodo, ultimo_nodo)
        
        idx_nodo_actual = 0
        while(idx_nodo_actual < num_nodos):
            idx_hijo_elegido = 0
            resultado_comp_izq = 0
            resultado_comp_der = 0
            resultado_comp_ambos_hijos_iguales = 0
            relacion_padre_hijo_izq = 0
            relacion_padre_hijo_der = 0
            llave_hijo_izq = None
            llave_hijo_der = None
            llave_actual = None
            nodo_hijo_elegido = None
            llaves_ordenadas_por_ts = []
            
            idx_nodo_hijo_izq = idx_nodo_actual * 2 + 1
            idx_nodo_hijo_der = idx_nodo_actual * 2 + 2
        
            nodo_actual = self.nodos[idx_nodo_actual]
            llave_actual = nodo_actual.llave
            
            if(idx_nodo_hijo_izq < num_nodos):
                nodo_hijo_izq = self.nodos[idx_nodo_hijo_izq]
                llave_hijo_izq = nodo_hijo_izq.llave
                if(idx_nodo_hijo_der < num_nodos):
                    nodo_hijo_der = self.nodos[idx_nodo_hijo_der]
                    llave_hijo_der = nodo_hijo_der.llave
                
            if(llave_hijo_izq is None):
                break
            
            print("comparando llave actual %s con hijo izq %s" % (llave_actual, llave_hijo_izq))
            resultado_comp_izq = self.funcion_comparar(llave_actual, llave_hijo_izq)
            if(self.min):
                relacion_padre_hijo_izq = resultado_comp_izq > 0
            else:
                relacion_padre_hijo_izq = resultado_comp_izq < 0
            
                
            if(llave_hijo_der):
                print("comparando llave actual %s con hijo der %s" % (llave_actual, llave_hijo_der))
                resultado_comp_der = self.funcion_comparar(llave_actual, llave_hijo_der)
                if(self.min):
                    relacion_padre_hijo_der = resultado_comp_der > 0
                else:
                    relacion_padre_hijo_der = resultado_comp_der < 0
            
            print("relacion padre ijo izq %d" % resultado_comp_izq)
            print("relacion padre ijo der %d" % resultado_comp_der)
                    
            
            if(abs(resultado_comp_der) > abs(resultado_comp_izq)):
                if(relacion_padre_hijo_der):
                    idx_hijo_elegido = idx_nodo_hijo_der
                    nodo_hijo_elegido = nodo_hijo_der
            else:
                if(abs(resultado_comp_der) < abs(resultado_comp_izq)):
                    if(relacion_padre_hijo_izq):
                        idx_hijo_elegido = idx_nodo_hijo_izq
                        nodo_hijo_elegido = nodo_hijo_izq
                else:
                    if(llave_hijo_der and resultado_comp_der == resultado_comp_izq):
                        if(resultado_comp_der):
                            print("comparando timestamps aora %10.6f con %10.6f" % (nodo_hijo_izq.llave.estampa_tiempo, nodo_hijo_der.llave.estampa_tiempo))
                            resultado_comp_ambos_hijos_iguales = NodoColaPrioridad.comparar_timestamp(nodo_hijo_izq.llave, nodo_hijo_der.llave)
                            print("resultado comp ts %10.6f" % resultado_comp_ambos_hijos_iguales)
                            assert(resultado_comp_ambos_hijos_iguales)
                            if(resultado_comp_ambos_hijos_iguales < 0):
                                idx_hijo_elegido = idx_nodo_hijo_izq
                                nodo_hijo_elegido = nodo_hijo_izq
                            else:
                                idx_hijo_elegido = idx_nodo_hijo_der
                                nodo_hijo_elegido = nodo_hijo_der
                        else:
                            llaves_ordenadas_por_ts = sorted([nodo_actual.llave, llave_hijo_izq, llave_hijo_der], key=lambda x: x.estampa_tiempo, reverse=False)
                            if(not self.funcion_comparar(llave_hijo_izq, llaves_ordenadas_por_ts[0])):
                                idx_hijo_elegido = idx_nodo_hijo_izq
                                nodo_hijo_elegido = nodo_hijo_izq
                            else:
                                if(not self.funcion_comparar(llave_hijo_der, llaves_ordenadas_por_ts[0])):
                                    idx_hijo_elegido = idx_nodo_hijo_der
                                    nodo_hijo_elegido = nodo_hijo_der
                    else:
                        if(not llave_hijo_der):
                            idx_hijo_elegido = idx_nodo_hijo_izq
                            nodo_hijo_elegido = nodo_hijo_izq
                            
                                
            
            if(not idx_hijo_elegido):
                break
            
            if(nodo_hijo_elegido):
                NodoMonton.intercambia_nodos(nodo_actual, nodo_hijo_elegido)
                    
            idx_nodo_actual = idx_hijo_elegido
            
        return valor
    
    def imprimir_nodo(self, idx_nodo, profundidad, buf):
        nodo = None
        
        if(idx_nodo > len(self.nodos) - 1):
            return
        
        nodo = self.nodos[idx_nodo]
        
        for _ in range(profundidad):
            buf += list("\t")
        buf += list("%s\n" % nodo)
        self.imprimir_nodo(idx_nodo * 2 + 1, profundidad + 1, buf)
        self.imprimir_nodo(idx_nodo * 2 + 2, profundidad + 1, buf)
        
    def imprimir_arbolin(self, cadena):
        self.imprimir_nodo(0, 0, cadena)
                
    def __str__(self):
        cad = []
        self.imprimir_arbolin(cad)
        return "%s" % "".join(cad)
        
