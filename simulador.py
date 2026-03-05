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

# Crear el entorno 
env = simpy.Environment()


# Crear recursos dentro del entorno
ram = simpy.Container(env, init=RAM_CAPACITY, capacity=RAM_CAPACITY)
cpu = simpy.Resource(env, capacity=CPU_CAPACITY)

print("RAM disponible:", ram.level)
print("Capacidad CPU:", cpu.capacity)
print("Tiempo inicial:", env.now)