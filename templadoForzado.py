import math
import random

sedes = [[40.514476148773156, -3.674447499629994],
         [40.533657515908644, -3.6564230558242317],
         [40.4893175, -3.3418228]]

# Cálculo de la tesela
tesela = 500
paralelo = 30.99233  # Un segundo en un paralelo son 30.99233 metros
meridiano = 30.7154  # Un segundo en un meridiano son 30.7154 metros

teselalon = tesela / paralelo / 3600
teselalat = tesela / meridiano / 3600

tesela = (teselalon + teselalat) / 2

# Aproximar las coordenadas de las sedes a las teselas
for i in range(len(sedes)):
    sedes[i][0] = int(round(sedes[i][0] / tesela))
    sedes[i][1] = int(round(sedes[i][1] / tesela))

print(sedes)


# Función de costo (ecuación a resolver y condiciones adicionales)
def costo(solucion):
    solucion_ecuacion=0
    costo =0
    solucion_ecuacion=1
    #for x in sedes:
    #    aux_solucion_ecuacion=0
    #    for i in range(0,len(solucion)):
    #        aux_solucion_ecuacion=solucion[i]*x[0]**i
    #    print(aux_solucion_ecuacion)
    #    costo+=abs(solucion_ecuacion-aux_solucion_ecuacion)
    #for x in range (0,len(sedes)-1):
    #    X=(sedes[x][0]+sedes[x+1][0])/2
    #    for i in range(0,len(solucion)):
    #        aux_solucion_ecuacion=solucion[i]*x**i
        
        #costo+=abs(2*1-aux_solucion_ecuacion)
    for x in sedes:
        aux_solucion_ecuacion=solucion[0]*x[0]*solucion[1]*x[0]**1+solucion[2]*x[0]**2+solucion[3]*x[0]**3
        costo+=abs(solucion_ecuacion-aux_solucion_ecuacion)

    return costo


# Función de vecino (genera una solución vecina)
def generar_vecino(solucion, temperatura):
    vecino = []
    for valor in solucion:
        vecino.append(valor + random.uniform(-temperatura, temperatura))
    return vecino


# Función de aceptación (determina si se acepta el vecino)
def aceptar_vecino(costo_actual, costo_vecino, temperatura):
    if costo_vecino < costo_actual:
        return True
    probabilidad_aceptacion = math.exp((costo_actual - costo_vecino) / temperatura)
    return random.random() < probabilidad_aceptacion


# Función de templado simulado
def templado_simulado(temperatura_inicial, temperatura_final, enfriamiento, num_variables):
    solucion_actual = [random.uniform(-100, 100) for _ in range(num_variables)]  # Valores iniciales aleatorios
    costo_actual = costo(solucion_actual)
    temperatura = temperatura_inicial
    iteracion = 1
    while temperatura > temperatura_final or costo_actual > 0.1:
        vecino = generar_vecino(solucion_actual, costo_actual * temperatura)
        costo_vecino = costo(vecino)
        print('costo----------------------------')
        print('iteracion ' + str(iteracion))
        print('costo ' + str(costo_actual))

        if aceptar_vecino(costo_actual, costo_vecino, temperatura):
            solucion_actual = vecino
            costo_actual = costo_vecino
        else:
            temperatura *= enfriamiento
        print(temperatura)
        print(solucion_actual)
        print('----------------------------------')
        iteracion += 1
        
    return solucion_actual


# Parámetros de ejecución
temperatura_inicial = 1000000000000000000000
temperatura_final = 0.1
enfriamiento = 0.999
num_variables = len(sedes)+1  # Número de incógnitas


# Ejecución del templado simulado
solucion = templado_simulado(temperatura_inicial, temperatura_final, enfriamiento, num_variables)
print("Solucion encontrada:", solucion)
print("Valor de la funcion de costo:", costo(solucion))
