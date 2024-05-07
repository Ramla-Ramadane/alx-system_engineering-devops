#!/usr/bin/python3
'''function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    '''pprint the titles of first 10 hot posts'''
    path = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(path, allow_redirects=False, headers=headers)
    if response.status_code in (302, 404):
        print("None")
        return

    json = response.json()
    json_children = json.get('data').get('children')
    for post in json_children:
        print(post.get('data').get('title'))
