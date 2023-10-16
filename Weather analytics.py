#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('file.csv',sep=',')


# # Analysis of Dataframe

# In[2]:


df.head()


# In[3]:


df.describe()


# In[4]:


df.columns


# In[5]:


df.index


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


df['Temp_C'].unique()


# In[9]:


df.nunique()


# In[10]:


df.count()


# In[11]:


df['Weather'].value_counts()


# In[12]:


df.info()


# In[13]:


df['Date/Time']=pd.to_datetime(df['Date/Time'])


# In[14]:


df.info()


# In[15]:


df.head()


# In[16]:


df['Wind Speed_km/h'].unique()


# In[17]:


df['Weather'].value_counts()


# In[18]:


df.groupby('Weather').get_group('Clear')


# In[19]:


df.groupby('Wind Speed_km/h').get_group(4)


# In[20]:


df.isnull().sum()


# In[21]:


df=df.rename(columns={'Weather':'Weather Condition'})


# In[22]:


df.head()


# In[23]:


df.describe()


# In[26]:


mean_visibility = df['Visibility_km'].mean()
print("Mean Visibility (km):", mean_visibility)


# In[27]:


df.Press_kPa.std()


# In[31]:


df['Rel Hum_%'].var()


# In[33]:


df.groupby('Weather Condition').get_group('Snow')


# In[35]:


df[df['Weather Condition'].str.contains('Snow')]


# In[39]:


df[(df['Wind Speed_km/h'] > 24 ) & (df['Visibility_km']==25)]


# In[40]:


df.groupby('Weather Condition').mean()


# In[43]:


min=df.groupby('Weather Condition').min()
max=df.groupby('Weather Condition').max()

print(min,max)


# In[44]:


df.head()


# In[47]:


df.groupby('Weather Condition').get_group('Fog')


# In[54]:


df[(df['Weather Condition']=='Clear') |  (df['Visibility_km']>40) | (df['Visibility_km']>40)]


# In[55]:


df[(df['Weather Condition']=='Clear') & (df['Rel Hum_%']>50) | (df['Visibility_km']>40)]


# In[52]:


df[(df['Visibility_km']>40)

