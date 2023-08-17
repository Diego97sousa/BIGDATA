#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Criar Objeto Serie vazio
import pandas as pd
serie = pd.Series()
print(serie)


# In[4]:


#Criar um objeto tipo series apartir de uma lista python
import pandas as pd

dados = pd.Series([12, 34, 21, -9, 7])
print(dados)


# In[5]:


#Series com array NumPy
import numpy as np
array_numpy = np.array([10, 20, 30, 40, 50, 60])
dados = pd.Series(array_numpy)
print(dados)


# In[7]:


#Series com repetição de itens
import pandas as pd
serie = pd.Series(33, index = ["num1", "num2", "num3", "num4", "num5"])
print(serie)


# In[9]:


#Series com dicionário
import pandas as pd
dicionario = {
    'Ano' : 1950,
    'Item' : 'TV,',
    'Preço' : 250.60
}
serie = pd.Series(dicionario)
print(serie)


# In[10]:


#Outro dicionário
import pandas as pd
dicionario = {'Brasil' : 5, 'EUA' : 0, 'Inglaterra' : 1, 'Argentina' : 3}
serie = pd.Series(dicionario)
print(serie)


# In[14]:


# print(dados.values) mostra apenas os valores
# print(dados.index) mostra apenas o indice

import pandas as pd
dicionario = {'Brasil' : 5, 'EUA' : 0, 'Inglaterra' : 1, 'Argentina' : 3}
serie = pd.Series(dicionario)
print(serie)


# In[17]:


#indices personalizados
import pandas as pd
dados = pd.Series([12, 34, 21, -9, 0, 7], index= ['a', 'b', 'c', 'd', 'e', 'f'])
print(dados)
#Olhar os valores atraves dos indices
print('Dado no indice c: ', dados['c'])
print('\nIndices b e e:')
print(dados[['b','e']])


# In[20]:


#Acessar um item
import pandas as pd
serie = pd.Series ([10, 20, 30, 40, 50], index = ["num1", "num2", "num3", "num4", "num5"])
print('Item na posição 0:', serie[0])
print('Item de indice num3' , serie['num3'])


# In[36]:


#Para identificar o maior ou menor valor
import pandas as pd
serie = pd.Series([5, 7, 12, 2, 1, 6, 7, 0, -3, 22])
print(f'Menor valor: {serie.min()}')
print(f'Valor mais alto: {serie.max()}')


# In[49]:


#Para obter o indice associado ao maior valor usamos o método .idxmax():
import pandas as pd

serie = pd.Series([5, 7, 12, 2, 1, 6, 7, 0, -3, 22])
print(f'Valor mais alto: {serie.max()}')
print(f'Indice do maior valor: {serie.idxmax()}')
print(f'Indice do maior valor: {serie.idxmix()}')

print(f'Média aritmetica: {serie.mean()}')

print(f'Mediana dos valores: {serie.median()}')

print(f'Somatorio dos valores: {serie.sum()}')


# In[39]:


#Podemos converter um objeto Series em uma lista comum do Python com o médtodo .tolist()
import pandas as pd
serie = pd.Series([5, 7, 12, 2, 1, 6, 7, 0, -3, 22])
print(serie)
lista = serie.tolist()
print(lista)


# In[40]:


#mostrar os lementos ordenados por valores de indice: método .sort_index()
import pandas as pd
dicionario = {'Brasil' : 5, 'EUA' : 0, 'Inglaterra' : 1, 'Argentina' : 3}
dados = pd.Series(dicionario)
print(dados.sort_index())
 


# In[43]:


#mostrar os lementos ordenados por valores de indice: método .sort_index()
import pandas as pd
dicionario = {'Brasil' : 5, 'EUA' : 0, 'Inglaterra' : 1, 'Argentina' : 3}
dados = pd.Series(dicionario)
print(dados.sort_values()) 


# In[ ]:


'Austria': 9006398,
   'Alemanha': 83289318,
   'Bélgica': 11589623,
   'Bulgária': 7000039,
   'Chipre': 1207361,
   'Croácia': 4076246,
   'Dinamarca': 5806015,
   'Eslováquia': 5459642,
   'Eslovênia': 2095861,
   'Espanha': 47351567,
   'Estônia': 1324820,
   'Finlândia': 5523231,
   'França': 66977107,
   'Grécia': 10423056,
   'Hungria': 9775564,
   'Irlanda': 4882495,
   'Itália': 60233948,
   'Letônia': 1906743,
   'Lituânia': 2793471,
   'Luxemburgo': 613894,
   'Malta': 493559,
   'Países Baixos': 17134872,
   'Polônia': 37974750,
   'Portugal': 10286263,
   'República Tcheca': 10693939,
   'Romênia': 19405156,
   'Suécia': 10106005,

