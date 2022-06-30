import pandas as pd
import numpy as np
import os

path='G:/Mi unidad/Semestre 2022-0/Lab R y python/Trabajo_final'
os.chdir(path)

# PREGUNTA 3
#-----------

df=pd.read_excel("muestrac.xls")

# Revisión de la base
df.dtypes
df.columns
pd.isna(df).sum()
df.shape

# Ordenamiento de la base
df.sort_values("ingreso_total_corr", axis = 0, ascending = True,
                 inplace = True, ignore_index= True)

# Pregunta a)
#------------
'ingreso_total_corr'
# Tamaño muestral
cantidad= df.shape[0]
df=df.squeeze() # de DataFrame a Series

# Definición Función Coeficiente de Gini
# n= tamaño muestral; df = base de datos (Clase: Series)

def Coef_gini (n, df):
    # Sumatoria denominador (sum_Yi)
    sum_Yi= sum(df)

    # Sumatoria numerador (sum1)
    sum1=0
    i=1
    
    while i<=n:
            valor=(n+1-i)*df.iloc[i-1]
            sum1= sum1 + valor
            i = i+1
            
    # Cálculo coeficiente de Gini
    Gini= 1/n*(n+1-2*(sum1/sum_Yi))
    return Gini

# Coeficiente de Gini
       
print('El coeficiente de gini es ' + str(round(Coef_gini(cantidad,df),3)))

# Pregunta b)
#------------

columnas=np.arange(0,1000) # Es un numpy.ndarray

# Pregunta c)
#------------

# Creación DataFrame vacío
df1 = pd.DataFrame(columns=columnas)

# Pregunta d)
#------------

for i in range(1000):
    df1[i]=df.sample(n=1000, replace=True, random_state=i).tolist()
    # Muestra de 1000 observaciones con reemplazo. Luego lo covertimos a lista para
    # agregar los valores al DataFrame vacío
    
# Pregunta e)
#------------

gini_serie=[]
    
for i in range(1000):
    y=df1[i].squeeze().sort_values() # de DataFrame a Series y luego lo ordenamos
    gini_i=Coef_gini(1000,y)
    gini_serie.append(gini_i)
    
# Pregunta f): Cálculo de la varianza de 'gini_serie'
#---------------------------------------------------

# Cálculo de la media
mean = np.mean(gini_serie)

# Cálculo de la varianza
varianza=0
i=1
    
while i < len(gini_serie):
    valor=(gini_serie[i]-mean)**2/len(gini_serie)
    varianza= varianza + valor
    i = i+1

# Resultado final
print('La varianza de gini_serie es ' + str(round(varianza,4)))

# Pregunta g)
#------------

# Ordenamos la lista
gini_serie=sorted(gini_serie)

# Percentiles
from empiricaldist import Cdf
cdf_gini = Cdf.from_seq(gini_serie)

p1=cdf_gini.inverse(0.025)
print('El percentil 2.5% es ' + str(np.round(p1,3)))

p2=cdf_gini.inverse(0.975)
print('El percentil 97.5% es ' + str(np.round(p2,3)))