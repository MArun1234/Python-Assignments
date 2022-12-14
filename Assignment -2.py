#!/usr/bin/env python
# coding: utf-8

# # Assignment - 2
# 

# In[ ]:


get_ipython().set_next_input('Q1. What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
Ans.

The two values of the Boolean data types are 'True' & 'False'
'True' is indicated with the value 1 & 'False' is indicated with the value 0

Boolean data type is mainly used to compare the things in Python 
if the comparision condition is ssatisified then it willl print 'True' or else it will print 'False'


Example:
x = 5
y = 10
print(bool(x==y))
#in the above example we are checking whether x is equal to y
if its yes it will print 'True' and since clearly those two are  not equal it will print 'False' 


# In[ ]:





# In[ ]:


Q2. What are the three different types of Boolean operators

Ans. 
The three basic boolean operators are: AND, OR, and NOT

AND searches find all of the search terms. 
OR searches find one term or the other.  
NOT eliminates items that contain the specified term


# In[ ]:





# In[ ]:


Q3. Make a list of each Boolean operator&truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

Ans:
    Combinations with ' AND'
    
True and True is True. 1 and 1 is 1
True and False is False , 1 and 0 is 0
False and True is False , 0 and 1 is 0,
False and False is False , 0 and 0 is 0,

Combinations with 'OR
'
True or True is True, 1 or 1 is 1
False or True is True, 0 or 1 is 1
False or False is False,0 or 0 is 0

Combinations with 'NOT'

not True is False, not 1 is 0
not False is True, not 0 is 1


Truth table for And is 

A B output
0 0 0
0 1 0 
1 0 0
1 1 1

Truth table for or is 

A B output
0 0 0
0 1 1 
1 0 1
1 1 1


Truth table for not is 

A output
0 1
1 0
 


# In[ ]:


get_ipython().set_next_input('Q4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')


# In[2]:



print((5>4) and (3==5))
print(not(5>4))
print((5>4) or (3==5))
print(not(5>4) or (3==5))
print((True and True) and (True==False))
print((not(False))or(not(True)))


# In[ ]:


get_ipython().set_next_input('Q5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans. 
 ==, !=, <, >, <=, and >= are the six comparison operators


# In[ ]:


Q6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
Ans. 

== is the equal to operator that compares two values and evaluates to a Boolean, 
while = is the assignment operator that stores a value in a variable.


# In[ ]:





# In[ ]:


Q&. 
Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs') 
if spam > 5:
print('bacon') 
else:
print('ham') 
print('spam')
print('spam')


# In[3]:


spam = 0
if spam == 10:
    print('eggs') #Block 1
if spam > 5:
    print('bacon') #Block 2
else:
    print('ham') #Block 3
    print('spam')
    print('spam')


# In[ ]:


Q8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
Ans :


# In[4]:


spam = int(input("Input a no."))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
        
        


# In[ ]:


get_ipython().set_next_input('Q9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans. 
If program is stuck in endless loop we will press ctrl+c, to exit the endless loop.


# In[ ]:


get_ipython().set_next_input('Q10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
Ans:


# In[5]:


# use of break
for i in range(10):
    if(i==7):
        break
    print(i)
    
print('Breaked')
#use of  continue
for i in range(10):
    if(i==7):
        continue
    print(i)
    


# In[ ]:


Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[6]:


for i in range(10):
    print(i)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 
for i in range(0,10):
    print(i)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for i in range(0,10,1):
    print(i)


# In[ ]:


Q12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[7]:


#Use of For Loop
print("For Loop")
for i in range(1,11):
    print(i)
#Use of While Loop
print("While Loop")
a =1
while a <= 10:
    print(a)
    a+=1


# In[ ]:


Q13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')
Ans.

This function can be called with spam.bacon().

 


# In[ ]:




