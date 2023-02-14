-------------------------------------------------------------------------------------

            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                               # Poor man's chess analysis code.                   
            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

-------------------------------------------------------------------------------------

            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                      ## From chess.com                          
            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-------------------------------------------------------------------------------------

# TODO

Create a cron job that checks whether there is a new url in the file games.txt.
If any is found, do the necessary and get a pgn file out of the url.

Merge the python files, so that it can extract data whilst sending the data to pgn
files directly instead of the code first writing to txt files, then another code
that converts the txt files to pgn files.


-------------------------------------------------------------------------------------
# What different files do...

games.txt -> stores urls from the chess games I have played in chess.com

       NB: This reminds me I should create a hotkey for pasting new urls in the games.txt file,
       whenever I have them copied.

-------------------------------------------------------------------------------------

games.py ->  formats the final form of the pgn file given by bash into a readable pgn form, bash
can also do this, but let's try the python version first.


-------------------------------------------------------------------------------------

data.sh -> Reads the given html files and gets the url with my chess data. It will then delete the
html files it has used once the data is derived... For space purposes and to not have to push diff't
html files to github all the time...


-------------------------------------------------------------------------------------

pgn/ -> A folder to store all derived pgn files...


-------------------------------------------------------------------------------------

games.sh -> curls the html files from games.txt into html files, which are then read to have their data
derived.

-------------------------------------------------------------------------------------

            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                If you come across this repo, and you can improve it please do so
                and inform me...
            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

-------------------------------------------------------------------------------------





