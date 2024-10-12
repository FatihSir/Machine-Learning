// static/js/script.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', (event) => {
        const totalBill = parseFloat(document.getElementById('total_bill').value);
        const size = parseInt(document.getElementById('size').value);
        
        // Validate total_bill
        if (isNaN(totalBill) || totalBill <= 0) {
            alert('Please enter a valid total bill amount.');
            event.preventDefault(); // Prevent form submission
            return;
        }

        // Validate size
        if (isNaN(size) || size <= 0) {
            alert('Please enter a valid party size.');
            event.preventDefault(); // Prevent form submission
            return;
        }

    });
});

