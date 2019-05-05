import datetime
import time
import tweepy
from tweepy import OAuthHandler
import re
import csv

C_KEY ='3D3GveliAIWrbGgTg5IZ5NqHo'
C_SECRET ='YvCpDOyp9Bk5av2t9eM9HO08IdP0lZi8NqfGauEXSNPo9bCHls'
A_TOKEN ='1104333276997509122-FivTPlAGoXlxDJIPfi9MBJdYPyAXPX'
A_TOKEN_SECRET = 'OHfHwA98MIXd0E7wPwVHAWcX6zy66TL6nASODH8HLU6qO'

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)

source_file = "C:/Users/admin/source/repos/crawl_twittter/data/"
def is_tag_user(tweet):
    tag_user = []
    string = tweet.split()
    for item in string:
        item = re.sub('[^a-zA-Z0-9@]', '', item)
        if (item.startswith('@') and len(item)>1):
            tag_user.append(item)
    return tag_user
def tweet_from_user(userName, startDate, endDate):
    i = 1
    user_level1 = []

    for tweet in tweepy.Cursor(api.user_timeline, id = userName).items():
        if tweet.created_at < endDate and tweet.created_at > startDate:
            print("Tweet " + str(i) + "\n")
            if(len(is_tag_user(tweet.text)) > 0):
                for user in is_tag_user(tweet.text):
                    user_level1.append(user)
                    with open(source_file+"graph.csv", "a",encoding='utf-8') as f:
                        writer = csv.writer(f)

                        writer.writerow([userName, user])
                    pass
        
                    
                    
            i = i + 1
    user_level1 = list(set(user_level1))
    for user in user_level1:
        with open(source_file+"user1.csv", "a",encoding='utf-8') as f:
            writer = csv.writer(f)

            writer.writerow([user])
        pass
        


screen_name = "@ManUtd"
startDate = datetime.datetime(2018, 8, 10, 0, 0, 0)
endDate = datetime.datetime(2019, 5, 2,0 , 0, 0)
tweet_from_user(screen_name,startDate,endDate)
























      



        
        









 









