#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Books(object):
    
    def __init__(self, author, title):
       
        self.author = author.strip().title()
        self.title = title.strip().title()

    def display(self):
        
        return '{}, written by {}'.format(self.title, self.author)


if __name__ == '__main__':
    Book = Books('John Steinbeck','Of Mice and Men')
    
    print Book.display()
    
    
    
    def __init__(self, author, title):
       
        self.author = author.strip().title()
        self.title = title.strip().title()

    def display(self):
        
        return '{}, written by {}'.format(self.title, self.author)


if __name__ == '__main__':
    Book = Books('Harper Lee', 'To Kill a Mockingbird')
    
    print Book.display()


# In[ ]:




