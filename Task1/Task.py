import random


def guess(ran=None, user_inputs=None):
    """Function to guess a random number between 0 and 1000."""
    if ran is None:
        ran = random.randint(0, 1000)  # If no random number is passed, generate a new one.

    count = 0
    feedback = []

    for number in user_inputs:
        count += 1
        try:
            if number < 0 or number > 1000:
                raise ValueError("Please enter a number between 0 and 1000.")

            if number == ran and count == 1:
                feedback.append("Congratulations! You guessed the right number in just ONE try.\nYou are legend!")
                return feedback
            elif number == ran and count >= 2:
                feedback.append(f"Congratulations! You guessed the right number in {count} tries.")
                return feedback
            elif ran > number:
                feedback.append("Sorry you have to guess higher.")
            elif ran < number:
                feedback.append("Sorry you have to guess lower.")
        except ValueError as e:
            feedback.append(str(e))

    return feedback

if __name__ == "__main__":
    while True:
        number = ("")