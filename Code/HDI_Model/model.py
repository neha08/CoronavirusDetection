import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import io
import numpy as np
import pickle as pkl
import os
import nltk
from numpy import zeros
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from gensim.models import KeyedVectors
from gensim.utils import tokenize

def encode(data):
	zero_v = zeros(shape=(300,))
	tokens = list(nltk.tokenize.word_tokenize(data))
	transformed_data = np.zeros(shape=(300,))
	zero_v = np.zeros(shape=(300,))
	if not tokens:
		pass
	else:
		for word in tokens:
			if word in encoder:
				transformed_data += list(encoder[word]) 
			else:
				transformed_data = zero_v
		transformed_data/=len(tokens)
	return transformed_data

def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', kernel_initializer='he_normal',input_shape=(300,)),
    keras.layers.Dense(8, activation='relu', kernel_initializer='he_normal'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(1, activation='sigmoid')
  ])
  model.compile(optimizer='adam',
                loss=tf.keras.losses.BinaryCrossentropy(),
                metrics=['accuracy'])
  return model

model = create_model()
train_x = np.zeros(shape=(3500,300))
train_y = np.zeros(shape=(3500,))
encoder = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, unicode_errors='ignore', limit=100000)
train_tweets = pd.read_csv('labelled_tweets.csv')
train_tweets2 = pd.read_csv('not_labelled_tweets.csv')
for i in range(len(train_tweets)):
	msg=train_tweets.iloc[i,0]
	if str(msg) != 'nan':
		encoded_msg = encode(msg)
		temp = np.array([encoded_msg])
		train_x [i] = temp
		train_y [i] = int(1)

for j in range(len(train_tweets2)):
	msg2=train_tweets2.iloc[i,0]
	if str(msg2) != 'nan':
		encoded_msg2 = encode(msg2)
		temp2 = np.array([encoded_msg2])
		train_x [i+j] = temp2
		train_y [i+j] = int(1)

model.fit(train_x, train_y,
  batch_size=32,
  epochs=5,
  verbose=1,
  validation_split=0.1,
  shuffle=True)
model.save('my_model.h5') 

