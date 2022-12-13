#!/usr/bin/env python
# coding: utf-8

# # Assignment-1

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

* - Expression used for doing mathematical operation thats multiplication.

"hello"- value

-87.8 - value

- - Expression

(-, Expression, ,, division, symbol)

+- Expression , Addition  symbol

6 - Value


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans:
     Variable is the memory location
    String is array thats used for storing text or characters
    
    The difference between the string and a variable is
    Variable can be used to store values of different data types whereas in string we can store only text or characters.
    


# In[ ]:





# Q3. Describe three different data types.
# 
# Ans :
# 
# DAta types in python represents the type of data stored into a variable or memory
# 
# few Data types are as follows:
# 
# # int data type
# The int data type represents an integer number, without any decimal points
# 
# ex. a=10
# 
# # float data type
# 
# A float data type is a number that contains decimal points.
# 
# ex. x=22.5
# 
# # str Data type
#  A string is represented by a group og characters .
#  a string is enclosed in single quote or double quote
#  
#  ex.
#  str="hello world"
#  
#  # Complex data type
#  
#  # Bool data type

# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Ans.
An expression is a combination of operators and operands that is interpreted to produce some other value.


The following are the arthematic and mathematical and some functions that we can perform using expressions

+ : add (plus).
- : subtract (minus).
x : multiply.
(:, divide.)
** : power.
get_ipython().run_line_magic(':', 'modulo.')
<< : left shift.
>> : right shift.
& : bit-wise AND.
| : bit-wise OR.
^ : bit-wise XOR.
~ : bit-wise invert.
< : less than.
> : greater than.
<= : less than or equal to.
>= : greater than or equal to.
== : equal to.
get_ipython().system('= : not equal to.')
and : boolean AND.
or : boolean OR.
not : boolean NOT.


# In[ ]:





# In[ ]:


Q5. This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Ans.
An expression in Python is a combination of operators and operands.
A statement is used for creating variables or for displaying values.

The difference between an expression and a statement is an expression is used to perform operations but statement is use to print
the result

spam = 10 # spam = 10 is statement 
if we want to convert the above statement into expression , it can be done in the following way,

spam = 10 +20 #its now converted into statement


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[1]:


bacon = 22
bacon + 1


# In[ ]:


After running the following code, what does the variable bacon contains the value 23 
because in the initial value of bacon is 23 but in the two line we have given an increment function (increment +1), as we know in 
python the variable takes the latest assigned value , the final output of bacon will be =23


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')

'spam'+'spamspam'
'spam'*3


# In[4]:


'spam'+'spamspam'
'spam'*3


# In[5]:


'spam'+'spamspam'.
# in the above statement '+' acts as a concatenator


# In[6]:


'spam'*3 
#in the statement '*' is acting as multiplication


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8 .Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Ans. 

According to the rules of declaring a variables
 
    A variable name shouldnot start with numbers 
    
    in the above example egg is considered as a variable where as 100 is not considered as a variable because it starts with a numeric value.


# In[ ]:





# In[ ]:


Q9. What three functions can be used to get the integer, floating-point number, or string
get_ipython().set_next_input('version of a value');get_ipython().run_line_magic('pinfo', 'value')

Ans .

The int() , float() , and str( ) functions will evaluate to the integer, floating-point number,
and string versions of the value passed to them.


# In[ ]:





# In[7]:


get_ipython().set_next_input('Q10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten '+99+' burritos'


# In[ ]:


'''' in the above question error has occured because concatenation can happen only beteewen a string and a string not a string and 
a integer due to this its showing an error


we can look to Q7 to see how the concatenate function works betwwen the str and a str

