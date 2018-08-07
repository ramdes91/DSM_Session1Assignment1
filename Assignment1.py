
# coding: utf-8

# In[59]:


num=range(2000,3201)
op=[]
i=0
for i in num:
    if (i%7==0) and (i%5!=0):
        op.append(str(i))
        print(",".join(op))
        
    
        


# In[65]:


firstname = input("Input your First Name :")
lastname = input("Input your Last Name :")
print ("Reversename: " +lastname + " " +firstname)


# In[84]:


import math
r=6
volume= 4/3*math.pi*r**3
print('The volume of the sphere is',volume)

