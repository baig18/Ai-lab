
# coding: utf-8

# In[32]:

from keras.datasets import cifar10
import  matplotlib.pyplot as plt
(x_train, y_train), (X_test, y_test) = cifar10.load_data()


# In[33]:

x_train[0]


# In[34]:

get_ipython().magic('matplotlib inline')
plt.imshow(x_train[3])


# In[35]:

get_ipython().magic('matplotlib inline')
plt.imshow(x_train[4])


# In[41]:

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train= X_train/ 255
X_test= X_test/ 255


# In[39]:

#create model
from keras.models import  Sequential 
from keras.layers import  Conv2D 
from keras.layers import  Dropout 
from keras.layers import  MaxPooling2D
from keras.layers import  Flatten
from keras.layers import  Dense
from keras.utils import  np_utils

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(3, 32, 32), padding='same', activation='relu'))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
#complie model
epochs = 25
lrate = 0.01
decay= lrate/epochs


# In[ ]:



