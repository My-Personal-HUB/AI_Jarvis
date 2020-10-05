# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.models import Model
import matplotlib.pyplot as plt
from models import *
import numpy as np

# load preprocessed data and labels
data = np.load('data address')
labels = np.load('labels address')


# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.20, stratify=labels, random_state=42,shuffle = True)

# initialize data generators
aug_train = ImageDataGenerator(rescale= 1.0/255.,
	rotation_range=20,
	zoom_range=0.15,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.15,
	horizontal_flip=True,
	fill_mode="nearest")

aug_test  = ImageDataGenerator(rescale= 1.0/255.)

# initialize batch size and epochs
BS = 32
EPOCHS = 50

# train model
hist = model.fit_generator(steps_per_epoch=len(trainX)//BS,
                           generator=aug_train.flow(trainX, trainY, batch_size=BS),
                           validation_data= (testX, testY),
                           validation_steps=len(testX)//BS,
                           epochs=EPOCHS)
