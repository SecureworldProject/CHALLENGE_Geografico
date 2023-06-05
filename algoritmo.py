
import numpy as np
import random
#calculo de "tesela" de longitud de tesela
#
#tesela=500


#paralelo=30.99233 #un segundo en un paralero son 30.99233 metros  lon*Paralero
#meridiano=30.7154 #un segundo en un meridiano son 30.7154 metros lat*meridiano

#teselalon=tesela/paralelo/3600
#teselalat=tesela/meridiano/3600
##simplificar los calculos hacemos la media
#tesela=(teselalon+teselalat)/2

##-------------------------------------------------escribimos en una matriz las longitudes y las latitudes de todas las sedes--------------------------------------
##obtener latitud y longitud del google maps es valido ya que utiliza el mismo elipsoide wgs84 el mismo utilizado para el GPS



##numero = random.randint(1, 10)

#numero=8

#sedes=[[40.514476148773156, -3.674447499629994],
#       [40.533657515908644, -3.6564230558242317]]
#       #[40.4893175, -3.3418228 ]]

#lat=[]
#lon=[]
#resultado=[]
#gradoDelPolinomio=len(sedes)
#media=np.mean(sedes, axis=0)//tesela





#for i in sedes:
#    aux_lat=int((round(i[0], 7)//tesela)-media[0])
#    aux_lon=int((round(i[1], 7)//tesela)-media[1])

#    exponencial_latitudes=[]
#    #if len(lat)==0 or lat[-1][-1]==-1:
#    #    derivada_latitudes=[1,aux_lon*2,0,+1]
#    #else:
#    #    derivada_latitudes=[1,aux_lon*2,0,-1]
#    derivadas_longitudes=[1]
#    exponencial_longitudes=[]
#    for x in range(1,1+gradoDelPolinomio):
#        exponencial_latitudes.append(aux_lat**x)
#        exponencial_longitudes.append(aux_lon**x)
#    #-------------------------------------------------------
#    exponencial_latitudes.append(1)
#    #exponencial_longitudes.append(1)
#    #exponencial_latitudes.append(0)
#    #exponencial_longitudes.append(0)
#    #-------------------------------------------------------
#    lat.append(exponencial_latitudes)
#    #lat.append(derivada_latitudes)
#    lon.append(exponencial_longitudes)
#    resultado.append([numero])
#    #resultado.append([0])
#resultado.append([2*numero])
#resultado.append([0])
#lat.append([0,0,1])


resultado=[[5],[5],[10],[0]]
X=[[-21,441,1], 
   [-17, 289,1],
   [-19,361,1],
   [1,2*(-19),0]]


print(X)
print(resultado)

C = np.linalg.lstsq(X,resultado,rcond=None)[0]

print('solucion')
print(C)

print(np.matmul(x,C[0]))

