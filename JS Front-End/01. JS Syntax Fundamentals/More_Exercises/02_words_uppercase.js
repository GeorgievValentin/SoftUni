function upper(text) {
    let result = text.match(/[a-zA-Z0-9]+/g).join(", ");
    console.log(result.toUpperCase())
}

upper("Hi, how are you?")