#!/usr/bin/env python
# coding: utf-8

# In[2]:


# python dictionaries
 # dictionary
sample_dict = {
   "year": 2023,
    "blogname": "Ayieko1",
    "email": "ayieko1@gmail.com",
    "about": "Data Science and Machine Learning"
}
print(type(sample_dict))


# In[3]:


# a dictionary with a list data type
sample_dict = {
   "year": 2023,
    "blogname": "Ayieko1",
    "email": "ayieko1@gmail.com",
    "about": "Data Science and Machine Learning",
    "featured": ['Python for data science', 'Numpy tutorial', 'Pandas tutorial']
}
print(type(sample_dict))


# In[4]:


# accessing dictionary items

blog_name = sample_dict['blogname']
featured_blogs = sample_dict['featured'] # the value is a list loop to display individual items

print('Blog name: ', blog_name)
print('Featured: ', featured_blogs)


# In[6]:


# displaying values and keys in the dictionary
# use keys() for keys and values() method for values

print(sample_dict.keys()) # displays list of all keys
print(sample_dict.values()) # displays a list of all values


# In[7]:


# updating dictionary
# use syntax; dict[key_name] = value

# since the item with key_name = featured, is a list we access and
# change the item at index 2

sample_dict["featured"][2] = 'How we build CNN in TensorFlow'
print('Featured: ', sample_dict)


# In[9]:


# add new item to the dict
sample_dict['posts'] = 30 # add item
print('Number of posts: ', sample_dict['posts']) # display item


# In[12]:


# removing items from the dictionary
# remove year with pop() method

sample_dict.pop("year")



# In[14]:


# remove email with del keyboard
del sample_dict["email"]


# In[ ]:




