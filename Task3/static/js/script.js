document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('priceForm');

    form.addEventListener('submit', (event) => {
        const size = parseFloat(document.getElementById('size').value);
        const bedrooms = parseInt(document.getElementById('bedrooms').value);

        // Validate size
        if (isNaN(size) || size <= 0) {
            alert('Please enter a valid property size.');
            event.preventDefault(); // Prevent form submission
            return;
        }

        // Validate bedrooms
        if (isNaN(bedrooms) || bedrooms <= 0) {
            alert('Please enter a valid number of bedrooms.');
            event.preventDefault(); // Prevent form submission
            return;
        }
    });
});
