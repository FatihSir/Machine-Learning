document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('guessForm');
    const resultDiv = document.getElementById('result');

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
            displayResult(data.message, data.message.includes('Congratulations!') ? 'success' :
                data.message.includes('higher') || data.message.includes('lower') ? 'warning' : 'error');
        })
        .catch(error => {
            displayResult('An error occurred. Please try again.', 'error');
        });
    });

    function displayResult(message, type) {
        resultDiv.textContent = message;
        resultDiv.classList.remove('success', 'error', 'warning');
        resultDiv.classList.add(type);
        resultDiv.style.display = 'block';
    }
});