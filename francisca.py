def evaluate_guess(user_guesses, target_value):
    """Evaluate user guesses against a secret value and return the outcome.

    Args:
        user_guesses (list): Guesses entered by the user as strings.
        target_value (str): The secret message or value to compare against.

    Returns:
        str: A message indicating whether the user guessed correctly or
            triggered a specific game outcome or error message.
    """
    attempts = 0

    for guess in user_guesses:
        if guess == "":
            continue

        attempts += 1

        if guess == target_value:
            return "Correct! You read my mind!"
        elif attempts >= 3:
            return "Game over! You ran out of attempts."

    if attempts == 0:
        return "No valid guesses were entered."

    return "You did not guess the secret value."