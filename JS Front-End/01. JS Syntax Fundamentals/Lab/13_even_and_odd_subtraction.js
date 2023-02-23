function solve(arr) {
    let evenArr = [0]
    let oddArr = [0]
    let evenSum = 0
    let oddSum = 0

    for (let number of arr) {
        if (number % 2 === 0) {
            evenArr.push(number)
        } else {
            oddArr.push(number)
        }
    }
    evenSum = evenArr.reduce((a, b) => a + b)
    oddSum = oddArr.reduce((a, b) => a + b)

    let result = evenSum - oddSum

    console.log(result)
}

solve([2,4,6,8,10])