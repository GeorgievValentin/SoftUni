function hashTag(text) {
    let textSplit = text.split(" ");
    let words = [];

    textSplit.forEach(word => {
        if (word.startsWith("#") && word.length > 1 && (!/[^a-z]/i.test(word.slice(1)))) {
           console.log(word.slice(1))
        }
    })
}
