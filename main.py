#!/usr/bin/env python

import random

import requests
from bs4 import BeautifulSoup


# TODO: separate spoilers
def main() -> None:
    imdb_id = input("Enter an imdb id:")
    url = f"https://www.imdb.com/title/{imdb_id}/trivia"

    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise err

    trivia = [
        " ".join(div.stripped_strings)
        for div in BeautifulSoup(response.text, "html.parser").find_all(
            "div", "sodatext"
        )
    ]

    print(f"Random fact: {random.choice(trivia)}")


if __name__ == "__main__":
    main()
