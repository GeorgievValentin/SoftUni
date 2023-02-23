function solve(num) {
    let area = 0
    if (typeof num === "number") {
        area = Math.PI * num**2
        console.log(area.toFixed(2))
    }
    else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof num}.`)
    }
}
