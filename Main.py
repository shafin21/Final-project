from shafin import create_secret_file
from hatim import validate_hex
from francisca import evaluate_guess
from Abraham import decode_hex_message

def main():

    filename = "secret.txt"

    create_secret_file(
        "Good job!! You found the secret message.",
        filename
    )

    target_hex = "41"
    secret_key = "01000001"
    guesses = []

    print("Welcome to Read My Mind!")
    print("Guess the secret hexadecimal key.")
    print("You have 3 attempts.")

    while len(guesses) < 3:

        guess = input("Enter your guess: ").strip()

        try:
            validate_hex(guess)
        except ValueError as error:
            print(error)
            continue

        guesses.append(guess)

        result = evaluate_guess(guesses, target_hex)

        print(result)

        if guess == target_hex:
            message = decode_hex_message(
                guess, secret_key, filename
            )
            print(message)
            break


if __name__ == "__main__":
    main()