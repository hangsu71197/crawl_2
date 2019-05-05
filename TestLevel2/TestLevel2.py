import datetime
import time
import tweepy
from tweepy import OAuthHandler
import re
import csv
import numpy as np

C_KEY ='3D3GveliAIWrbGgTg5IZ5NqHo'
C_SECRET ='YvCpDOyp9Bk5av2t9eM9HO08IdP0lZi8NqfGauEXSNPo9bCHls'
A_TOKEN ='1104333276997509122-FivTPlAGoXlxDJIPfi9MBJdYPyAXPX'
A_TOKEN_SECRET = 'OHfHwA98MIXd0E7wPwVHAWcX6zy66TL6nASODH8HLU6qO'

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)

source_file = "C:/Users/admin/source/repos/crawl_twittter/data/"

level1_node = np.atleast_1d(np.loadtxt(source_file + "user1.csv", dtype=str, delimiter=",", usecols=(0,)))

def is_tag_user(tweet):
    tag_user = []
    string = tweet.split()
    for item in string:
        item = re.sub('[^a-zA-Z0-9@]', '', item)
        if (item.startswith('@') and len(item)>1):
            tag_user.append(item)
    return tag_user
def tweet_from_user(list1, startDate, endDate):
    i = 1
    user_level2 = []
    backoff_counter = 1
    for userName in list1:
        if(backoff_counter > 20):
            bbackoff_counter = 15
        while True:
            try:
                all_tweet = tweepy.Cursor(api.user_timeline, id = userName).items(300)
                for tweet in all_tweet:
                    
                    print("Tweet " + str(i) + "\n")
                    if(len(is_tag_user(tweet.text)) > 0):
                        for user in is_tag_user(tweet.text):
                            user_level2.append(user)
                            with open(source_file+"graph.csv", "a",encoding='utf-8') as f:
                                writer = csv.writer(f)

                                writer.writerow([userName, user])
                            pass

            
                    i = i + 1

                break

            except tweepy.TweepError as e:
                if (e.reason == "Twitter error response: status code = 429" ):
                    
                    print (e.reason)
                    time.sleep(60*backoff_counter)
                    backoff_counter = backoff_counter + 1
                    continue
                else:
                    print (e.reason)
                    break
                    
    user_level2 = list(set(user_level2))
    for user in user_level2:
        with open(source_file+"user2.csv", "a",encoding='utf-8') as f:
            writer = csv.writer(f)

            writer.writerow([user])
        pass
        

startDate = datetime.datetime(2018, 8, 10, 0, 0, 0)
endDate = datetime.datetime(2019, 5, 2,0 , 0, 0)
tweet_from_user(level1_node,startDate,endDate)

























      



        
        









 










