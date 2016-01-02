# |/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
'''
Created on 31/12/2015

@author: ernesto
'''
import array
from functools import wraps

def deco_memo(func):
    print("me lleva la mierda")
    @wraps(func)
    def func_deco(*args, **kwargs):
        numero = 0
        res = 0
        numero = args[0]
        if(numero is None):
            numero = kwargs["numero"]
        assert(numero is not None)
        print("interceptando mamada %d" % numero);
        if not hasattr(func, "cachete"):
            func.cachete = {}
        if numero not in func.cachete:
            print("ejecutando x q no se tenia en cachete %d" % numero)
            res = func(*args, **kwargs)
            func.cachete[numero] = res
        else:
            print("se saca de cachate %d" % numero)
            res = func.cachete[numero]
        return res
    return func_deco

@deco_memo
def fibonazzzi(numero, repulsivo=False):
    resultado = 0 
    if(repulsivo):
        print("aciendo llamadas repulsivas para calcular fibo de %d" % numero)
        if(numero == 1 or numero == 0):
            print("se llego al caca base %d" % numero)
            resultado = 1 
        else:
            print("llamando a los fibonazis de %d" % numero)
            resultado = fibonazzzi(numero - 1, repulsivo) + fibonazzzi(numero - 2, repulsivo)
    else:
        numero_actual = 0
        if not hasattr(fibonazzzi, "fibonazis"):
            print("generando arreglo para numeros")
#            fibonazzzi.fibonazis = [None for _ in range(numero + 1)]
            fibonazzzi.fibonazis = array.array("l", [1, 1])
        
        if(numero > 1):
            print("iterando para calcular fibo de %d" % numero)
            for numero_actual in range(2, numero + 1):
                if(len(fibonazzzi.fibonazis) <= numero_actual):
                    resultado = fibonazzzi.fibonazis[numero_actual - 1] + fibonazzzi.fibonazis[numero_actual - 2]
                    print("el fbo de %d es %d" % (numero_actual, resultado))
                    fibonazzzi.fibonazis.append(resultado)
            
        print("los numerillos son %s" % fibonazzzi.fibonazis)
        resultado = fibonazzzi.fibonazis[numero]
        
    return resultado

def p_decorate(func):
    print("pero la puta madre")
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)



if __name__ == '__main__':
    caca = 0
    print("caca")
    caca = fibonazzzi(11)
    print("la mierda %d" % caca)
    caca = fibonazzzi(5)
    print("la mierda %d" % caca)
    caca = fibonazzzi(15)
    print("a toda ley poderosa %d" % caca)
    caca = fibonazzzi(11, repulsivo=True)
    print("el tirano y el abaro %d" % caca)
    caca = fibonazzzi(5, repulsivo=True)
    print("la mort %d" % caca)
    

    print(get_text("John"))
