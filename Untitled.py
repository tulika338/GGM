#!/usr/bin/env python
# coding: utf-8

# ### ~~*Harry Potter Trivia*~~

# ### *Loops*

# In[2]:


Houses=["Gryffindor","Gryffindor","Gryffindor","Gryffindor","Slytherin","Slytherin","Slytherin","Slytherin","Slytherin","Ravenclaw","Slytherin","Gryffindor","Slytherin","Hufflepuff","Gryffindor","Hufflepuff","Hufflepuff","Hufflepuff","Ravenclaw","Ravenclaw","Ravenclaw","Ravenclaw","Ravenclaw","Hufflepuff","Hufflepuff","Gryffindor","Ravenclaw","Ravenclaw","Ravenclaw"]
Lion=[]
i=0
while(Houses[i]=="Gryffindor"):
    Lion.append(Houses[i])
    i=i+1
print(Lion)


# In[4]:


Houses=["Gryffindor","Gryffindor","Gryffindor","Gryffindor","Slytherin","Slytherin","Slytherin","Slytherin","Slytherin","Ravenclaw","Slytherin","Gryffindor","Slytherin","Hufflepuff","Gryffindor","Hufflepuff","Hufflepuff","Hufflepuff","Ravenclaw","Ravenclaw","Ravenclaw","Ravenclaw","Ravenclaw","Hufflepuff","Hufflepuff","Gryffindor","Ravenclaw","Ravenclaw","Ravenclaw"]
Eagle=[]
i=0
while(Houses[i]=="Ravenclaw"):
    Eagle.append(Houses[i])
    i=i+1
print(Eagle)


# ### *Functions*

# In[12]:


def Add3(a):
    b=a+3
    return b


# In[13]:


Add3(4)


# In[15]:


def Multiply3(a):
    b=3*a
    return b


# In[18]:


Multiply3("Harry Potter ")


# #### (Present value of Cash Flows)

# In[26]:


def discount_factor(interest_rate,number_of_periods):
    dis_factor=1/pow((1+interest_rate),number_of_periods)
    return dis_factor


# In[27]:


discount_factor(0.067,5)


# In[37]:


def Present_Value_of_CF(cash_flow,dis_factor):
    PV=cash_flow*dis_factor
    return PV


# In[38]:


Present_Value_of_CF(100,discount_factor(0.055,6))


# In[50]:


Cash_Flows=[-119,200.88,168.34,72.99,50.11,486.10,389,255.5433,670,356,776]
Holding_period=6
for n in range(0,7):
    PV=Present_Value_of_CF(Cash_Flows[n],discount_factor(0.05,n))
    print(PV)
    n=n+1


# #### (Gordon Growth Model)

# In[64]:


def Dividend(payout_percentage,earnings):
    Dividend=(payout_percentage/100)*earnings
    return Dividend


# In[65]:


Dividend(45,670)


# In[67]:


payout_percentage=[40,36,32,25,30,41]
earnings=[300,276,258.65,242.78,290.58,310]
for n in range(0,6):
    Dividends=Dividend(payout_percentage[n],earnings[n])
    print(Dividends)
    n=n+1


# In[75]:


def GGM(Dividend,interest_rate,growth_rate,number_of_periods):
    Dividend=Dividend(payout_percentage,earnings)
    Intrinsic_Value=Dividend/(pow(((interest_rate-growth_rate)/100),number_of_periods))
    return Intrinsic_Value


# In[79]:


GGM(Dividend(6,550),5,4,7)


# In[ ]:




