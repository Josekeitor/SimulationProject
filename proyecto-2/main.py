import sys

from datetime import datetime, timedelta
from random import randint
from tabulate import tabulate

def is_valid_input(str):
    try:
        value = int(str)
    except ValueError:
        print('Valor debe ser un número entero')
        return False
    else:
        print('Valor debe ser mayor que 0')
        return value >= 1

START_TIME = datetime(year=1, month=1, day=1, hour=9)
FILE_NAME = 'results.txt'

value = input('Número de clientes que usarán el cajero: ')
if is_valid_input(value):
    n_clients = int(value)
else:
    sys.exit()

value = input('Tiempo máximo que le toma llegar a un cliente: ')
if is_valid_input(value):
    max_time_btw_arrivals = int(value)
else:
    sys.exit()

value = input('Tiempo máximo de duración de un trámite: ')
if is_valid_input(value):
    max_transaction_duration = int(value)
else:
    sys.exit()

n_clients_waited = 0
total_wait_time = 0
total_transaction_duration = 0
total_atm_inactivity_time = 0

# Primer cliente
client = 1
time_btw_arrivals = 0
arrival_time = START_TIME
transaction_duration = randint(1, max_transaction_duration)
service_start_time = arrival_time
service_end_time = service_start_time + timedelta(minutes=transaction_duration)
wait_time = 0
atm_inactivity_time = 0

row = {
    'client': client,
    'time_btw_arrivals': time_btw_arrivals,
    'arrival_time': arrival_time.strftime('%H:%M %p'),
    'transaction_duration': transaction_duration,
    'service_start_time': service_start_time.strftime('%H:%M %p'),
    'service_end_time': service_end_time.strftime('%H:%M %p'),
    'wait_time': wait_time,
    'atm_inactivity_time': atm_inactivity_time
}

# Guardar actividad del cliente
data = [row]

# Clientes consecutivos
for i in range(2, n_clients + 1):
    # Cliente
    client = i
    # Tiempo entre llegadas
    time_btw_arrivals = randint(1, max_time_btw_arrivals)
    # Hora de llegada
    arrival_time += timedelta(minutes=time_btw_arrivals)
    # Tiempo del trámite
    transaction_duration = randint(1, max_transaction_duration)
    # Hora de llegada fue antes que hora de fin de servicio del cliente anterior
    if arrival_time < service_end_time:
        # Tiempo de espera, hora de inicio de servicio, tiempo de inactividad del ATM
        wait_time = (service_end_time - arrival_time).total_seconds() / 60
        service_start_time = service_end_time
        atm_inactivity_time = 0
    # Hora de llegada fue después que hora de fin de servicio del cliente anterior
    else:
        # Tiempo de espera, hora de inicio de servicio, tiempo de inactividad del ATM
        wait_time = 0
        service_start_time = arrival_time
        atm_inactivity_time = (
            arrival_time - service_end_time).total_seconds() / 60

    # Hora de fin de servicio
    service_end_time = service_start_time + \
        timedelta(minutes=transaction_duration)

    row = {
        'client': client,
        'time_btw_arrivals': time_btw_arrivals,
        'arrival_time': arrival_time.strftime('%H:%M %p'),
        'transaction_duration': transaction_duration,
        'service_start_time': service_start_time.strftime('%H:%M %p'),
        'service_end_time': service_end_time.strftime('%H:%M %p'),
        'wait_time': wait_time,
        'atm_inactivity_time': atm_inactivity_time
    }

    # Guardar actividad del cliente
    data.append(row)

    # Tiempo total de espera de los clientes
    total_wait_time += wait_time
    # Duración total de las transacciones de los clientes
    total_transaction_duration += transaction_duration
    # Tiempo total de inactividad del ATM
    total_atm_inactivity_time += atm_inactivity_time

    # Registrar si el cliente tuvo que esperar
    if wait_time > 0:
        n_clients_waited += 1

# Tiempo total de ejecución de la simulación
total_time = (arrival_time - START_TIME).total_seconds() / 60

total_wait_time = int(total_wait_time)
total_transaction_duration = int(total_transaction_duration)
total_atm_inactivity_time = int(total_atm_inactivity_time)
total_time = int(total_time)

# Escribir resultados en archivo de texto
with open(FILE_NAME, 'w', encoding='utf-8') as f:
    f.write(tabulate(data, headers='keys'))
    f.write('\n')

    f.write('Tiempo de espera promedio por cliente')
    f.write('\n')
    f.write(f'{total_wait_time} min/{n_clients} clientes = {round(total_wait_time/n_clients, 1)} min de espera para ser atendidos')
    f.write('\n' * 2)

    f.write('Probabilidad de que un cliente espere en la fila')
    f.write('\n')
    f.write(f'{n_clients_waited} clientes esperando / {n_clients} clientes = {round((n_clients_waited / n_clients) * 100, 2)}%')
    f.write('\n' * 2)

    f.write('Porcentaje de tiempo en el que el ATM estuvo inactivo')
    f.write('\n')
    f.write(f'{total_atm_inactivity_time} min inactivo / {round(total_time)} min total = {round((total_atm_inactivity_time / total_time) * 100, 2)}%')
    f.write('\n' * 2)

    f.write('Tiempo promedio de servicio')
    f.write('\n')
    f.write(f'{total_transaction_duration} min trámite / {n_clients} clientes = {round(total_transaction_duration / n_clients, 1)} min de realizar el trámite')

# Fin
print(f'Los resultados han sido guardados en {FILE_NAME}')