#!/usr/bin/env python3
"""
A module to login in to brave browser and search for links
from the games and save them to txt files for each game.

The links will be found from duckduckgo.com.
"""
import os

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def connection_active():
    """This function checks whether there is an active internet
    connection in the device, if there is, find the necessary pgn
    files for the urls, if not... pass
    """
    try:
        _ = requests.get('https://www.google.com', timeout=1)
        return True

    except requests.exceptions.RequestException:
        return False


def games_played(jp_file: str) -> list:
    """
    Function to get games from file and return a list
    """

    with open(jp_file, "r", encoding="utf-8") as file:
        games = file.read().splitlines()

    return games


# TODO: Change this filepaths to add whether I played black or white.
def check_unconverted_pgns():
    """
    Function to look for urls that are already converted to
    pgns so as not to reconvert them.
    """

    url: str = "https://www.chess.com/game/live/"

    games: list[str] = games_played("./games.txt")

    all_games: list = [game.split("/")[-1]
                       for game in games]

    games_analyzed = [game.split("-")[-1].removesuffix(".txt")
                      for game in os.listdir("pgn")]

    non_analyzed = [url+game for game
                    in all_games if game not in games_analyzed]

    return non_analyzed


EXECUTABLE_PATH = "/usr/bin/chromium"
CHROME_DRIVER = "/usr/bin/chromedriver"

service = Service(CHROME_DRIVER)

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

# For running brave browser in the background...
options.add_argument("--headless")
options.add_argument("--disable-gpu")

options.binary_location = EXECUTABLE_PATH

driver = webdriver.Chrome(service=service, options=options)


def check_if_black_or_white() -> str:
    """
    Function to check whether I played as white or black
    Checks which username is given at the beginning... If your
    username is given, you are playing as black,
    (black is on top -> board and piece placement)
    else, you are playing as white...
    """

    color = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "user-tagline-component")
        )
    )

    # my username is EphantusMash3727
    username: str = "EphantusMash3727"
    black: bool = username in color.text

    return "black" if black else "white"


def main():
    """
    Main function to login and search for links
    """

    # Check for games that have already been converted to pgn
    games = check_unconverted_pgns()

    if not games:
        return

    for game in games:

        query: str = game.rstrip()

        driver.get(query)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "move-list"))
        )
        moves = driver.find_element(By.ID, "move-list")

        color = check_if_black_or_white()

        f_name: str = f"pgn/{color}-data-" + query.split("/")[-1] + ".pgn"
        # write the moves to a file
        with open(f_name, "w", encoding="utf-8") as file:
            moves = moves.text
            moves = moves.replace("\n", " ")
            file.write(moves)


if __name__ == "__main__":

    if connection_active():
        main()

    else:
        print("No internet connection")
