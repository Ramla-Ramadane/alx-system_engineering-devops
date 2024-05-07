#!/usr/bin/python3
''' function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit'''

from requests import get


def number_of_subscribers(subreddit):
    '''Return the total number of subscribers'''

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 197.249.58.55'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
