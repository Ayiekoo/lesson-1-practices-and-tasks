#!/usr/bin/env python
# coding: utf-8

# In[7]:


# create a tuple
sample_tuple1 = ('Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian')
print(sample_tuple1)
type(sample_tuple1)

# accessing tuple items
# access the third element in the tuple
print(sample_tuple1[2])

# to access the second last item in the tuple
sample_tuple1[-2]

# specifying start and end to slice a tuple
sample_tuple1[1:4] # the element at the fourth index is excluded

# updating tuples
list_from_tuple = list(sample_tuple1) # convert the tuple list

list_from_tuple[3] = 'Ranch' # change the item at index [3]

sample_tuple1 = tuple(list_from_tuple) # convert back to tuple

sample_tuple1

del sample_tuple1


# In[10]:


# unpacking tuples

#unpack the tuple
sample_tuple1 = ('Pepperoni', 'Hawaiian', 'Chicken Alfredo', 'Vegeterian', 'Magherita')

(house_type1, house_type2, house_type3, house_type4, house_type5) = sample_tuple1
print(house_type1)
print(house_type2)
print(house_type3)
print(house_type4)
print(house_type5)


# In[29]:


# Python sets
sample_set1 = {'Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
print(sample_set1)
print(type(sample_set1))

# we can find duplicates
sample_set2 = {'Pensies', 'Sunflower', 'Sunflower', 'Pimrose', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
print(sample_set2) # duplicates are ignored

# accessing set items
# interete over the set and display items
for flower in sample_set1:
    print(flower)
    
print( 'Sunflower' in sample_set1)

# adding items to a set
# add(); addas a single element to the set
# update() adds multiple elements to the set

# add a single element; add()
sample_set1.add('Bloodroot')
sample_set1.add('Buttercup')
print('update set with add() method')
for flower in sample_set1:
    print(flower)
    
    
# using the update() method
sample_set1 = {'Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
sample_set1.update(['Apple', 'Pinneaples', 'Peach', 'Guavas']) # add to the list
print('Update set with update() method')
sample_set1

# removing items from the set
# use remove() or discard()
sample_set1 = {'Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
sample_set1.remove('Pimrose')
print('One flower removed from the set')
print(sample_set1)


# In[24]:





# In[30]:


# removing items from the set
# use remove() or discard()
sample_set1 = {'Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
sample_set1.remove('Pimrose')
print('One flower removed from the set')
print(sample_set1)


# In[34]:


# discard()
sample_set1 = {'Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
sample_set1.discard('Sunflower') # discards sunflower
print('One flower discarded from the list')
print(sample_set1)

# discard()
sample_set1 = {'Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry'} # types of flower sets
sample_set1.discard('Pimrose') # discards pimrose
print('one flowers discarded from the list')
print(sample_set1)


# In[ ]:




