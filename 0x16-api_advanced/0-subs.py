#!/usr/bin/python3
"""  function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers (not active users,
    total subscribers) for a given subreddit"""

    headers = {"User-Agent": 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return (0)
    else:
        return (r.json().get("data").get("subscribers"))
