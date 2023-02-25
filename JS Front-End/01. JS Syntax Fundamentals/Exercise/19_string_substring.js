function substring(searchedWord, text) {
    let textSplit = text.split(" ");
    let exist = false;

    for (let word of textSplit) {
        if (word.toLowerCase() === searchedWord) {
            console.log(searchedWord)
            exist = true;
            break
        }
    }
    if (!exist) {
        console.log(`${searchedWord} not found!`)
    }
}

