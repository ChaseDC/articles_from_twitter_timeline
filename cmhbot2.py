
from twython import Twython
from twython import TwythonError
import json


def extract_article(t):
    """find the url for articles in a single tweet"""
    try:
        expanded = t.get('entities', {}).get('urls', {})[0].get('expanded_url', {})
        return expanded
    except (IndexError):
        pass

    try:
        retweet = t.get('retweeted_status', {}).get('entities', {}).get('urls', {})[0].get('expanded_url', {})
        return retweet
    except (IndexError, KeyError):
        pass

    try:
        quote_url = t.get('quoted_status', {}).get('entities', {}).get('urls', {})[0].get('expanded_url', {})
        return quote_url
    except (IndexError, KeyError):
        pass

    try:
        reply = t.get('retweeted_status', {}).get('quoted_status', {}).get('entities', {}).get('urls', {})[0].get('expanded_url', {})
        return reply
    except (IndexError, KeyError):
        pass


with open('twitter_bot_credentials.json') as f:
    creds = json.loads(f.read())

def handler(event, context):
    twitter = Twython(creds['APP_KEY'], creds['APP_SECRET'],
                  creds['OAUTH_TOKEN'], creds['OAUTH_TOKEN_SECRET'])
    tweets = twitter.get_home_timeline(count = 2000, tweet_mode = 'extended')
    print("found {} timeline tweets".format(len(tweets)))
    url = []
    for t in tweets:
        article = extract_article(t)
        if article:
            url.append(article)


    for u in url:
        if "https://twitter.com/" in u:
            try:
                
                tweet_id = [i for i in u.split('/') if i.isdigit()]
                tweet = twitter.show_status(id = tweet_id[0], tweet_mode = 'extended')
                article = extract_article(tweet)
                if article:
                    url.append(article)
            except TwythonError:
                pass
    final_url = [u for u in url if "twitter.com" not in u]
    final_url = set(final_url)
    print("posted {} article tweets".format(len(final_url)))

    twitter_bot = Twython(creds['APP_KEYbot'], creds['APP_SECRETbot'],
                  creds['OAUTH_TOKENbot'], creds['OAUTH_TOKEN_SECRETbot'])

    for t in final_url:
        try:
            twitter_bot.update_status(status = t)
        except TwythonError:
            pass
