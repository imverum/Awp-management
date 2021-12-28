from datetime import date
data_atual = date.today()
import pandas as pd

################################Funções auxiliares
def filter_null_predecessor(cod):
    if cod[-5:] == 'XXXXX':
        return False
    else:
        return True
    
def get_string(n, left=True):
    if left:
        def f(string):
            return string[:n]
    else:
        def f(string):
            return string[len(string)-n:]
    return f

def cod_int_number_3dig(n):
    n=int(n-1)
    if n<10:
        return f'00{n}'
    elif n<100:
        return f'0{n}'
    else:
        return str(n)
    
def cod_int_number_4dig(n):
    n=int(n-1)
    if n<10:
        return f'000{n}'
    elif n<100:
        return f'00{n}'
    elif n<1000:
        return f'0{n}'
    else:
        return str(n)
    
def cod_int_number_6dig(n):
    n=int(n-1)
    if n<10:
        return f'00000{n}'
    elif n<100:
        return f'0000{n}'
    elif n<1000:
        return f'000{n}'
    elif n<10000:
        return f'00{n}'
    elif n<100000:
        return f'0{n}'
    else:
        return str(n)
    
