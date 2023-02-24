function fruits(fruit, weightGrams, price) {
    let kilograms = weightGrams / 1000
    let cost = kilograms * price

    console.log(`I need $${cost.toFixed(2)} to buy ${kilograms.toFixed(2)} kilograms ${fruit}.`)
}
