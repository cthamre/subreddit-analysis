#define what subreddit's top posts will be extracted
#define client id, client secret, username, password, and user agent for API access
def redditsearch(subreddit, client_id, client_secret, username, password, user_agent):

    # -*- coding: utf-8 -*-
    f = open(f"{subreddit}_date_user_text.txt", "w", encoding='utf-8') #location of combined file (user, date, text)
    f2 = open(f"{subreddit}_users.txt", "w", encoding='utf-8') #location of user list
    f3 = open(f"{subreddit}_dates.txt", "w", encoding='utf-8') #location of date list
    f4 = open(f"{subreddit}_text.txt", "w", encoding='utf-8') #location of text list
    
    
    #set up PRAW with reddit API credentials
    import praw
    reddit= praw.Reddit(client_id = client_id,
                        client_secret = client_secret,
                        username = username,
                        password = password,
                        user_agent = user_agent,)
    
    subreddit = reddit.subreddit('subreddit') #access subreddit
    
    top_subreddits = subreddit.top(limit=5000) #the maximum number of posts you want to extract
 
    for submission in top_subreddits:
       if not submission.stickied: #avoid stickied posts
           #print author, date, and text in combined output file
           #replace line breaks with spaces
           print((submission.author),"\t",(submission.created_utc),"\t",(submission.title.replace('\n', ' ')), file = f)
           print((submission.title), file = f4)
           print((submission.created_utc), file = f3)
           print((submission.created_utc), file = f3)
           print((submission.author), file = f2)
           print((submission.author), file = f2)
           print((submission.author),"\t",(submission.created_utc),"\t",(submission.selftext.replace('\n', ' ')), file = f)
           print((submission.selftext), file = f2)
           submission.comments.replace_more(limit=0)
           for comment in submission.comments.list():
               print((comment.author),"\t",(comment.created_utc),"\t",(comment.body.replace('\n', ' ')), file = f)
               print((comment.body.replace('\n', ' ')), file = f4)
               print((comment.created_utc), file = f3)
               print((comment.author), file = f2)
    
    f.close()
    f2.close()
    f3.close()
    f4.close()
