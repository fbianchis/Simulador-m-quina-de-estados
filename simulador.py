# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import signal, sys, time


#%% Declaraçao dos eventos

anterior = 0
state_pr = 0
a1 = 1
a2 = 2
a3 = 3
b1_i = 4
b1_f = 5 # evento que será protegido 
b2_i = 6
b2_f = 7
b3 = 8

#%% Tempo de cada evento em segundos 
t_a1 = 1
t_a2 = 1
t_a3 = 1
t_b1_i = 2
t_b1_f = 2
t_b2_i = 2
t_b2_f = 2
t_b3 = 3


#%% Tempo de envio e tempo de recebimento do protocolo ModBus (usando tempo maximo de time out para a simulação)

t_envio = 0.1
t_recebe = 0.1

#%% Funçoes para o tratamento os eventos 

def start(signum, frame):
    global finalizado
    finalizado =  1
    signal.alarm(0)
    
    
def saida (signum, frame):
    print('Finalizou')
    signal.alarm(0)
    sys.exit()
    
def delay_modbus (tipo,evento):

    if (tipo == 1):
        if(evento == b1_f):
            print()
            #linha para encriptografar
        time.sleep(t_envio)
    else:
        if(evento == b1_f):
            print()
            #linha para descriptografar 
        time.sleep(t_recebe)

def gerar_eventos_best_way (anterior):
    global finalizado 
    global state_nx
    if(finalizado == 1): 
        finalizado = 0
        if(anterior == 0):
            prox = a1
            signal.alarm(t_a1)
            delay_modbus(1,a1)
        elif(anterior == a1):
            prox = b1_i
            signal.alarm(t_b1_i)
            delay_modbus(1,b1_i)
        elif(anterior == b1_i):
            prox = b1_f
            signal.alarm(t_b1_f)
            delay_modbus(1,b1_f)
        elif(anterior == b1_f):
            prox = a2
            signal.alarm(t_a2)
            delay_modbus(1,a2)
        elif(anterior == a2):
            prox = b2_i
            signal.alarm(t_b2_i)
            delay_modbus(1,b2_i)
        elif(anterior == b2_i):
            prox = b2_f
            signal.alarm(t_b2_f)
            delay_modbus(1,b2_f)
        elif(anterior == b2_f):
            prox = a3
            signal.alarm(t_a3)
            delay_modbus(1,a2)
        elif(anterior == a3):
            prox = b3
            signal.alarm(t_b3)
            delay_modbus(1,b3)
        else:
            prox = 0
    else:
        prox =  anterior
    
    return prox


