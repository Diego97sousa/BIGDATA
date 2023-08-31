#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

dicionario={'País':['Brasil','Uruguai','Bélgica','Inglaterra','Espanha','Holanda','Itália',
                    'Argentina','Alemanha','França','Croácia','Portugal','México','Japão','Suécia'],
           'Ano':[1958,1930,None,1966,2010,None,1934,1978,1954,1998,None,None,None,None,None],
           'Titulos':[5,2,0,1,1,0,4,3,4,2,0,0,0,0,0],
           'Participações':[22,14,14,16,16,11,18,18,20,16,6,8,18,7,12]
           }
dados = pd.DataFrame(dicionario)
display(dados)


# In[7]:


#exportar DataFrame para CSV.
dados.to_csv('copa.csv', index=False)


# In[9]:


#importar CSV
dados2 = pd.read_csv('copa.csv')
display(dados2)


# In[12]:


#Exportar a coluna 'País' para um objeto Series

paises = dados['País']

display(paises)


# In[14]:


#Series a usar
continentes = pd.Series(['America do Sul','America do Sul','Europa','Europa','Europa','Europa','Europa','America do Sul','Europa','Europa','Europa','Europa','America do Sul','Ásia','Europa','Europa','America do Sul'])

#Importar o series como coluna nova no df:
dados2['Continente'] = continentes

#Visualizar DataFrame
display(dados2)


# In[16]:


# 5 primeiras linhas
print(dados2.head())
print()
# 5 últimas linhas
print(dados2.tail())


# In[17]:


#Método 1: Usando 'isna()'
linhas_nulas = dados2[dados2['Ano'].isna()]

#Método 2: Usando 'isnull()'
linhas_nulas = dados2[dados2['Ano'].isnull()]

print(linhas_nulas)


# In[18]:


#Filtrar as linhas com valor 0 na coluna 'Titulos'
paises_sem_titulo = dados2[dados2['Titulos'] ==0]

print(paises_sem_titulo[['País','Titulos']])


# In[22]:


#Identificar o pais com o maior número de titulos
pais_mais_titulos = dados2.loc[dados2['Titulos'].idxmax()]['País']
max_titulos = dados2['Titulos'].max()

#Identificar o pais com maior número de participações
pais_mais_participacoes = dados2['Participações'].max()
max_participacoes = dados2['Participações'].max()

print(f"País com mais titulos: {pais_mais_titulos} {max_titulos} titulos")
print(f"País com mais participações: {pais_mais_participacoes} ({max_participacoes} Particpações)")


# In[23]:


#Criar ranking com base no número de titulos
dados2['Ranking_Titulos'] = dados2['Titulos'].rank(ascending=False, method='min')

#Criar ranking com base no número de participações
dados2['Ranking_Participacoes'] = dados2['Participações'].rank(ascending=False, method='min')

print(dados2[['País','Ranking_Titulos','Ranking_Participacoes']])


# In[24]:


#1. Filtro com query()

#Filtrar os países que ganharam mais de um título usando query()
paises_com_mais_de_um_titulo = dados.query('Titulos > 0')

print(paises_com_mais_de_um_titulo)


# In[25]:


#2. indexação booleana

#Filtrar os paises que ganharam mais de um titulo usando indexação booleana
paises_com_mais_de_um_titulo = dados[dados['Titulos'] > 0]

print(paises_com_mais_de_um_titulo)


# In[ ]:




