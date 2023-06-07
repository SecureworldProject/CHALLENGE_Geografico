
import numpy as np
import random
#calculo de "tesela" de longitud de tesela
#buscamos en google maps la longitud y la latitud de las sedes
sedes = [[40.514476148773156, -3.674447499629994],
         [40.533657515908644, -3.6564230558242317],
         #[40.4893175, -3.3418228]]
         [40.4993175, -3.3418228]]


# Cálculo de la tesela
tesela = 500
paralelo = 30.99233  # Un segundo en un paralelo son 30.99233 metros
meridiano = 30.7154  # Un segundo en un meridiano son 30.7154 metros

teselalon = tesela / paralelo / 3600
teselalat = tesela / meridiano / 3600

tesela = (teselalon + teselalat) / 2
X=[]
Y=[]

for i in range(len(sedes)):
    X.append( int(round(sedes[i][0] / tesela)))
    Y.append(int(round(sedes[i][1] / tesela)))

print(X)
print(Y)

lat = np.poly1d([1])
lon= np.poly1d([1])
for i in X:
    solucion_parcial = np.poly1d([1,-i])
    lat=np.polymul(solucion_parcial, lat)


print('solucion latitud')
print(lat)

for i in Y:
    solucion_parcial = np.poly1d([1,-i])

    lon=np.polymul(solucion_parcial, lon)


print('solucion longitud')
print(lon)

np.savez('ecuaciones',lat,lon)

#print('solucion')
#print(C)
#print(np.matmul(x,C[0]))

