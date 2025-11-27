import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_data(year, day):
    return requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        },
        cookies={
            "session": os.environ.get("SESSION"),
        },
    ).text.splitlines()
