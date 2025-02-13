import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# Un canal en caso de estereo
def extraeuncanal(sonido):
    canales=sonido.shape
    cuantos=len(canales)
    canal = 0
    if (cuantos==1): # Monofónico
        uncanal=sonido[:]
    if (cuantos>=2): # Estéreo
        uncanal=sonido[:,canal]
    return(uncanal)

# PROGRAMA
# INGRESO
# archivo01 = input('archivo de sonido 01:' )
# archivo02 = input('archivo de sonido 02:' )
archivo01 = 'elaguacate_muestra01.wav'
archivo02 = 'elaguacate_muestra02.wav'

muestreo, sonido = waves.read(archivo01)
senal01 = extraeuncanal(sonido)

muestreo, sonido = waves.read(archivo02)
senal02 = extraeuncanal(sonido)

# PROCEDIMIENTO
tamano01 = len(senal01)
tamano02 = len(senal02)

# Normaliza las señales
amplitud = np.max(senal01)
senal01 = senal01/amplitud
senal02 = senal02/amplitud

# Correlación para comparar
correlacion = np.correlate(senal01,senal02, mode='same')

# SALIDA
# unifica dimensiones de señal01 y señal02
extra = np.abs(tamano01-tamano02)
relleno = np.zeros(extra,dtype=float)
senal01relleno = np.concatenate((senal01,relleno),axis=0)
plt.suptitle('Correlación(señal01,señal02)')

plt.subplot(311)
plt.plot(senal01relleno,'g', label = 'señal01')
plt.legend()

plt.subplot(312)
plt.plot(senal02,'b', label = 'señal02')
plt.legend()

plt.subplot(313)
plt.plot(correlacion,'m', label = 'correlación')
plt.legend()

plt.show()