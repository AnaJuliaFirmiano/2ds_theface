document.addEventListener("DOMContentLoaded", function (){
    const minusButtons = document.querySelectorAll(".minus-btn");
    const plusButtons = document.querySelectorAll(".plus-btn");

    minusButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const index = button.getAttribute("data-id");
            const quantityElement = document.querySelector(`.qty:nth-child(${parseInt(index) + 1}) span`);
            let quantity = parseInt(quantityElement.textContent);
            if (quantity > 1) {
                quantity--;
                quantityElement.textContent = quantity;
            }
    });
});

plusButtons.forEach((button) => {
    button.addEventListener("click", function () {
        const index = button.getAttribute("data-id");
        const quantityElement = document.querySelector(`.qty:nth-child(${parseInt(index) + 1}) span`);
        let quantity = parseInt(quantityElement.textContent);
        quantity++;
        quantityElement.textContent = quantity;
        });
    });
});