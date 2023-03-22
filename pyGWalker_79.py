#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyGWalker


# In[2]:


import pandas as pd
import pygwalker as pyg


# In[23]:


df = pd.read_excel("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\US Superstore data.xls")


# In[32]:


df.head()


# Exploratory Data Analysis

# In[33]:


#row,column count of data
df.shape


# In[34]:


#column names of table
df.columns


# In[35]:


#check data type of columns/attributes
df.dtypes


# Checking for missing values in data

# In[36]:


df.isnull().sum()


# Check for unnecessary columns and drop them if not required
# 
# 'Row ID' column is nothing but the serial number so we can drop this column.

# In[31]:


#dropping Country column
df=df.drop('Country',axis=1)
df.head()


# In[37]:


#number of products in each sub-category
df['Sub-Category'].value_counts()


# In[38]:


df['Product Name'].value_counts()


# In[40]:


df['Cost']=df['Sales']-df['Profit']
df['Cost'].head()


# In[41]:


df['Profit %']=(df['Profit']/df['Cost'])*100


# In[43]:


#Profit Percentage of first 5 product names
df.iloc[[0,1,2,3,4],[14,20]]


# In[44]:


#Products with high Profit Percentage 
df.sort_values(['Profit %','Product Name'],ascending=False).groupby('Profit %').head(5)


# In[45]:


#Top 10 customers who order frequently
df_top10=df['Customer Name'].value_counts().head(10)
df_top10


# In[47]:


pyg.walk(df)


# # # Sales of the store were highest in 2016.

# In[29]:


pyg.walk(df)


# # Highest profit is earned in Copiers while Selling price for Chairs and Phones is extremely high compared to other products.
# 
# It is also evident that people dont prefer to buy Tables and Bookcases from Superstore. Hence these departments are in loss.
# 

# In[46]:


pyg.walk(df)


# # People residing in Western part of US tend to order more from superstore.
# 

# In[25]:


pyg.walk(df)


# # The distribution is highest in Consumer Segment.

# In[48]:


pyg.walk(df)


# # We see that majority of the Profitable Customers are from New York and Michigan State.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




