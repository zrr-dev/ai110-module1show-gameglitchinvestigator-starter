# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.
## 2. How did you use AI as a teammate?

**AI Suggestion 1: Accepted**
* **What the AI suggested:** When I asked how to stop the game from resetting every time I clicked "Submit", Claude suggested wrapping the random number generator in an `if "secret_number" not in st.session_state:` block.
* **Why it was correct:** This was correct because Streamlit reruns the entire `app.py` script on every button click. Using `session_state` forces the app to remember the secret number between runs instead of generating a new one.
* **How I verified it:** I accepted the code, ran the live app using `python -m streamlit run app.py`, and verified in the "Developer Debug Info" tab that the secret number stayed exactly the same across multiple guesses.

**AI Suggestion 2: Rejected / Modified**
* **What the AI suggested:** When I asked Claude to generate the `pytest` case for `check_guess`, it initially suggested writing a complex test that mocked Streamlit's session state and UI components.
* **Why I rejected or changed it:** This was over-engineered and out of scope. The `check_guess` function in `logic_utils.py` is pure Python logic and just takes integers as arguments. I didn't need to test the Streamlit UI, just the logic. 
* **How I verified it:** I asked Claude to simplify the test to only pass basic integers into `check_guess`. I verified the simpler version worked by running `python -m pytest` in the terminal and watching the tests pass successfully.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

 ## Demo Walkthrough
1. The game initializes and securely generates a secret number in the background (e.g., 50).
2. The user enters an initial guess of 25 and clicks Submit.
3. The game processes the input and correctly displays a "Too Low" hint.
4. The user enters a new guess of 75 and clicks Submit.
5. The game processes the input and correctly displays a "Too High" hint.
6. The user enters the correct guess of 50.
7. The game displays a success message, updates the score accurately, and ends.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
## Test Results
```text
============================= test session starts =============================
platform win32 -- Python 3.13.0, pytest-9.1.1
rootdir: C:\Zia Files\CodePath\ai110-module1show-gameglitchinvestigator-starter
collected 1 item

tests\test_game_logic.py .                                               [100%]

============================== 1 passed in 0.05s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
