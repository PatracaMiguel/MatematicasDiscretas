#!/usr/bin/env python
# coding: utf-8

# # Teoria de conjuntos
# 
# La teoría de conjuntos es una rama de la lógica-matemática que se encarga del estudio de las relaciones entre entidades denominadas conjuntos. Los conjuntos se caracterizan por ser colecciones de objetos de una misma naturaleza. Dichos objetos son los elementos del conjunto y pueden ser: números, letras, figuras geométricas, palabras que representan objetos, los objetos mismos y otros
# 

# ## Creacion de conjuntos
# En python, puedes crear un conjunto utilizando llaves {} o la funcion set ()

# In[ ]:


A = {1,2,3,4,5}


# In[3]:


B = {3,4,5,6,7}


# In[4]:


C = set([3,6,9,12,15])


# ## Listas vs Conjuntos                                                                                                       

# In[7]:


lista = [1,2,3,4.5,1,2,3,4,5]


# In[8]:


lista


# In[9]:


conjunto = set(lista)


# In[10]:


conjunto


# # Operaciones
# 
# python proporciona operadores y metodos para realizar operaciones básicas de conjuntos como union,diferencia y diferencia simetrica 

# # Unión 
#  La operación de unión en teoria de conjuntos 
#  
#  $$
#      C = A \cup B = {x:x \in A \quad o \quad x \in B}
#  $$
#  
#  En pyton, la operación de unión puede ralizarse utilizando eñ operador | o el método unión 

# In[12]:


A | B


# In[13]:


A.union(B)


# # Intersección 
# Siempre que hablamos de la intersección entre dos conjuntos, significa un conjunto resultante que contiene todos los elementos comunes entre estos dos conjuntos. Alternativamente, también podemos decir que contiene todos los elementos de un conjunto que también pertenecen al otro conjunto.
# 
# Formalmete 
# $$
#    A \cup B
# $$
# En python  se puede hacer la intersección con el comando set1.intersection(set2)

# In[15]:


A.intersection(B)


# # Diferencia 
# La diferencia de conjuntos es una operación matemática que se realiza entre dos conjuntos, donde se obtiene un nuevo conjunto formado por los elementos que están en el primer conjunto pero no en el segundo 
# Formalmente
# $$
# [ A \setminus B ]
# $$
# 
# En python se puede hace la intersección con el comando set1.symmetric_difference(set2)

# In[16]:


A.symmetric_difference(B)


# # Diferencia simétrica
# 
# La diferencia simétrica de dos conjuntos es una operación en teoría de conjuntos que resulta en otro conjunto. Este conjunto contiene todos los elementos que pertenecen a cada uno de los conjuntos iniciales, pero no a ambos al mismo tiempo
# Formalmente
# 
# $$
#     A \triangle B
# $$
# 
# En python utilizamos el comando set_A.symmetric_difference(set_B)

# In[18]:


A - B


# In[17]:


A.symmetric_difference(B)


# In[19]:


B - A


# # Diagrama de Venn
# 
# Un diagrama de Venn es un tipo de gráfico formado por círculos superpuestos. Cada círculo representa un concepto o grupo de datos diferente y las secciones superpuestas representan sus cualidades compartidas. Esto hace que los diagramas de Venn sean una herramienta excelente para comparar datos y medir la probabilidad
# 
# ![DiagramadeVennde3Conjuntos.png](attachment:DiagramadeVennde3Conjuntos.png)
# 
# 

# In[37]:


pip install matplotlib_venn


# In[44]:


import matplotlib.pyplot as plt
import matplotlib_venn as venn


# In[45]:


from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# Tamaño relativo de los subconjuntos: (Ab, aB, AB)
venn2((1, 1, 1))

# Mostrar el diagrama
plt.show()


# In[ ]:




