#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('file(3).csv',sep=',')


# In[3]:


df.head()


# In[5]:


df.isnull().sum()


#  Show the number of Confirmed, Deaths and Recovered cases in each Region.
#  

# In[6]:


df[['Region','Confirmed','Deaths','Recovered']]


# Remove all the records where the Confirmed Cases is Less Than 10.

# In[7]:


mask=df['Confirmed']<10
df=df[~mask]


# In[8]:


df.head()


# In which Region, maximum number of Confirmed cases were recorded ?

# In[15]:


df.groupby('Region').Confirmed.max().sort_values(ascending=False)


# In which Region, minimum number of Deaths cases were recorded ?

# In[17]:


df.groupby('Region').Confirmed.min().sort_values(ascending=True)


# In[19]:


df.groupby('Region').get_group('Morocco')


#  How many Confirmed, Deaths & Recovered cases were reported from Morocco till 29 April 2020 ?

# In[24]:


df[df.Region=='Morocco']


# Sort the entire data wrt No. of Confirmed cases in ascending order.

# In[43]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[38]:


sort=df.sort_values(by=['Confirmed'],ascending = True)
sns_sorted=sort.head(10)


# In[45]:


sns.boxplot(x="Confirmed", y="Region", data=sns_sorted, palette="Set3", width=0.6)
plt.title("Boxplot of least 10 Confirmed by Region")
plt.xlabel("Confirmed")
plt.ylabel("Region")
plt.show()


# Sort the entire data wrt No. of Recovered cases in descending order.

# In[35]:


sorted =df.sort_values(by=['Recovered'],ascending = False)
sns_sort=sorted.head(10)


# In[44]:


sns.boxplot(x="Recovered", y="Region", data=sns_sort, palette="Set3", width=0.6)
plt.title("Boxplot of Top 100 Recovered by Region")
plt.xlabel("Recovered")
plt.ylabel("Region")
plt.show()

