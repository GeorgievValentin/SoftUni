function solve(text, word) {
    let words = text.split(" ")
    let counter = 0
    for (let el of words) {
        if (el === word) {
            counter++
        }
    }
    console.log(counter)
}

solve('This is a word and it also is a sentence', 'is')