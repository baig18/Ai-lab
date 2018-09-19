
# coding: utf-8

# In[1]:

print("Noman Baig")


# In[4]:

for i in range(1,101):
 print(i)


# In[13]:

year =int(input("Enter Year:")) 
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("This is a leap year")
       else:
           print("This is not a leap year")
   else:
       print("This is a leap year")
else:
   print("This is not a leap year")


    


# In[15]:

s="Noman Baig"
s=[1:3]


# In[19]:

x="Hello World"
x=[-1::-1]
print(x)


# In[17]:

x="Hello world"


# In[18]:

x=[-1::-1]


# In[21]:

Name= "Noman Baig"
x=Name[-1::-1]
print(x)


# In[23]:

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
print("Letters", l)
print("Digits", d)


# In[27]:

l= [Noman Baig]
for i in l
print(i)


# In[32]:

alphabet = "N o m a n"
data = alphabet.split() 

for temp in data:
    print(temp)


# In[35]:

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print (b,':',students[a][b])


# In[ ]:




# In[ ]:



