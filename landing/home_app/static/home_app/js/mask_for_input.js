const input_1 = document.body.querySelector('.phone_mask');

input_1.addEventListener('keypress', (evt) => {
    if (evt.keyCode < 47 || evt.keyCode > 57) {
        evt.preventDefault();
    }
})

input_1.addEventListener('focus', () => {
    if (input_1.value.length === 0) {
        input_1.value = '+7';
        input_1.selectionStart = input_1.value.length;
    }
})

input_1.addEventListener('click', (evt) => {
    if (input_1.selectionStart < 2) {
        input_1.selectionStart = input_1.value.length;
    }
    if (evt.key === 'Backspace' && input_1.value.length <= 2) {
        evt.preventDefault();
    }
})

input_1.addEventListener('blur', () => {
    if (input_1.value === '+7') {
        input_1.value = '';
    }
})

input_1.addEventListener('keydown', (evt) => {
    if (evt.key === 'Backspace' && input_1.value.length <= 2) {
        evt.preventDefault();
    }
})