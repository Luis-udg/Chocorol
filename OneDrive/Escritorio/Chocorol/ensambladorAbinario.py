import re

def ensambladorAbinario(instruccionEnsamblador):
    operaciones={
        'AND'   :'000',
        'OR'    :'001',
        'SUMA'  :'010',
        'RESTA' :'011',
        'RESTA' :'011',
        'MENORQ':'100',
        'LEER'  :'111'
    }
    direccionesMemoria={
        "0":'00000',
        '1':'00001',
        '2':'00010',
        '3':'00011',
        '4':'00100',
        '5':'00101',
        '6':'00110',
        '7':'00111'
    }
    partes=instruccionEnsamblador.split()
    operacion=partes[0]
    opAluBinario=operaciones.get(operacion)
    patron = re.compile(r'\$([0-9]+)')
    resultados = patron.findall(instruccionEnsamblador)
    dirMemoriaB = direccionesMemoria.get(resultados[0])
    if operacion == 'LEER' :
        MC='10'
        dir1Lectura = "00000"
        dir2Lectura = "00010"
    else:
        MC='01'
        dir1Lectura = direccionesMemoria.get(resultados[1])
        dir2Lectura = direccionesMemoria.get(resultados[2])
    
    return MC+dir1Lectura+opAluBinario+dir2Lectura+dirMemoriaB
