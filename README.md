# Connect Four

This is an attempt to build an AI that plays Connect Four in Python.

## Usage

Two files `playerOne.py` and `playerTwo.py` will be placed in the root directory.
Executing the command `python referee.py` will import both players (AI strategies) and output the sequence of moves to STDOUT, and the winning player.

## API

The playerOne and playerTwo modules should implement a `Player` class that has the following methods and attributes:

- an `__init__` method that accepts the keyword arguments `token` and `opponentToken`, which will be characters. For example, a Player object will be initialized with:
`player = Player(token="1", opponentToken="2")`

- a settable `grid` attribute that is a list of strings. Each row is represented by a 7 characters string where "0" is an empty cell, "1" has a token from you, "2" has a token from the opponent (or respectively with the tokens that have been initialized). See the following grid as an example:
```
["0000000",
 "0000000",
 "0012100",
 "0011201",
 "0121222",
 "0112121"]
```
- a `move` property that outputs an integer in `range(7)`. In the previous example, it should probably output `2` if it does not want the opponent to win.

## Rules

- 5 seconds thinking time per move. Any more will be disqualified.
- Any invalid move is disqualifying.
- Let the best AI win.

## TODO

- Write the main loop for the Referee
- Write a dummy player with the right API
- Write a player module that takes human input
