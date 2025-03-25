const display = document.querySelector('#display');
const buttons = document.querySelectorAll('button');

buttons.forEach((item) => {
    item.onclick = () => {
        if (item.id == 'clear') {
            display.innerText = '';
        } else if (item.id == 'backspace') {
            let string = display.innerText.toString();
            display.innerText = string.substr(0, string.length - 1);
        } else if (display.innerText != '' && item.id == 'equal') {
            display.innerText = sequentialEvaluate(display.innerText);
        } else if (display.innerText == '' && item.id == 'equal') {
            display.innerText = 'Empty!';
            setTimeout(() => (display.innerText = ''), 2000);
        } else {
            display.innerText += item.id;
        }
    };
});

// Function to evaluate expressions sequentially (left-to-right)
function sequentialEvaluate(expression) {
    let tokens = expression.match(/(\d+|\D)/g); // Split numbers and operators
    if (!tokens) return '';

    let result = parseFloat(tokens[0]); // Start with the first number

    for (let i = 1; i < tokens.length; i += 2) {
        let operator = tokens[i];
        let nextNumber = parseFloat(tokens[i + 1]);

        if (!isNaN(nextNumber)) {
            if (operator == '+') result += nextNumber;
            else if (operator == '-') result -= nextNumber;
            else if (operator == '*') result *= nextNumber;
            else if (operator == '/') result /= nextNumber;
        }
    }

    return result;
}