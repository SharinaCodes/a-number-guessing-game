# Number Guessing Game 🎲

A Python-based interactive number guessing game that incorporates **basic descriptive statistics** to analyze player performance across multiple rounds. This project combines **programming fundamentals** with **data science techniques** such as tracking attempts, computing averages, and identifying trends in performance.

---

## 📌 Project Overview

This project demonstrates how a simple game can serve as a foundation for **data collection and analysis**. Each time the player attempts to guess the randomly generated number, their number of attempts is stored. At the end of the session, summary statistics are calculated to provide insights into the player’s performance.

Key highlights:

* **Game logic**: Random number guessing with higher/lower feedback.
* **Error handling**: Invalid inputs (non-numeric, out-of-range) are caught and handled gracefully.
* **Performance tracking**: Attempts are logged across multiple games.
* **Statistical analysis**: Mean, median, and mode of attempts are computed and displayed.

---

## ⚙️ Features

### Gameplay

* Random number generated between **1 and 100** for each round.
* Player receives feedback:

  * `"It's higher"` if guess is too low.
  * `"It's lower"` if guess is too high.
  * `"Got it"` when correct.
* Robust input validation (rejects invalid and out-of-range guesses).

### Data Tracking

* Saves the **number of attempts per game** in a list.
* Maintains a **running high score** (fewest guesses).
* Calculates:

  * **Mean** → average attempts.
  * **Median** → midpoint attempts.
  * **Mode** → most common attempts (or reports none if multimodal).

### User Interaction

* Displays a **welcome message** at the start.
* Shows **round results** and cumulative performance stats.
* Offers option to **play again** or **quit gracefully**.
* Displays **final stats summary** when quitting.

---

## 🗂️ File Structure

```
project/
│── guessing_game.py   # Main game script
│── README.md          # Documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed.
* Terminal or command prompt.

### Running the Game

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python guessing_game.py
   ```

---

## 📊 Example Gameplay

```
-------------------------------------
Welcome to the numbers guessing game!
-------------------------------------

I'm thinking of a number between 1 and 100...   50
It's higher
I'm thinking of a number between 1 and 100...   75
It's lower
I'm thinking of a number between 1 and 100...   62
Got it
Attempt #1
It took you 3 guesses to get the correct number.
Your best attempt was 3 guesses
Y for yes, anything else to exit: Y
```

*On exit:*

```
-------------------------------------
Final Stats!
-------------------------------------
The average of your guesses is 4.
The median of your guesses is 3
The mode of your guesses is [3]
Thanks for playing!
```

---

## 🔬 Data Science Connections

This project reflects a **miniature data science pipeline**:

1. **Data Collection**

   * Captures the number of attempts per game as raw observations.

2. **Data Cleaning & Validation**

   * Ensures inputs are valid integers within the specified range.

3. **Exploratory Data Analysis (EDA)**

   * Computes descriptive statistics (mean, median, mode).
   * Identifies patterns in guessing performance across games.

4. **Performance Tracking**

   * Uses “best attempt” as a benchmark for improvement.
   * Provides feedback loop for the player to aim for fewer guesses.

---

## ✅ Rubric Alignment

* **Run Script** → Game runs without crashing; exceptions are handled ✅
* **Display Intro** → Welcome message shown at start ✅
* **Random Number** → New random number each game ✅
* **User Input** → Input validated; out-of-range and non-numeric handled ✅
* **Responding to Player** → Higher/lower feedback provided ✅
* **Displaying Scores** → Attempts per round and best attempt tracked ✅
* **Display End Game** → Quit message and stats summary displayed ✅
* **Analysis** → Mean, median, mode of attempts shown at end ✅

---

## 🧩 Possible Extensions

* Track game data across sessions by saving results to a file or database.
* Visualize attempt distributions with **matplotlib** or **seaborn**.
* Add difficulty modes (different ranges or hints).
* Build a web or GUI interface for interactive play and analytics.

---

## 📖 License

This project is for educational purposes as part of a Data Analysis Techdegree.

---