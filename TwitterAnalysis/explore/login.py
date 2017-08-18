import tweepy
#consumer key,access token, access secret
ckey = "U7A6sqsqmeQHvipknVGmdjzwT"
csecret = "zTDbhjrqJcGLsUn3S9V4SYV5BQi61C1XbrxObSLUbFFxJKTnFV"
atoken = "891974438585081857-3Uw4GCUWC7FJGLRQumzYeLnio5COWT9"
asecret = "S0QriqKzg1JFCHehOvwqhf4ICXfNlNVjJr3r5yNd7k9hG"


def authentication():
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return auth
