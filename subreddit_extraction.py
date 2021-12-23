# -*- coding: utf-8 -*-

"""
f = open("location", "w", encoding='utf-8') #location of combined file (user, date, text)
f2 = open("location", "w", encoding='utf-8') #location of user list
f3 = open("location", "w", encoding='utf-8') #location of date list
f4 = open("location", "w", encoding='utf-8') #location of text list

#you will need to set up a reddit account with the reddit api

import praw
reddit= praw.Reddit(client_id = 'client_id', #your client id goes here
                    client_secret = 'client_secret', #your client secret goes here
                    username = 'username', #your username goes here
                    password = 'password', #your password goes here
                    user_agent = 'user_agent',) #use any string you prefer

subreddit = reddit.subreddit('news') #replace 'news' with subreddit of your choice

top_subreddit = subreddit.top(limit=5000) #the maximum number of posts you want to extract (it may be dignificantly lesss than 5000)

for submission in top_subreddit:
    if not submission.stickied:
        print((submission.author),"\t",(submission.created_utc),"\t",(submission.title.replace('\n', ' ')), file = f)
        print((submission.title), file = f2)
        print((submission.created_utc), file = f3)
        print((submission.created_utc), file = f3)
        print((submission.author), file = f4)
        print((submission.author), file = f4)
        print((submission.author),"\t",(submission.created_utc),"\t",(submission.selftext.replace('\n', ' ')), file = f)
        print((submission.selftext), file = f2)
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            print((comment.author),"\t",(comment.created_utc),"\t",(comment.body.replace('\n', ' ')), file = f)
            print((comment.body), file = f2)
            print((comment.created_utc), file = f3)
            print((comment.author), file = f4)

f.close()
f2.close()
f3.close()
f4.close()
