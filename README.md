# Battleship practice project implementation

This repo is a possible solution to the [Battleship practice project](https://github.com/JOmarCuenca/battleship-practice-project) exercise.

# Installation

1. Clone this repo
2. You'll need to create a python virtual env and activate it to install the dependencies

```sh
python3 -m venv env && source env/bin/activate
```

3. Install the dependencies

```sh
pip install -r requirements.txt
```

4. Now you are ready to run the program

```sh
python3 main.py --horizontal
```

You can check all the possible ways to run the program with explanations by running

```sh
python3 main.py -h
```

# Challenge Points Grade 8/10

## Required

- [ ] Fork this repo
- [x] Make it so the user can send its input as `A1`, `F6` and so on
- [x] The AI must be able to play using randomly generated input (aka not very smart moves)
- [x] The Game must be able to start and finish when one of the players has lost
- [x] The Game must be turned based
- [x] It must have some sort of GUI 
  - [x] To start a game
  - [x] To visualize what moves have been played
  - [x] To visualize a winner
- [x] Make a **happy path game** (Meaning if the player or AI behave properly and perfectly the game should start and finish no problem)
- [x] Basic version control with readable commit messages

## Beginner

- [x] Make the UI in the console using ascii characters, printable so the user can play the game vertically, (meaning on side of the board above the other) against the opponent
- [x] Make the game using replayable, meaning play multiple games on a row
- [x] Make the commit messages descriptive and relevant (keep a good version control of the program)
- [x] Divide the program into reusable functions that make the code readable
- [x] Edit the `Readme.md` file to have instructions on how to install (if required) and how to run it.
- [x] Add `try-except` clauses so that it is able to handle **not happy paths** *i.e. the user sends something like `Z-1` which is not a valid input*

## Challenging

- [x] Make the UI better, meaning able to be played horizontally to better display the board for each player
- [x] Enhance the AI, so that it plays still randomly, but if it finds a battleship, keep attacking it until it destroys it
- [x] Make the `Readme` file complaint with better *Markdown practices*
```bash
> # Something kind of like this
> # add lines like this so that it looks better for the readers
> # as an example
> python3 my_battleship_program.py
```
- [x] Write logs of the games, record scores and moves from each player in a *directory/file* (I recommend the *logs/* directory, if it doesn't exist, it must be created)
- [x] Make better `try-except` clauses, meaning instead of catching generic error types, catch specific error classes in your program
```python
# like so
try:
    # Do something
except ValueError:
    # Log that the user sent something weird and we log that specific error
except IndexError:
    # Some value is out of range, print why and where
except:
    # Some generic clause
```

## Advanced

- [x] Make it portable, i.e. make it so that you are using `venv` or `conda` to install required packages and using the correct python version, this also means that you'll require a `requirements.txt` file to be added in the repo [reference](https://docs.python.org/es/3/library/venv.html)
- [x] Write `unittests` that can be used to assert Quality in the program and prevent breaking changes
- [x] Keep tags for versions of your code so that they can be downloaded by others [>Read this for reference<](https://www.atlassian.com/es/git/tutorials/inspecting-a-repository/git-tag)
- [x] Write the program in an Object Oriented fashion, meaning instead of plain functions, make classes and objects that interact with each other in order to play a game
- [ ] Make the game pausable, meaning if the user inputs a command the game is saved in local storage to be continued later, can be a raw file, but I recommend using `pickle`
- [x] Make it so that it can be run directly from the CLI with arguments, I recommend checking the `argparse` lib
```bash
# Kind of like this to play against an easy AI
python3 my-program.py --ai-level 1
# Kind of like this to play against an hard AI
python3 my-program.py --ai-level 2
# Or 2 players
python3 my-program.py --pvp
```
- [x] Make better logs, there are libraries dedicated to printing logs, catching and documenting exceptions, etc, I recommend checking [loguru](https://github.com/Delgan/loguru)

## Very Hard

- [ ] Make an awesome UI using a library like `PyGame` or something along the lines
- [x] Make a Github Action to test the repo's unittests in the cloud, in case anyone wants to contribute to your repo

## Impossible
- [ ] Make it playable online against another player using something like `Django`, mounting it on a server in `AWS`, `Firebase/GCP`, etc