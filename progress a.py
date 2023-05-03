#!/usr/bin/env python
# coding: utf-8

# In[2]:


sample_list1 = ['Bungalow', 'Cottage', 'Cabin', 1997, 2000]
sample_list2 = [30, 40, 100, 60]
print(sample_list1)
print(sample_list2)


# In[3]:


# printing a list, with the title list
sample_list1 = ['Bungalow', 'Cottage', 'Cabin', 1997, 2000]
sample_list2 = [30, 40, 100, 60]
print('List 1:', sample_list1)
print('List 2:',sample_list2)


# In[4]:


# Find the length of sample_list1
len(sample_list1)


# In[5]:


# Accessing list items
print(sample_list[2])


# In[6]:


# Accessing list items
print(sample_list1[2])


# In[7]:


print(sample_list2[1]) #to access the second element


# In[8]:


print(sample_list1[1:3]) # To access the start and the last index


# In[9]:


# Omit the end index
# Omit start index
print(sample_list1[1:])
print(sample_list[:3])


# In[10]:


# Omit the end index
# Omit start index
print(sample_list1[1:])
print(sample_list1[:3])


# In[11]:


# NEGATIVE INDEXING
print(sample_list1[-2])


# In[12]:


# Negative slicing
#Return item [-5] from end to the item at [-2] -not included, from end
print(sample_list1[-5:-2])


# In[13]:


# Add a new element to the list.
# use the syntax; list[element_index] = new_value

# changing the value of item at index [3]
# remember index counts begin with 0

sample_list1[3] = 1996
print(sample_list1)

# value of teh index changed from 1997 to 1996


# In[16]:


# adding lit item
# use teh syntax; append()

sample_list1.append('Charlet')
print(sample_list1)
sample_list1


# In[17]:


# removing item in the list
# use the syntax; remove()

sample_list1.remove('Charlet')
print(sample_list1)


# In[23]:


# use pop() method or del statement to remove a specific index

# using pop();
#remove item at index 3 1996

sample_list1.pop(3)
print(sample_list1)
# 1996 is omitted

sample_list1.pop()
print(sample_list1)

# 2000 is omitted

# using del statement
# remove teh element using del statement
sample_list2 = [30, 40, 100, 60]
del sample_list2[2] # Removes the element at position 3 -> 100 (which is number 2 considering numbering starts from 0)
print(sample_list2)

# the del statement can be used to clear the list
del sample_list2
print(sample_list2)

# alternatively, the clear method can be used to eliminate the list
sample_list1.clear()
print(sample_list1)


# In[28]:


#SORTING LISTS

# create a new list
pizza_flavors = ['Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian']
pizza_prices_usd = [11.99, 17.99, 14.99, 18.99, 19.99]

# apply the sort() method:
pizza_flavors.sort()
print(pizza_flavors)

# sorted alphabetically

pizza_prices_usd.sort()
print(pizza_prices_usd)


# In[27]:


pizza_prices_usd.sort()
print(pizza_prices_usd)


# In[29]:


pizza_prices_usd = [11.99, 17.99, 14.99, 18.99, 19.99]
pizza_prices_usd.sort()
print(pizza_prices_usd)


# In[30]:


pizza_prices_usd = [100, 17.99, 200, 18.99, 300]
pizza_prices_usd.sort()
print(pizza_prices_usd)


# In[33]:


# sorting in descending; we reverse
# sort the pizza_flavor list in descending order
pizza_flavors = ['Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian']
pizza_flavors.sort(reverse = True)
print(pizza_flavors)


# In[34]:


# sorting in descending; we reverse
# sort the pizza_flavor list in descending order
pizza_flavors = ['Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian']
pizza_flavors.sort(reverse = False)
print(pizza_flavors)


# In[37]:


# sort pizza_prices_usd list in descending order
pizza_prices_usd = [100, 17.99, 200, 18.99, 300]
pizza_prices_usd.sort(reverse = True)
print(pizza_prices_usd)


# In[38]:


# sort pizza_prices_usd list in descending order
pizza_prices_usd = [100, 17.99, 200, 18.99, 300]
pizza_prices_usd.sort(reverse = False)
print(pizza_prices_usd)


# In[39]:


# reverse the order of list
pizza_flavors = ['Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian']
pizza_flavors.reverse()
print(pizza_flavors)


# In[ ]:


# reverse the order of list
pizza_flavors = ['Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian']
pizza_flavors.reverse()
print(pizza_flavors)

