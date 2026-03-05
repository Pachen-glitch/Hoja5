import simpy
import random
import numpy as np

RANDOM_SEED = 42


def generador(env, ram, cpu, num_procesos, tiempos, intervalo, instrucciones_por_turno):
    for i in range(num_procesos):
        tiempo_espera = random.expovariate(1.0 / intervalo)
        yield env.timeout(tiempo_espera)
        env.process(
            proceso(env, ram, cpu, tiempos, instrucciones_por_turno)
        )


def proceso(env, ram, cpu, tiempos, instrucciones_por_turno):
    llegada = env.now

    memoria = random.randint(1, 10)
    yield ram.get(memoria)

    instrucciones = random.randint(1, 10)

    while instrucciones > 0:
        with cpu.request() as req:
            yield req
            ejecutar = min(instrucciones_por_turno, instrucciones)
            yield env.timeout(1)
            instrucciones -= ejecutar

    yield ram.put(memoria)

    tiempo_total = env.now - llegada
    tiempos.append(tiempo_total)


def correr_simulacion(num_procesos, intervalo, ram_capacity, cpu_capacity, instrucciones_por_turno):

    random.seed(RANDOM_SEED)

    env = simpy.Environment()

    ram = simpy.Container(env, init=ram_capacity, capacity=ram_capacity)
    cpu = simpy.Resource(env, capacity=cpu_capacity)

    tiempos = []

    env.process(
        generador(env, ram, cpu, num_procesos, tiempos, intervalo, instrucciones_por_turno)
    )

    env.run()

    promedio = np.mean(tiempos)
    desviacion = np.std(tiempos)

    return promedio, desviacion


def experimento(intervalo, ram, cpu, instrucciones_turno):

    cantidades = [25, 50, 100, 150, 200]
    promedios = []

    for n in cantidades:
        prom, _ = correr_simulacion(
            n,
            intervalo,
            ram,
            cpu,
            instrucciones_turno
        )
        promedios.append(prom)

    return cantidades, promedios