# Application of EventMapper Framework for Coronavirus Detection 

Weak signal events cannot be detected and verified easily unlike signal events. This is because they have fewer reports for each event. Detecting them from social media streams is difficult when corroborative event detection is not available.  Further, due to the presence of noise or surrounding large-signal events they are difficult to identify. The EventMapper framework integrates corroborative and probabilistic sources for real-time weak-signal detection. Corroborative sources include news articles, historical databases and reporting agencies. Probabilistic data sources include social media sources including Twitter, Facebook, Youtube among others. 

### Data Characteristics
- Kaggle Dataset on Novel Coronavirus 2019
	- Day-wise time series at global level
	- Has data on confirmed cases, recovered cases and deaths
	- Important fields include Id, Province, Country, Day-wise cases
	- Original Source: John Hopkins
	- Update Frequency: 2 days
- Twitter Datastream
	- Complete size is 5GB
	- Important attributes extracted: created_at, id, id_str, text, source, retweeted, retweet_count, timestamp_ms, land, coordinates, place etc

### Download Kaggle data using API
- Setup a Kaggle account and get a key. Then using the commands below on the command line.
- kaggle datasets download -d sudalairajkumar/novel-corona-virus-2019-dataset
- /home/neha/.local/bin/kaggle competitions list
- /home/neha/.local/bin/kaggle datasets download -d sudalairajkumar/novel-corona-virus-2019-dataset
- unzip novel-corona-virus-2019-dataset.zip
​
[Reference]:​ https://adityashrm21.github.io/Setting-Up-Kaggle/
[Project Presentation Video] : ​​https://youtu.be/DZcj1QFaikU
[Project Demo Video]: https://youtu.be/UivQ1fZoTR4
