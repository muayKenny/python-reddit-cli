#! usr/bin/env python3

import click
import praw
from prawcore.exceptions import ResponseException
import json

# On each run of your program, it should print out:
#  New posts from the last program execution,
#  Posts that are no longer within the top 75 posts, and
#  Posts that had a vote count change and by how much.

print("Hello, welcome to the best way to view Reddit.")
print("What would you like to do?")


@click.command()
@click.argument("cmd")
def main(cmd):
    click.echo("Okay, running {}".format(cmd))


reddit = praw.Reddit(
    client_id="client_id",
    client_secret="client_secret",
    user_agent="user_agent",
    username="username",
    password="pw",
)

try:
    print("Authenticated as {}".format(reddit.user.me()))
except ResponseException:
    print("Something went wrong during authentication")

list = []


for submission in reddit.subreddit("threejs").top(limit=75):
    sub = {
        "id": submission.id,
        "title": submission.title,
        "score": submission.score,
        "url": submission.url,
        "body": submission.selftext,
    }
    list.append(sub)

print("churning out list of submissions")

with open("./data_store/incoming.json", "w") as f:
    f.write(json.dumps(list))

# ", ".join(str(d) for d in list)

""" import praw
import pandas as pd
import datetime as dt


subreddit = reddit.subreddit('threejs')



top_subreddit = subreddit.top()

for submission in subreddit.top(limit=1)
    print(submission.title, submission.id)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \ 
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext) """
