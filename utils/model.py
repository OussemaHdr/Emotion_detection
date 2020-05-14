from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import BatchNormalization
from time import time
from tensorflow.python.keras.callbacks import TensorBoard

tensorboard = TensorBoard(log_dir="logs/{}".format(time()))

classifier = Sequential()

classifier.add(Conv2D(64, (3, 3), input_shape = (48, 48, 3), activation = 'relu' )) 
classifier.add(MaxPooling2D(pool_size=(2,2))) 
classifier.add(BatchNormalization()) 


classifier.add(Conv2D(128, (3, 3), activation = 'relu')) 
classifier.add(MaxPooling2D(pool_size = (2, 2))) 
classifier.add(BatchNormalization())


classifier.add(Conv2D(256, (3, 3), activation = 'relu' ))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(BatchNormalization()) 



classifier.add(Flatten())
classifier.add(Dense(units = 512, activation = 'relu'))  
classifier.add(Dropout( rate = 0.2 )) 

classifier.add(Dense(units = 256, activation = 'relu'))  
classifier.add(Dropout( rate = 0.2 )) 

classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dropout( rate = 0.2 )) 

classifier.add(Dense(units = 64, activation = 'relu'))  
classifier.add(Dropout( rate = 0.2 ))

classifier.add(Dense(units = 32, activation = 'relu'))  
classifier.add(Dropout( rate = 0.2 )) 

classifier.add(Dense(units = 16, activation = 'relu'))  
classifier.add(Dropout( rate = 0.2 )) 

classifier.add(Dense(units = 6 , activation = 'softmax')) 
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,                
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True) 

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory("Train",
                                                 target_size = (48, 48),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory("Test",                  
                                            target_size = (48, 48),
                                            batch_size = 32,
                                            class_mode = 'categorical')
classifier.summary() 

classifier.fit_generator(training_set,
                         steps_per_epoch = 100, 
                         epochs = 75,
                         validation_data = test_set,
                         validation_steps = 100,
                         shuffle = True, callbacks = [tensorboard] )
