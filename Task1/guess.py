from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Oturum için gizli anahtar


# Ana sayfa rotası
@app.route('/')
def index():
    session['random_number'] = random.randint(0, 1000)  # Başlangıçta yeni bir rastgele sayı oluştur
    session['attempts'] = 0  # Deneme sayısını sıfırla
    return render_template('index.html')


# Tahmin rotası
@app.route('/guess', methods=['POST'])
def guess_number():
    if 'random_number' not in session:
        session['random_number'] = random.randint(0, 1000)  # Oturum sona erdiyse yeni bir rastgele sayı oluştur

    random_number = session['random_number']
    session['attempts'] += 1  # Deneme sayısını artır

    data = request.json
    user_guess = data.get('guess')

    try:
        guess = int(user_guess)
        if guess < 0 or guess > 1000:
            return jsonify({'message': 'Lütfen 0 ile 1000 arasında bir sayı girin.'})

        if guess == random_number:
            message = f"Tebrikler! {session['attempts']} denemede doğru sayıyı tahmin ettiniz."
            session['random_number'] = random.randint(0, 1000)  # Sayıyı sıfırla
            session['attempts'] = 0  # Bir sonraki oyun için denemeleri sıfırla
        elif guess < random_number:
            message = "Üzgünüz, daha yüksek bir sayı tahmin etmelisiniz."
        else:
            message = "Üzgünüz, daha düşük bir sayı tahmin etmelisiniz."

        return jsonify({'message': message, 'attempts': session['attempts']})

    except ValueError:
        return jsonify({'message': 'Geçersiz giriş. Lütfen geçerli bir sayı girin.'})


if __name__ == '__main__':
    app.run(debug=True)
