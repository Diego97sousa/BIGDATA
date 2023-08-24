#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

dados = {
    'Nome': ['Fabio', 'Ana', 'Ricardo', 'Daniela'],
    'Idade': [45, 30, 22, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Recife']
}
df = pd.DataFrame(dados)
print(df)


# In[30]:


import pandas as pd
dicionario = {
    'Pais': ['Brasil','Uruguai','Inglaterra','Espanha','Holanda','Italia','Argentina','Alemanha','França'],
    'Ano':[1958,1930,1966,2010,None,1934,1978,1954,1998],
    'Titulos':[5,2,1,1,0,4,3,4,2]
}
dados = pd.DataFrame(dicionario)
print(dados)

# 5 Primeiras Linhas
print(dados.head())

#5 Ultimas linhas
print(dados.tail())

#Alterar ordem das colunas
dados = pd.DataFrame(dados, columns=['Titulos','Pais','Ano'])
print(dados)

#Ver Nomes das colunas
print(dados.columns)

#para imprimir colunas individuais
print('Paises:')
print(dados['Pais'])
print('\nAluno:')
print(dados.Ano)

#Acrescentar uma coluna ao DataFrama:
dados['Participações'] = 0
print(dados)

#Preencher a Coluna com valores de uma lista:
part = [22,14,16,16,11,18,18,20,16]
dados['Participações'] = part
print(dados)

#Excluir coluna "Participações"
del dados['Participações']
print(dados)

#Excluir a linha 4 (Holanda) (dados2 é uma cópia de dados)
dados2 = dados.drop([4])
print(dados2)

#Excluir as linhas 4,3,5 de uma vez
dados2 = dados.drop([4, 3, 5])
print(dados2)

#Excluir Linhas In Loco (Propia tabela)
dados.drop(4, inplace=True)
print(dados)

#Retornar Linhas de 1 a 5
print(dados[1:5])

#Indexação com Loc (Localização por nome de indice)
#Linha b, colunas de País e Titulos
print(dados.loc['b',['Pais', 'Titulos']])

#Linhas de a a b, coluna de ano.
print(dados.loc[:'d', 'Ano'])


# In[31]:


#Fatiamento com rotulos

import pandas as pd
dicionario = {
    'Pais': ['Brasil','Uruguai','Inglaterra','Espanha','Holanda','Italia','Argentina','Alemanha','França'],
    'Ano':[1958,1930,1966,2010,None,1934,1978,1954,1998],
    'Titulos':[5,2,1,1,0,4,3,4,2]
}
dados = pd.DataFrame(dicionario, index=['a','b','c','d','e','f','g','h','i'])
#Mostra df completo
print(dados, '\n')
#Mostra apenas Linhas de rotulos b até e:
print(dados['b':'e'])

#indexação com iloc
print(dados.iloc[1,[0,2]])


# In[33]:


#Ordenação por indice
print(dados.sort_index())
print()
#Ordenação por indice em ordem inversa
print(dados.sort_index(ascending=False))


# In[34]:


#Ordenação por colunas: ordem alfabetica de pais
print(dados.sort_values(by='Pais'))


# In[35]:


#Ordem alfabetica inversa
print(dados.sort_values(by='Pais', ascending=False))


# In[37]:


#Ordenação por varias colunas: ordem crescente de titutlos e alfabetica de paises:
print(dados.sort_values(by=['Titulos','Pais']))


# In[38]:


# OU ainda ordem decrescente de titulos e alfabetica de paises:
#Ordenação por varias colunas
print(dados.sort_values(by=['Titilos','Pais'], ascending = [False, True]))


# In[ ]:




