#!/usr/bin/python
import MySQLdb
import sys
import operator
import pandas as pd
import json
import time

def fetch_data():
	data = pd.read_csv("time_series_covid_19_deaths.csv")
	j = 4
	n = len(data.columns)
	for i in range(0,len(data)):
	  if j < n-1:
	  	data.iloc[i,j]=data.iloc[i,j+1]-data.iloc[i,j]
	  	j = j + 1
	return data

def insert_data(data):	
	db = MySQLdb.connect(host="localhost", user="root", db="mydatabase")
	cursor = db.cursor()
	n = len(data)
	data = data.astype(object).where(pd.notnull(data), None)
	for i in range(0,n):
		insert = 'INSERT INTO `COVID19_deaths` (`Id`, `Province`, `Country`, `Lat`, `Long`, `New Cases 01/22/2020`,`New Cases 01/23/2020`,`New Cases 01/24/2020`,`New Cases 01/25/2020`,`New Cases 01/26/2020`,`New Cases 01/27/2020`,`New Cases 01/28/2020`,`New Cases 01/29/2020`,`New Cases 01/30/2020`,`New Cases 01/31/2020`,`New Cases 02/1/2020`,`New Cases 02/2/2020`,`New Cases 02/3/2020`,`New Cases 02/4/2020`,`New Cases 02/5/2020`,`New Cases 02/6/2020`,`New Cases 02/7/2020`,`New Cases 02/8/2020`,`New Cases 02/9/2020`,`New Cases 02/10/2020`,`New Cases 02/11/2020`,`New Cases 02/12/2020`,`New Cases 02/13/2020`,`New Cases 02/14/2020`,`New Cases 02/15/2020`,`New Cases 02/16/2020`,`New Cases 02/17/2020`,`New Cases 02/18/2020`,`New Cases 02/19/2020`,`New Cases 02/20/2020`,`New Cases 02/21/2020`,`New Cases 02/22/2020`,`New Cases 02/23/2020`,`New Cases 02/24/2020`,`New Cases 02/25/2020`,`New Cases 02/26/2020`,`New Cases 02/27/2020`,`New Cases 02/28/2020`,`New Cases 02/29/2020`,`New Cases 03/1/2020`,`New Cases 03/2/2020`,`New Cases 03/3/2020`,`New Cases 03/4/2020`,`New Cases 03/5/2020`,`New Cases 03/6/2020`,`New Cases 03/7/2020`,`New Cases 03/8/2020`,`New Cases 03/9/2020`,`New Cases 03/10/2020`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		params = (i+1,data.iloc[i,0],data.iloc[i,1],data.iloc[i,2],data.iloc[i,3],data.iloc[i,4],data.iloc[i,5],data.iloc[i,6],data.iloc[i,7],data.iloc[i,8],data.iloc[i,9],data.iloc[i,10],data.iloc[i,11],data.iloc[i,12],data.iloc[i,13],data.iloc[i,14],data.iloc[i,15],data.iloc[i,16],data.iloc[i,17],data.iloc[i,18],data.iloc[i,19],data.iloc[i,20],data.iloc[i,21],data.iloc[i,22],data.iloc[i,23],data.iloc[i,24],data.iloc[i,25],data.iloc[i,26],data.iloc[i,27],data.iloc[i,28],data.iloc[i,29],data.iloc[i,30],data.iloc[i,31],data.iloc[i,32],data.iloc[i,33],data.iloc[i,34],data.iloc[i,35],data.iloc[i,36],data.iloc[i,37],data.iloc[i,38],data.iloc[i,39],data.iloc[i,40],data.iloc[i,41],data.iloc[i,42],data.iloc[i,43],data.iloc[i,44],data.iloc[i,45],data.iloc[i,46],data.iloc[i,47],data.iloc[i,48],data.iloc[i,49],data.iloc[i,50],data.iloc[i,51],data.iloc[i,52])
		try:
			cursor.execute(insert, params)
			db.commit()
		except Exception as e:
			print('Failed to insert %s with error %s' % (1, repr(e)))
			cursor.close()

def search_location(loc, colname):
	db = MySQLdb.connect(host="localhost", user="root", db="mydatabase")
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	search = 'SELECT * FROM `COVID19_deaths` WHERE `Province`= %s'
	loc = loc.encode('ascii',errors='ignore')
	try:
		cursor.execute(search, (loc,))
		records = cursor.fetchall()
		for record in records:
			if record[colname] > 0:
				return 1
			else:
				return 0

		if(len(records)==0):
			return 0		
			
	except Exception as e:
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

def parse_tweets():
	all_tweets = []
	labelled_tweets = []
	weight_tweets = {}
	cnt=0
	for line in open('00.json','r'):
		temp = json.loads(line)
		all_tweets.append(temp)
		if(temp["user"]["location"]):
			location = temp["user"]["location"]
			ts = time.strftime('%m/%d/%Y', time.strptime(temp['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			colname = "New Cases " +  ts
			flag = search_location(location, colname)
			if(flag == 1):
				labelled_tweets.append(temp)
				all_tweets.remove(temp)
				weight = calculate_weight(temp)
				weight_tweets.update({cnt:weight})
		cnt=cnt+1
	return all_tweets, labelled_tweets, weight_tweets

if __name__ == '__main__':
	data = fetch_data()
	insert_data(data)
	all_tweets, labelled_tweets, weight_tweets = parse_tweets()
	print("Number of tweets labelled : " + str(len(labelled_tweets)))
	print("Number of tweets not labelled : " + str(len(all_tweets)))
	with open("labelled_tweets.txt", "w") as output:
		output.write(str(labelled_tweets))
	with open("not_labelled_tweets.txt", "w") as output:
		output.write(str(all_tweets))
	with open("weight_tweets.txt", "w") as output:
		output.write(str(weight_tweets))