def state_machine (evento):
    global state_pr
    global state_nx
    if(state_pr == 0):
        if(evento == a1):
            state_nx = 1
        elif(evento == a2):
            state_nx = 31
        else:
            state_nx = 0
    elif(state_pr == 1):
        if(evento == a2):
            state_nx = 21
        elif(evento == b1_i):
            state_nx = 2
        else:
            state_nx = 1
    elif(state_pr == 2):
        if(evento == a2):
            state_nx = 17
        elif(evento == b1_f):
            state_nx = 3
        else:
            state_nx = 2
    elif(state_pr == 3):
        if (evento == a2):
            state_nx = 4
        else:
            state_nx = 3
    elif(state_pr == 4):
        if (evento == b2_i):
            state_nx = 5
        else:
            state_nx = 4
    elif(state_pr == 5):
        if(evento == b2_f):
            state_nx = 6
        else:
            state_nx = 5
    elif(state_pr == 6):
        if(evento == a3):
            state_nx = 7
        else:
            state_nx = 6
    elif(state_pr == 7):
        if(evento == a1):
            state_nx = 18
        elif(evento == a2):
            state_nx = 19
        elif(evento == b3):
            state_nx = 0
        else:
            state_nx = 7
    elif(state_pr == 8):
        if(evento == b3):
            state_nx = 6
        else:
            state_nx = 8
    elif(state_pr == 9):
        if(evento == b1_f):
            state_nx = 8
        elif(evento == b3):
            state_nx = 10
        else:
            state_nx = 9
    elif(state_pr == 10):
        if(evento == b1_f):
            state_nx = 6
        else:
            state_nx = 10
    elif(state_pr == 11):
        if(evento == b2_f):
            state_nx = 8
        elif(evento == b3):
            state_nx = 5
        else:
            state_nx = 11
    elif(state_pr == 12):
        if(evento == b2_i):
            state_nx = 11
        elif(evento  == b3):
            state_nx = 4
        else:
            state_nx = 12
    elif(state_pr == 13):
        if(evento == a2):
            state_nx = 12
        elif(evento == b3):
            state_nx = 3
        else:
            state_nx = 13
    elif(state_pr == 14):
        if(evento == b1_i):
            state_nx = 11
        elif(evento == b2_f):
            state_nx = 9
        elif(evento == b3):
            state_nx = 23
        else:
            state_nx = 14
    elif(state_pr == 15):
        if(evento == b1_f):
            state_nx = 12
        elif(evento == b2_i):
            state_nx = 14
        elif(evento == b3):
            state_nx = 17
        else:
            state_nx = 15
    elif(state_pr == 16):
        if(evento == a2):
            state_nx = 15
        elif(evento == b1_f):
            state_nx = 13
        elif(evento == b3):
            state_nx = 2
        else:
            state_nx = 16
    elif(state_pr == 17):
        if(evento == b1_f):
            state_nx = 4
        elif(evento == b2_i):
            state_nx = 23
        else:
            state_nx = 17
    elif(state_pr == 18):
        if(evento == a2):
            state_nx = 20
        elif(evento == b1_i):
            state_nx = 16
        elif(evento == b3):
            state_nx = 1
        else:
            state_nx = 18
    elif(state_pr == 19):
        if(evento == a2):
            state_nx = 20
        elif(evento == b2_i):
            state_nx = 28
        elif(evento == b3):
            state_nx = 31
        else:
            state_nx = 19
    elif(state_pr == 20):
        if(evento == b1_i):
            state_nx = 15
        elif(evento == b2_i):
            state_nx = 24
        elif(evento == b3):
            state_nx = 21
        else:
            state_nx = 20
    elif(state_pr == 21):
        if(evento == b1_f):
            state_nx = 17
        elif(evento == b2_i):
            state_nx = 22
        else:
            state_nx = 21
    elif(state_pr == 22):
        if(evento == b1_i):
            state_nx = 23
        elif(evento == b2_f):
            state_nx = 25
        else:
            state_nx = 22
    elif(state_pr == 23):
        if(evento == b1_f):
            state_nx = 5
        elif(evento == b2_f):
            state_nx = 10
        else:
            state_nx = 23
    elif(state_pr == 24):
        if(evento == b1_i):
            state_nx = 14
        elif(evento == b2_f):
            state_nx = 26
        elif(evento == b3):
            state_nx = 22
        else:
            state_nx = 24
    elif(state_pr == 25):
        if(evento == b1_i):
            state_nx = 10
        else:
            state_nx = 25
    elif(state_pr == 26):
        if(evento == b1_i):
            state_nx = 9
        elif(evento == b3):
            state_nx = 25
        else:
            state_nx = 26
    elif(state_pr == 27):
        if(evento == a1):
            state_nx = 26
        elif(evento == b3):
            state_nx = 29
        else:
            state_nx = 27
    elif(state_pr == 28):
        if(evento == a1):
            state_nx = 24
        elif(evento == b2_f):
            state_nx = 27
        elif(evento == b3):
            state_nx = 30
        else:
            state_nx = 28
    elif(state_pr == 29):
        if(evento == a1):
            state_nx = 25
        else:
            state_nx = 29
    elif(state_pr == 30):
        if(evento == a1):
            state_nx = 22
        elif(evento == b2_f):
            state_nx = 29
        else:
            state_nx =30
    elif(state_pr == 31):
        if(evento == a1):
            state_nx = 21
        elif(evento == b2_i):
            state_nx = 30
        else:
            state_nx = 31
    if (state_nx != state_pr):
        print("Mudou de estado:"+str(state_pr)+"->"+str(state_nx))
    state_pr = state_nx
    delay_modbus(0,state_pr)
    
#%% main
signal.signal(signal.SIGALRM, start)
signal.signal(signal.SIGINT,saida)


finalizado = 1
state_nx = 0
while(1):
    evento = gerar_eventos_best_way(anterior)
    anterior = evento
    state_machine(evento)

#print("tempo finalizado")
#signal.alarm(0)