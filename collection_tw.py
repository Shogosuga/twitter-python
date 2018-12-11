import tweepy

CONSUMER_KEY = '8qqYKpCmhHz12maFnAZtH1Tiq'
CONSUMER_SECRET = 'OVsabb6XA6wXSBwcBrgjb5ZkZbRDkgoEfo3qRHlNygbDrFoPGk'
ACCESS_TOKEN = '1430529673-8DKgzTYLxQJSsNl3R4cr7ojFagvGHXgWG4K3oEw'
ACCESS_SECRET = 'Y1twCN883RURgdR1BZmRbMEvbHmlZ851eO42BAzvWNCaE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


class getTweet:
    
    def __init__(self , listPath , outputPath):
        self.listPath = listPath
        self.outputPath = outputPath

    def pulltext(self):
        with open (self.listPath , 'r' ) as f:
            u = [s.strip() for s in f.readlines()]
            for username in u:
                try:
                    timeline = api.user_timeline(id = username)
                
                    for i in timeline['text'] :
                        with open (self.outputPath , mode ='a' , encoding = 'utf-8') as w:
                            w.write(i)  
                
                except Exception as e:
                    pass

#指定のファイルパス
listPath = './data/users/0.tsv'
outputPath = './data/texts/0.txt'

t = getTweet(listPath, outputPath)
t.pulltext()