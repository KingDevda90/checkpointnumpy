#!/usr/bin/env python
# coding: utf-8

# In[72]:


#2.Importation des donnees et creation du tableau grade
import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])


# In[73]:


#3.Utilisez les fonctions numpy pour calculer la moyenne, la médiane et l'écart type des notes.
#Moyenne
np.mean(grades)


# In[74]:


#mediane
np.median(grades)


# In[75]:


#Ecartype
np.std(grades)


# In[76]:


#4.Utiliser Numpy pour trouver le maximum et le minimum
#Le minimum
np.min(grades)


# In[77]:


#Le maximum
np.max(grades)


# In[78]:


#5.Utilisez la fonction numpy pour trier les notes par ordre croissant
np.sort(grades)


# In[79]:


#6.Utilisez la fonction numpy pour trouver l'index de la note la plus élevée du tableau.
np.argmax(grades)


# In[88]:


#7.Utilisez la fonction numpy pour compter le nombre d'élèves ayant obtenu un score supérieur à 90.
len(grades[grades>90])


# In[97]:


#8.Utilisez la fonction numpy pour calculer le pourcentage d'élèves ayant obtenu un score supérieur à 90.
pourcentage = (len(grades[grades>90])/len(grades))*100
pourcentage


# In[98]:


#9.Utilisez la fonction numpy pour calculer le pourcentage d'élèves ayant obtenu un score inférieur à 75.
pourcentage2 = (len(grades[grades<75])/len(grades))*100
pourcentage2


# In[100]:


#10.Utilisez la fonction numpy pour extraire toutes les notes supérieures à 90 et les placer dans un nouveau tableau appelé "high_performers".
high_performers = grades[grades>90]
high_performers


# In[102]:


#11. 
passing_grades = grades[grades>75]
passing_grades


# In[ ]:




