#!/usr/bin/env python3

"""

"""

import os


def format_data(data: str):
    """Formats the data in readable form"""

    print(data)


def file_cleaner(file_name: str, new_file: str):
    """converts text files to pgn files"""

    with open(file_name, 'r') as file, open(new_file, 'w') as new_f:
        data = file.read()
        data = data.replace('\n', ' ')
        new_f.write(data)


def main():
    """
    Main function
    """

    games_tup: list = [file for file in os.listdir('chess_pgn/')
                       if file.endswith('.txt')]

    for game in games_tup:

        new_game: str = 'data' + game.removesuffix('.txt') + '.pgn'

        file_cleaner(f'chess_pgn/{game}',
                     f'pgn/{new_game}')


if __name__ == '__main__':
    main()
