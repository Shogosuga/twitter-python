from pymongo import MongoClient, DESCENDING
from pprint import pprint
import pandas as pd
from score import Sentiment
from datetime import datetime

db = MongoClient(host='mongodb+srv://masai:kkkkk412@masai-vfhtb.mongodb.net/test?retryWrites=true',port=27017).masai
post_col = db['food_posts']

#nodes = post_col.find({},{'text':1}).limit(5)
nodes = post_col.find({},{'text':1}).sort('utime', DESCENDING).limit(100).skip(200)

scoreList = pd.DataFrame(index=[], columns=['_id','score'])
dictNoun = pd.read_csv('./dict/noun.csv', names=['id','name','eval','form','score'])
dictDeclinable = pd.read_csv('./dict/declinable.csv', names=['id','eval','name','score'])

for node in nodes:
    sentiment = Sentiment(node['text'])
    noun = sentiment.speech('名詞', dictNoun)
    verb = sentiment.speech('動詞', dictDeclinable)
    adjective = sentiment.speech('形容詞', dictDeclinable)

    evaluation = noun + (verb*1.2) + (adjective*1.4)
    evaluation = round(evaluation, 3)

    oneScore = pd.Series({'_id':node['_id'], 'score':evaluation})
    scoreList = scoreList.append(oneScore, ignore_index = True)

now = datetime.now()
now_ts = now.timestamp()
now_str = str(now_ts)
scoreList.to_csv('./data/' + now_str + '.csv')