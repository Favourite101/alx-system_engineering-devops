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
    url = f"https://www.reddit.com/r/{subreddit}/about.json?allow_over18=true"  # Include NSFW subreddits
  headers = {"User-Agent": "MyCoolScript (by /u/your_username)"}  # Replace with your username
  try:
    response = requests.get(url, headers=headers, allow_redirects=False)  # Don't follow redirects
    response.raise_for_status()  # Raise exception for non-200 status codes
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
  except requests.exceptions.RequestException:
    # Handle any request errors (e.g., network issues, 404)
    return 0
    