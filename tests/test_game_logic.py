from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_low_high_correct():
    # Lower than the secret: "Too Low" and the hint points up
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

    # Higher than the secret: "Too High" and the hint points down
    outcome, message = check_guess(70, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    # Exact match: a win with the "Correct" message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message
