#!/usr/bin/env python
# coding: utf-8

# # Assignmnet-3

# In[ ]:


get_ipython().set_next_input('1.Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')
Ans:
    
    Functions are very Advantageous to have in your progrmas because Functions helps the coder to reduce\ shorten the code.
    Its helps in saving time and memory. its helps in reducing deplicasy of coding , its like using the wheel instead of
    reinventing the wheel.
    
    Functions are two types 1.in-built
                            2.User defined 
        
        
    becuase of functions if the user  define the function once , he can use it by calling the function whenever he requires 
    the function.
    


# In[ ]:


get_ipython().set_next_input("2.When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')
    
Ans:
    The code in a function run: when it's called not when it's specified because the code gets excuted when we run the code not 
        when we specify the function.
        
In order to finish the specifing of function it needs to be excuted intially.
    
    


# In[ ]:


get_ipython().set_next_input('3.What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')
Ans :
    The statement thats used to create a function is def() >>> thats define function followed by the identifier thats the name 
    of the function.
    
    
    example :
         def function_name


# In[ ]:


get_ipython().set_next_input('4.What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')
Ans:
    
    Function is basic step where we specify the function in the def function.
    
    Function call is the next step of def function , function call is what moved execution into function, the function call 
    is what returns function's value.
    
    Function was the intial step , then
    function call is the final step.


# In[ ]:


get_ipython().set_next_input('5.How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')
Ans:
    Variables defined inside the function body have local scope, while variables defined outside have global scope.
    
    one global Python scope per program execution
    one local scope inside a program.
    


# In[ ]:


get_ipython().set_next_input('6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')
Ans:
    When the function returns, the local scope is destroyed and any variables it contains are forgotten.


# In[ ]:


get_ipython().set_next_input('7.What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')
Ans:
The return statement is used to terminate the execution of a function call 
and "return" the result (the value of the expression after the return keyword) to the caller. 

No, it is not it possible to have a return value in an expression.


# In[ ]:


get_ipython().set_next_input('8.If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')

Ans:
If no return statement appears in a function definition, control automatically returns to the 
calling function after the last statement of the called function is executed. 
In this case the return value of the called function is undefined.


# In[ ]:


get_ipython().set_next_input('9.How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans:

We can use the global keyword to declare which variables are global.


# In[ ]:


get_ipython().set_next_input('10.What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')
ans:
    The data type of None is NoneType.


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')
Ans:
    That import statement imports a module named areallyourpetsnamederic.


# In[ ]:


get_ipython().set_next_input('12.If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
Ans:
    This function can be called with spam. bacon().


# In[ ]:


get_ipython().set_next_input('13.What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')
 Ans:
    Error handling can be used,for example we can use try and except block.


# In[ ]:


get_ipython().set_next_input('14.What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')
Ans:
    The code that could potentially cause an error goes in the try clause.
    The code that executes if an error happens goes in the except clause.

