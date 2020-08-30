#!/usr/bin/env python
# coding: utf-8

# In[4]:


def listDivide(numbers, divide=2): 
    count = 0 
    for num in numbers:
        if num % divide is 0: 
            count += 1 
    return count 
      

    class ListDivideException(Exception): 
          pass 
 
 
    def testListDivide(): 
        if listDivide([1, 2, 3, 4, 5]) != 2: 
            raise ListDivideException 
        elif listDivide([2, 4, 6, 8, 10]) != 5: 
             raise ListDivideException 
        elif listDivide([30, 54, 63, 98, 100], 10) != 2:
            raise ListDivideException 
        elif listDivide([]) != 0: 
            raise ListDivideException 
        elif listDivide([1, 2, 3, 4, 5], 1) != 5: 
            raise ListDivideException
            
    if __name__ == "__main__": 
        testListDivide() 

