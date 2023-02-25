function calculate(num1, operation, num2) {
    let operations = {
        "+": num1 + num2,
        "-": num1 - (num2),
        "*": (num1) * (num2),
        "/": (num1) / (num2),
    }
    let result = operations[operation].toFixed(2)
    console.log(result)
}
