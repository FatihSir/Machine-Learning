document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('guessForm');
    const resultDiv = document.getElementById('result');
    const progressBar = document.getElementById('progressBar');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const guessInput = document.getElementById('guessInput').value;

        fetch('/guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ guess: guessInput }),
        })
        .then(response => response.json())
        .then(data => {
            displayResult(data.message, data.message.includes('Tebrikler!') ? 'success' :
                data.message.includes('daha yüksek') || data.message.includes('daha düşük') ? 'warning' : 'error');

            // Tahmin ne kadar yakınsa, ilerleme çubuğu genişliğini güncelle
            updateProgressBar(guessInput, data.target);
        })
        .catch(error => {
            displayResult('Bir hata oluştu. Lütfen tekrar deneyin.', 'error');
        });
    });

    function displayResult(message, type) {
        resultDiv.textContent = message;
        resultDiv.classList.remove('success', 'error', 'warning');
        resultDiv.classList.add(type);
        resultDiv.style.display = 'block';
    }

    function updateProgressBar(guess, target) {
        const max = 1000;
        const progress = Math.abs(target - guess) / max * 100;
        progressBar.style.width = `${100 - progress}%`;
    }
});
