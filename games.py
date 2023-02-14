#!/usr/bin/env python3

"""
A module to login in to brave browser and search for links
from the games and save them to txt files for each game.

The links will be found from duckduckgo.com.
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from time import sleep


def games_played(jp_file: str) -> list:
    """
    Function to get games from file and return a list
    """

    with open(jp_file, "r", encoding="utf-8") as file:
        games = file.read().splitlines()

    return games


EXECUTABLE_PATH = "/usr/bin/brave"
CHROME_DRIVER = "/usr/bin/chromedriver"

service = Service(CHROME_DRIVER)

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

# For running brave browser in the background...
options.add_argument("--headless")
options.add_argument("--disable-gpu")

options.binary_location = EXECUTABLE_PATH

driver = webdriver.Chrome(service=service, options=options)


def main():
    """
    Main function to login and search for links
    """

    # Instantiate the jackpot file.
    jackpot_file = "./games.txt"

    # Collect the games to be played.
    games = games_played(jackpot_file)

    for game in games:

        query: str = game.rstrip()
        filename: str = "pgn/" + query.split("/")[-1].lower() + ".txt"
        print(filename)

        driver.get(query)
        sleep(5)

        try:
            moves = driver.find_element(By.ID, "move-list")

            # write the moves to a file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(moves.text)

        except NoSuchElementException:
            print("No moves found for this game")


if __name__ == "__main__":
    main()
