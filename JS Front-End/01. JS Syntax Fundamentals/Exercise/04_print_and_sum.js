function printAndSum(num1, num2) {
    let arr = [];
    let result = 0;

    for (let i = num1; i <= num2; i++) {
        arr.push(i);
    }

    result = arr.reduce((a, b) => a + b)

    console.log(arr.join(" "))
    console.log(`Sum: ${result}`)
}
