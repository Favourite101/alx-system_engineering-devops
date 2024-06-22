#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json?allow_over18=true"
  headers = {"User-Agent": "Custom"}
  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
  except requests.exceptions.RequestException:
    return 0
