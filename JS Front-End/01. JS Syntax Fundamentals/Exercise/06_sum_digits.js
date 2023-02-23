function sumDigits(number) {
    let result = 0;
    result = String(number).split("").map(Number).reduce((a, b) => a + b)

    console.log(result)
}