import json
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	print(request.method)
	if request.method == "GET":
		return render_template('index.html')
	if request.method == "POST":
		details = request.form['province']
		provincelist = details.split(',')
		Lats = []
		Longs = []
		
		## Deaths
		Deaths = []
		provincenames = []
		cur = mysql.connection.cursor()
		val = []
		sql_select_Query = "SELECT * FROM COVID19_deaths WHERE Province = %s"
		provincename = provincelist[0]
		provincename = provincename.strip()
		val.append(provincename)
		for i in range(1, len(provincelist)):
			temp = []
			provincename = provincelist[i]
			provincename = provincename.strip()
			val.append(provincename)
			sql_select_Query += " OR Province = %s"
		val=tuple(val)
		cur.execute(sql_select_Query, val)
		results = cur.fetchall()
		for row in results:
			Lats.append(row[3])
			Longs.append(row[4])
			Deaths.append(row[len(row)-1])
			provincenames.append(row[1])
		cur.close()

		## Confirmed
		Confirmed = []
		cur = mysql.connection.cursor()
		val = []
		sql_select_Query = "SELECT * FROM COVID19_confirmed WHERE Province = %s"
		provincename = provincelist[0]
		provincename = provincename.strip()
		val.append(provincename)
		for i in range(1, len(provincelist)):
			temp = []
			provincename = provincelist[i]
			provincename = provincename.strip()
			val.append(provincename)
			sql_select_Query += " OR Province = %s"
		val=tuple(val)
		cur.execute(sql_select_Query, val)
		results = cur.fetchall()
		for row in results:
			Confirmed.append(row[len(row)-1])
		cur.close()

		## Recovered
		Recovered = []
		cur = mysql.connection.cursor()
		val = []
		sql_select_Query = "SELECT * FROM COVID19_recovered WHERE Province = %s"
		provincename = provincelist[0]
		provincename = provincename.strip()
		val.append(provincename)
		for i in range(1, len(provincelist)):
			temp = []
			provincename = provincelist[i]
			provincename = provincename.strip()
			val.append(provincename)
			sql_select_Query += " OR Province = %s"
		val=tuple(val)
		cur.execute(sql_select_Query, val)
		results = cur.fetchall()
		for row in results:
			Recovered.append(row[len(row)-1])
		cur.close()
		return render_template('index.html', Lats=Lats, Longs=Longs, provincenames=provincenames, Deaths=Deaths, results=results, provincename=provincename, Confirmed=Confirmed, Recovered=Recovered)
        
if __name__ == '__main__':
    app.run()
