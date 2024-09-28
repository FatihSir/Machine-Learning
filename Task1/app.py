from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for session


# Route for main page
@app.route('/')
def index():
    session['random_number'] = random.randint(0, 1000)  # Generate a new random number at the start
    session['attempts'] = 0  # Reset attempt count
    return render_template('index.html')


# Route for guessing
@app.route('/guess', methods=['POST'])
def guess_number():
    if 'random_number' not in session:
        session['random_number'] = random.randint(0, 1000)  # In case the session has expired

    random_number = session['random_number']
    session['attempts'] += 1  # Increment the attempt count

    data = request.json
    user_guess = data.get('guess')

    try:
        guess = int(user_guess)
        if guess < 0 or guess > 1000:
            return jsonify({'message': 'Please enter a number between 0 and 1000.'})

        if guess == random_number:
            message = f"Congratulations! You guessed the right number in {session['attempts']} tries."
            session['random_number'] = random.randint(0, 1000)  # Reset the number
            session['attempts'] = 0  # Reset attempts for the next game
        elif guess < random_number:
            message = "Sorry, you have to guess higher."
        else:
            message = "Sorry, you have to guess lower."

        return jsonify({'message': message, 'attempts': session['attempts']})

    except ValueError:
        return jsonify({'message': 'Invalid input. Please enter a valid number.'})


if __name__ == '__main__':
    app.run(debug=True)