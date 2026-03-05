import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

# Semilla
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Parámetros iniciales
INTERVALO = 10
RAM_CAPACITY = 100
CPU_CAPACITY = 1
INSTRUCCIONES_POR_TURNO = 3

def proceso(env, nombre, cpu):
    print(nombre, "llega en tiempo", env.now)
    
    instrucciones = random.randint(1, 10)
    print(nombre, "tiene", instrucciones, "instrucciones")
    
    while instrucciones > 0:
        with cpu.request() as req:
            yield req
            
            ejecutar = min(INSTRUCCIONES_POR_TURNO, instrucciones)
            
            print(nombre, "usa CPU en", env.now, 
                  "ejecutando", ejecutar, "instrucciones")
            
            yield env.timeout(1)
            
            instrucciones -= ejecutar
            
            print(nombre, "le quedan", instrucciones, "instrucciones")
    
    print(nombre, "termina en tiempo", env.now)
# Crear el entorno 
env = simpy.Environment()

# Crear recursos dentro del entorno
ram = simpy.Container(env, init=RAM_CAPACITY, capacity=RAM_CAPACITY)
cpu = simpy.Resource(env, capacity=CPU_CAPACITY)

print("Tiempo inicial:", env.now)
print("RAM disponible:", ram.level)
print("Capacidad CPU:", cpu.capacity)

env.process(proceso(env, "Proceso 1", cpu))
env.process(proceso(env, "Proceso 2", cpu))
env.run()


