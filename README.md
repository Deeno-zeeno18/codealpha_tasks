# CodeAlpha Python Programming Internship

This repository contains my submissions for the CodeAlpha Python Programming internship. Three of the four available tasks were completed, built with core Python — no external libraries required.

## Tasks Completed

### 1. Hangman Game — `HANGMAN_GAME.py`
A text-based Hangman game where the player guesses a randomly selected word one letter at a time.
A maximum of six guesses are allowed.

- Random word selection from a predefined list of 5 words
- 6 incorrect guesses allowed before the game ends
- Console-based input/output

**Concepts used:** `random`, `while` loops, `if-else`, strings, lists

**To Run it:**
```bash
python HANGMAN_GAME.py
```

### 2. Stock Portfolio Tracker — `STOCK_PORTFOLIO_TRACKER.py`
A simple stock tracker that calculates total investment value based on user-entered stock names and quantities, matched against a hardcoded price dictionary.

- Validates user input (stock names, quantities)
- Warns on unrecognized ticker symbols instead of failing silently
- Combines duplicate ticker entries automatically
- Saves a formatted breakdown of the investment, plus the total, to `INVESTMENT.TXT`

**Concepts used:** dictionaries, input/output, basic arithmetic, file handling

**To Run it:**
```bash
python STOCK_PORTFOLIO_TRACKER.py
```

### 3. Rule-Based Chatbot — `RULE_BASED_CHATBOT.py`
A simple rule-based chatbot that replies to greetings, questions, and goodbyes using predefined response categories.

- Recognizes greetings across multiple categories (welcome, morning, afternoon, evening, goodbye)
- Matches user input against a predefined phrase dictionary and returns a random reply from the matching category
- Falls back to a "not recognized" message for unmatched input

**Concepts used:** `if-elif`, functions, loops, input/output

**Run it:**
```bash
python RULE_BASED_CHATBOT.py
```

## About

Completed as part of my [CodeAlpha](https://www.codealpha.tech) Python Programming internship.
Zelden Okai. 