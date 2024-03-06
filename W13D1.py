#!/usr/bin/env python
# coding: utf-8

# Abbiamo 25 studenti; memorizzare questo dato in una variabile. Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile. Creare un'altra variabile ancora che conterrà la somma delle prime due, poi stamparla a video.

# In[2]:


students=25


# In[3]:


print(students)


# In[76]:


additional_students=3
Total_Students=y=students+additional_students
print(y)


# In[9]:


school="Epicode"


# In[10]:


print(school)


# Abbiamo la variabile:
# 
# x = 10 Incrementarla di 2 e poi moltiplicarla per 3 Usare due metodi diversi (ad esempio, uno utilizzando gli operatori di assegnazione, e uno senza)

# In[33]:


x=10
x_cal=(x+2)*3


# In[34]:


print(x_cal)


# method 2 by assigning variables.

# In[15]:


x=10
a=2
b=3


# In[35]:


x_cal2=(x+a)*b


# In[36]:


print(x_cal2)


# **Esercizio** 
# 
# 
# Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è compreso tra 5 e 8:

# In[19]:


str1 = "Windows"
str2 = "Excel" 
str3 = "Powerpoint" 
str4 = "Word"


# In[70]:


print("lengths:",len(str1),len(str2),len(str3),len(str4))


# In[72]:


print(len(str1)>5 <8)
print(len(str2)>5 <8)
print(len(str3)>5 <8)
print(len(str4)>5 <8)


# Calcolare e stampare a video quanti secondi ci sono in un anno non bisestile.

# In[38]:


year=365 #days
day=24 #hours
minutes=60 
hour=60 #seconds


# In[43]:


one_year=year*day*minutes*hour
print(one_year,"seconds in an year")


# **Assigning variables to count number of seconds in # years**

# In[59]:


years=y=2
days_in_one_year=d=365
hours_in_a_day=h=24
minutes_in_an_hour=m=60
seconds_in_a_minute=s=60
Total=y*d*h*m*s


# In[60]:


print( "There are", Total,"seconds in", y, "years")


# Esercizio Abbiamo la seguente stringa: 
# **my_string = "I am studying Python"**
# * Trasformarla in modo che tutti i caratteri siano maiuscoli (uppercase) 
# * Trasformarla in modo che tutti i caratteri siano minuscoli (lowercase) 
# * Sostituire la sottostringa "Python" con la stringa "a lot" 
# * Usare il metodo .strip(); cambia qualcosa? Perché?Esercizio Abbiamo la seguente stringa: my_string = "I am studying Python" • Trasformarla in modo che tutti i caratteri siano maiuscoli (uppercase) • Trasformarla in modo che tutti i caratteri siano minuscoli (lowercase) • Sostituire la sottostringa "Python" con la stringa "a lot" • Usare il metodo .strip(); cambia qualcosa? Perché?

# In[61]:


my_string = "I am studying Python"


# In[75]:


print("maiuscoli:", str.upper(my_string))
print("maiuscoli:", str.lower(my_string))
print("Replace:", my_string.replace("Python","a lot"))
print("strip:", my_string.strip())


# In[ ]:




