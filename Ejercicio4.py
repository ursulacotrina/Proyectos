#EJERCICIO 4

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import scipy.stats as ss
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statistics import mean

# Pregunta a

Beta = [1 ,2, 10]

# Pregunta b 
np.random.seed(3767342)
n=1000

x1= np.random.uniform(0,1,n)

x2 =np.random.binomial(1, 0.3, n)

e = np.random.normal(0,1,n)

plt.hist(x1, color = '#F2AB6D', rwidth = 0.9)
plt.title('Histograma de x1')
plt.show()

plt.hist(x2, color = 'BLUE', rwidth = 0.9)
plt.title('Histograma de x2')
plt.show()

plt.hist(e, color = 'pink')
plt.title('Histograma del error')
plt.show()

# Preguntas c) y d)
'''
df_x11 --> variable x1 cuando n=5
df_x12 --> variable x2 cuando n=5
df_e1 --> variable e cuando n=5
y1 --> variable y cuando n=10

df_x21 --> variable x1 cuando n=10
df_x22 --> variable x2 cuando n=10
.
.
.
df_x14 --> variable x1 cuando n=1000
df_x14 --> variable x2 cuando n=1000
df_e4 --> variable e cuando n=1000
y4 --> variable y cuando n=1000

'''

fila=[5,10,100,1000]

for j in range(1,5):
    globals()[f'df_x1{j}']=pd.DataFrame()
    globals()[f'df_x2{j}']=pd.DataFrame()
    globals()[f'df_e{j}']=pd.DataFrame()
    
    for i in range(10000):
        globals()[f'df_x1{j}'][i]= np.random.uniform(0,1,fila[j-1]).tolist()
        globals()[f'df_x2{j}'][i]= np.random.binomial(1,0.3,fila[j-1]).tolist()
        globals()[f'df_e{j}'][i]= np.random.normal(0,1,fila[j-1]).tolist()
        
    globals()[f'y{j}'] = Beta[0] +globals()[f'df_x1{j}']*Beta[1] + globals()[f'df_x2{j}']*Beta[2] + globals()[f'df_e{j}']
    globals()[f'media{j}']=globals()[f'y{j}'].mean()
   
    plt.hist(globals()[f'media{j}'], color = 'pink', rwidth = 0.9 )
    plt.title('Histograma de media muestra n=' + str(fila[j-1]))
    
    globals()[f'promedio_{j}'] = globals()[f'media{j}'].mean()
    globals()[f'varianza_{j}'] = globals()[f'media{j}'].var()
    globals()[f'maximo_{j}'] = globals()[f'media{j}'].max()
    globals()[f'minimo_{j}'] = globals()[f'media{j}'].min()
    
    globals()[f'tab{j}'] = pd.DataFrame([globals()[f'promedio_{j}'],globals()[f'varianza_{j}'],globals()[f'maximo_{j}'],globals()[f'minimo_{j}']])
    
    
tabla_estadistica = np.concatenate((tab1,tab2,tab3,tab4), axis = 1)
tabla_estadistica = pd.DataFrame(tabla_estadistica)

tabla_estadistica.rename(columns={0:'N=5', 1:'N=10', 2:'N=100', 3:'N=100'},
                         index={0:'Promedio', 1:'Varianza', 2:'Maximo', 3: 'Minimo'})

print('Se puede observar que la varianza va disminuyendo a medida que n aumenta')

'''El promedio de las cuatro muestras no varía considerablemente, solo hay un pequeño cambio significativo
    entre la muestra N=5 con N=10. Sin embargo, la diferencia entre el promedio de las muestras:
    N=10, N=100 y N=1000 no es significativa.
- Por el lado de la varianza, se puede ver una reducción considerable entre la primera 
    y las demás muestras.
- En el caso del número máximo, nos damos cuenta de que disminuye mientras se aumenta la muestra.
    Y, esto, se debe probablemente a que hay un mayor margen para la elección de números aleatorios.
- Y, por último, en el caso del número mínimo, en la tabla podemos notar que mientras aumenta el 
    número de muestra, el número mínimo se incrementa. Lo que causa que en la muestra mayor: N=100,
    el número máximo y el número mínimo tienen menos diferencia que el número máximo y el número 
    mínimo de la muestra N=5'''

# Pregunta e)

for j in range(1,5):
    globals()[f'Beta0_{j}']=[]
    globals()[f'Beta1_{j}']=[]
    globals()[f'Beta2_{j}']=[]
    
    for i in range(10000):
        
        x=pd.concat([globals()[f'y{j}'].iloc[:,i],globals()[f'df_x1{j}'].iloc[:,i],globals()[f'df_x2{j}'].iloc[:,i]],axis=1)
        x.columns = [ 'Y', 'X1' , 'X2']
        resultados1=smf.ols('Y ~ X1+X2', data=x).fit()
        #resultados1.summary()
        globals()[f'Beta0_{j}'].append(resultados1.params[0])
        globals()[f'Beta1_{j}'].append(resultados1.params[1])
        globals()[f'Beta2_{j}'].append(resultados1.params[2])
        
# Gráfico de histogramas
 
for j in range (1,5):
    plt.hist(globals()[f'Beta0_{j}'], color = 'green', rwidth = 0.9 )
    plt.title('Histograma de Beta0 n=' + str(fila[j-1]))
    plt.show()

for j in range (1,5):
    plt.hist(globals()[f'Beta1_{j}'], color = 'pink', rwidth = 0.9 )
    plt.title('Histograma de Beta1 n=' + str(fila[j-1]))
    plt.show()
   
for j in range (1,5):  
    plt.hist(globals()[f'Beta2_{j}'], color = 'red', rwidth = 0.9 )
    plt.title('Histograma de Beta2 n=' + str(fila[j-1]))
    plt.show()
    
a= mean(Beta2_4) - Beta[2]
b= mean(Beta1_4) - Beta[1]

print('Se observa que a medida el tamaño muestra aumenta, la distribución converge a una distribución normal')
print('Se puede observar que los estimadores convergen a los valores poblaciones cuando n es cada vez más grande')
''' Una forma de reducir el error, es reducir la varianza o aumentar el tamaño de la muestra'''

