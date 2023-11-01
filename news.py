from newsapi import NewsApiClient
import random
from api_key import API_KEY
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

from datetime import datetime, timedelta
prev_date = datetime.today() - timedelta(days=30)
next_date = datetime.today() - timedelta(days=0)
p_date = str(prev_date.year)+'-'+str(prev_date.month)+'-'+str(prev_date.day)
c_date = str(next_date.year)+'-'+str(next_date.month)+'-'+str(next_date.day)
p_date = prev_date.strftime('%Y-%m-%d')
c_date = next_date.strftime('%Y-%m-%d')
# Task 2: Create a Get News Method
newsapi = NewsApiClient(api_key=API_KEY)
def getNews(sourceId):
    newses = newsapi.get_everything(sources=sourceId,domains='bbc.co.uk,techcrunch.com',from_param=p_date,to=c_date,language='en',sort_by='relevancy',page=2)
    newsData = []
    for news in newses['articles']:
        list = [random.randint(0, 100), news['publishedAt'], news['title'],news['content'], 'REAL']
        newsData.append(list)
    return newsData



sources = newsapi.get_sources()
sourceList = []
for source in sources['sources']:
    sourceList.append(source['id'])
del sourceList[10:len(sourceList)]
print('New Sources: ', sourceList)


dataList = []
for sourceId in sourceList:
    newses = getNews(sourceId)
    dataList = dataList + newses

print('Total News: ', len(dataList))


import pandas as pd
df = pd.DataFrame.from_records(dataList)
df.columns = ['','publishedAt','title','text','label']
print(df)

# trainData = pd.read_csv('news.csv')
# trainData.columns = ['', 'title', 'text', 'label']
# data = [trainData, df]
# df = pd.concat(data)
# print(df.head())

# training_x, testing_x, training_y, testing_y = train_test_split(
#     df['text'], df.label, test_size=0.3, random_state=7)

# count_vectorizer = CountVectorizer(stop_words='english', max_df=0.7)
# feature_train = count_vectorizer.fit_transform(training_x)
# feature_test = count_vectorizer.transform(testing_x)

# classifier = PassiveAggressiveClassifier(max_iter=50)
# classifier.fit(feature_train, training_y)

# prediction = classifier.predict(feature_test)
# score = accuracy_score(testing_y, prediction)

# print("Accuracy: ", score*100)



# test_data = pd.read_csv('test_data.csv')
# test_labels = test_data.label
# test_data.head()

# test_data_feature = count_vectorizer.transform(test_data['text'])
# prediction = classifier.predict(test_data_feature)


# for i in range(len(test_labels)):
#     print(test_labels[i], prediction[i])

# score = accuracy_score(test_labels, prediction)
# print("Accuracy: ", score*100, "%")