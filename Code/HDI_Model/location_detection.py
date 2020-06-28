import numpy as np
import pickle
import nltk
import tensorflow as tf 
from numpy import zeros
from gensim.models import KeyedVectors
from gensim.utils import tokenize
import pandas as pd
from sner import Ner
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


def search_location(loc, colname):
	db = MySQLdb.connect(host="localhost", user="root", db="mydatabase")
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	loc = loc.encode('ascii',errors='ignore')
	l1=loc.split(" ")
	search = 'SELECT * FROM `COVID19_confirmed` WHERE `Province`= %s'
	try:
		cursor.execute(search, (loc,))
		records = cursor.fetchall()
		for record in records:
			if record[colname] > 0:
				return 1	
	except Exception as e:
		return 0
		print('Failed to select %s with error %s' % (1, repr(e)))

	search = 'SELECT * FROM `COVID19_confirmed` WHERE `Country`= %s'
	try:
		cursor.execute(search, (loc,))
		records = cursor.fetchall()
		for record in records:
			if record[colname] > 0:
				return 1		
	except Exception as e:
		return 0
		print('Failed to select %s with error %s' % (1, repr(e)))

	if(len(l1)==0):
		return 0
			
	search = 'SELECT * FROM `COVID19_confirmed` WHERE `Province`= %s'
	try:
		cursor.execute(search, (l1[0],))
		records = cursor.fetchall()
		for record in records:
			if record[colname] > 0:
				return 1
	except Exception as e:
		return 0
		print('Failed to select %s with error %s' % (1, repr(e)))
	
	search = 'SELECT * FROM `COVID19_confirmed` WHERE `Country`= %s'
	try:
		cursor.execute(search, (l1[0],))
		records = cursor.fetchall()
		for record in records:
			if record[colname] > 0:
				return 1
			else:
				return 0
		if(len(records)==0):
			return 0
	except Exception as e:
		return 0
		print('Failed to select %s with error %s' % (1, repr(e)))

def calculate_weight(temp):
	weight=0
	if "favorited"== "true" or "favorite_count">0:
		weight=weight+1
	if "retweeted"== "true" or "retweet_count">0:
		weight=weight+1
	if "quote_count">0:
		weight=weight+1
	if "reply_count">0:
		weight=weight+1		
	return weight	


def findLocations(location_tags):
        locations = []
        loc=[]
        if location_tags[0][1] == 'LOCATION':
            loc.append(location_tags[0][0])
        for entry in location_tags[1:]:
            if entry[1] == 'LOCATION':
                loc.append(entry[0])
            else:
                if loc:
                    locations.append(' '.join(loc))
                    loc=[]
        if loc:
            locations.append(' '.join(loc))
        return locations

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


def parse_tweets(desc_locations):
	all_tweets = []
	labelled_tweets = []
	weight_tweets = {}
	cnt=0
	for line in open('00.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp["text"])
		for i in range(len(desc_locations)):
			location = desc_locations[i]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp["text"])
				all_tweets.remove(temp["text"])
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
			else:
				flag2 = search_location(x[0], colname)
				if flag2 == 1:
					labelled_tweets.append(temp["text"])
					all_tweets.remove(temp["text"])
					weight = calculate_weight(temp)
					weight_tweets.update({cnt:weight})		
		cnt=cnt+1
	for line in open('01.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp["text"])
		for i in range(len(desc_locations)):
			location = desc_locations[i]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp["text"])
				all_tweets.remove(temp["text"])
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
			else:
				flag2 = search_location(x[0], colname)
				if flag2 == 1:
					labelled_tweets.append(temp["text"])
					all_tweets.remove(temp["text"])
					weight = calculate_weight(temp)
					weight_tweets.update({cnt:weight})
		cnt=cnt+1
	for line in open('02.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp["text"])
		for i in range(len(desc_locations)):
			location = desc_locations[i]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp["text"])
				all_tweets.remove(temp["text"])
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
			else:
				flag2 = search_location(x[0], colname)
				if flag2 == 1:
					labelled_tweets.append(temp["text"])
					all_tweets.remove(temp["text"])
					weight = calculate_weight(temp)
					weight_tweets.update({cnt:weight})
		cnt=cnt+1
	for line in open('03.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp["text"])
		for i in range(len(desc_locations)):
			location = desc_locations[i]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp["text"])
				all_tweets.remove(temp["text"])
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
			else:
				flag2 = search_location(x[0], colname)
				if flag2 == 1:
					labelled_tweets.append(temp["text"])
					all_tweets.remove(temp["text"])
					weight = calculate_weight(temp)
					weight_tweets.update({cnt:weight})
		cnt=cnt+1
	for line in open('04.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp["text"])
		for i in range(len(desc_locations)):
			location = desc_locations[i]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp["text"])
				all_tweets.remove(temp["text"])
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
			else:
				flag2 = search_location(x[0], colname)
				if flag2 == 1:
					labelled_tweets.append(temp["text"])
					all_tweets.remove(temp["text"])
					weight = calculate_weight(temp)
					weight_tweets.update({cnt:weight})
		cnt=cnt+1
	for line in open('05.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp["text"])
		for i in range(len(desc_locations)):
			location = desc_locations[i]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp["text"])
				all_tweets.remove(temp["text"])
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
			else:
				flag2 = search_location(x[0], colname)
				if flag2 == 1:
					labelled_tweets.append(temp["text"])
					all_tweets.remove(temp["text"])
					weight = calculate_weight(temp)
					weight_tweets.update({cnt:weight})
		cnt=cnt+1	
	return all_tweets	
	

encoder = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, unicode_errors='ignore', limit=100000)
model = tf.keras.models.load_model("my_model.h5")

all_tweets2 = pd.read_csv('not_labelled_tweets.csv')
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz','stanford-ner.jar', encoding='utf-8')

locations=[]
for i in range(len(all_tweets2)):
	cleaned_message = all_tweets2.iloc[i,0]
	if str(cleaned_message) != 'nan':
		tokenized_text = word_tokenize(cleaned_message)
		classified_text = st.tag(tokenized_text)
		desc_locations = findLocations(classified_text)
		locations.append(desc_locations)

test_tweets = parse_tweets(desc_locations)
pred1=[]
pred0=[]

for i in range(len(test_tweets)):
	msg = all_tweets.iloc[i,0]
	if str(msg) != 'nan':
		encoded_msg = encode(msg)
		prediction = np.argmax(model.predict(np.array([encoded_msg]))[0])
		if(prediction==0):
			pred0.append(prediction)
		else:
			pred1.append(prediction)


