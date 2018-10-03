
# coding: utf-8

# In[3]:

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None


# In[8]:

g={}
g[1]=[3,4]
g[2]=[1,4]
g[3]=[]
g[4]=[3]


# In[9]:

g


# In[10]:

g[1]


# In[11]:

n=int(input('enter the node:'))


# In[17]:

ind=0
for k in g.keys():
    if n in g[k]:
        ind+=1
        
print(ind)


# In[18]:

print(len(g[n]))



# In[19]:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# In[20]:

graph


# In[33]:

stack=1
def push(s,e):
    s.insert(0,e)
    return s

def pop(s):
    if(len(s)==0):
        return null
    else:
        return s.pop(0)


# In[36]:

push(stack, 1)


# In[30]:




# In[37]:

push(stack,1)


# In[ ]:



