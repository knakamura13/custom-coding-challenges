# Challenge 005 – Xs and Os

Players X and O are playing a game consisting of N rounds.
A player wins the whole game if they win any three rounds in a row AND their opponent does not.
If both or neither players manage to win three rounds in a row, then there is a tie.
Note that the total number of rounds a player has won does not matter.

Given a string S of length N consisting only of letters "X" and "O",
write a function that determines the winner of the game.

Return "X" if player X won the game, "O" if player O won the game, or "tie" if there was a tie.

Examples:

1. `"OXXXOXOOX"` => `"X"`
2. `"XOXXXOOOXOOO"` => `"tie"`
3. `"XX"` => `"tie"`
4. `"XXOOOOOXX"` => `"O"`

Assumptions:

- N is an integer within the range `[1...2001]`
- String S is made only of the characters `X` and/or `O`.
