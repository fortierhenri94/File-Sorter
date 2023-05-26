#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[6]:


path = r"C:/Users/hfort/Desktop/test/"


# In[11]:


file_name = os.listdir(path)


# In[20]:


folder_names = ['txt files', 'pdf files','png files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
        
for file in file_name:
    if ".txt" in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path + file, path + "txt files/" + file)
    elif ".png" in file and not os.path.exists(path + "png files/" + file):
        shutil.move(path + file, path + "png files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




