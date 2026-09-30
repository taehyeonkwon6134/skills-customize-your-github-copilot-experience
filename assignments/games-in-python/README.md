
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python to practice string manipulation, loops, conditional statements, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Use the provided list of words to select a secret word and initialize the variables needed to track the game state.

#### Requirements

Completed program should:

- Randomly select one word from the predefined `words` list.
- Store guessed letters in a collection that can be updated during the game.
- Set a maximum number of incorrect guesses and track the current count.
- Treat letter guesses consistently, such as by converting them to lowercase.


### 🛠️ Implement Gameplay and Results

#### Description

Create the main game loop so the player can guess letters, reveal the secret word, and receive a result when the game ends.

#### Requirements

Completed program should:

- Display the current progress of the secret word using underscores for unguessed letters.
- Ask the player to enter a letter and update the progress when the guess is correct.
- Track incorrect guesses and show how many attempts remain.
- End when the player reveals the complete word or reaches the maximum number of incorrect guesses.
- Display a clear win or lose message, including the secret word when the player loses.

Example output:

```text
Word: _ _ _ _ _ _
Guess a letter: p
Correct! Attempts remaining: 6
Word: p _ _ _ _ _
```
