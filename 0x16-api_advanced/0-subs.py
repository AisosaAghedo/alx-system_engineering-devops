#!/usr/bin/python3
"""  function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers (not active users,
    total subscribers) for a given subreddit"""
    headers = {"User-Agent": 'Mozilla/5.0 (platform; rv:geckoversion)\
            Gecko/geckotrail Firefox/firefoxversion'}
    r = requests.get('https://www.reddit.com/r/programming/about.json'.
                     format(subreddit), headers=headers,
                     allow_redirects=False)
    if r.status_code != 200:
        return (0)
    else:
        return (r.json().get("data").get("subscribers"))
