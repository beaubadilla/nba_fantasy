import datetime
import logging
import requests
from string import Template
import time

from bs4 import BeautifulStoneSoup

MAX_REQUESTS_PER_MIN = 20
SAFE_MAX_REQUESTS_PER_MIN = MAX_REQUESTS_PER_MIN / 2
SECS_PER_MIN = 60
REQUEST_RATE = SECS_PER_MIN / SAFE_MAX_REQUESTS_PER_MIN


def main():
    url_template = Template("https://www.basketball-reference.com/players/$first_initial/$player_additional.html")
    'Hey, Bob!'

    players = [
        "jokicni01",
        "antetgi01",
        # "embiijo01",
        # "doncilu01",
        # "jamesle01",
        # "duranke01",
        # "murrade01",
        # "davisan02",
        # "hardeja01",
    ]
    for player in players:
        first_initial = player[0].lower()
        player_additional = player

        url = url_template.substitute(first_initial=first_initial, player_additional=player_additional)
        response = requests.get(url)

        # Read HTML
        # Get id="meta". This will be a div

        # Get all paragraphs within div
        # For each paragraph
        #   If no <strong> element, skip. e.g. nicknames
        #   Get text from <strong> element. This will be the section/category e.g. NBA Debut
        #   Get text from paragraph. This will be the value of the section/category e.g. October 28, 2009
        # Save to file
        time.sleep(REQUEST_RATE)


if __name__ == "__main__":
    main()