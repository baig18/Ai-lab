
# coding: utf-8

# In[1]:

g={}
g[1]=[3,4]
g[2]=[1,4]
g[3]=[]
g[4]=[3]


# In[2]:

g


# In[3]:

g[1]


# In[8]:

stack=[]
def push(s,e):
    if e in s:return
    s.insert(0,e)
   
def pop(s):
    if(len(s)==0):
        return null
    else:
        return s.pop(0)

def empty(s):
    return len(s)==0


# In[16]:

push(stack,1)


# In[11]:

while empty(stack)==False:
    e=pop(stack)
    print(e)
    for k in g[e]:
        push(stack,k)


# In[15]:

X= "NOMAN BAIG"
print(X)


# In[ ]:



