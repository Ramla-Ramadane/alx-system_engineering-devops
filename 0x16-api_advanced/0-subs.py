#!/usr/bin/python3
'''function that queries the Reddit API and returns the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''Return the total number of subscribers'''
    path = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(path, allow_redirects=False, headers=headers)
    if response.status_code in (302, 404):
        return 0

    json = response.json()
    return json.get('data').get('subscribers')
