function words(words, text) {
    let wordsSplit = words.split(", ");
    let textSplit = text.split(" ");

    wordsSplit.forEach(word => {
        textSplit.forEach(el => {
            if (el.startsWith("*") && el.length === word.length) {
                text = text.replace(el, word)
            }
        })
    })
    console.log(text)
}
