
# coding: utf-8

# # Pandas Lab

# ### 1. Create a data series with marks of students : 75, 80, 79, 60

# In[45]:

import pandas as pd
pd.Series([75,80,79,60])


# ### 2. Create a data frame with name of students, id and marks

# In[46]:

pd.DataFrame({
        'name':['ali','ahmed','rashid'],
        'id':[101,102,103],
        'marks':[60,70,80]
    })


# ### 3. Now read the file 'data.csv' in panda

# In[47]:

data=pd.read_csv('data.csv')
data


# ### 4. What are the columns in the dataframe?

# In[48]:

data.columns


# ### 5. Sort the data based on Marks obtained. Fill all the 'na' cells with 0

# In[49]:

data=data.fillna(0)
data.sort_values(by=['Total (100)'])


# ### 6. Display the top 10 rows

# In[18]:

data.head(10)


# ### 7. Display the last 10 rows

# In[50]:

data.tail(10)


# ### 8. Display only the odd rows

# In[57]:

data.iloc[1::2]


# ### 9. Display only those students who got failed in examination

# In[59]:

cond = data['Assignment 1']==0
data[cond]


# ### 10. Find out the basic statistical info about data

# In[61]:

data.describe()


# ### 11. How many students got A, B, C, F?

# In[65]:

data.groupby(['Grade']).count()


# ### 12. What are the mean scores for students who got A, B, C, F?

# In[69]:

data.groupby(['Grade'])['Total (100)'].mean()


# In[ ]:



