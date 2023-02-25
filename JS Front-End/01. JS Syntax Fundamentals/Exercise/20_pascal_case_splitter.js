function pascal(text) {
    let result = text.split(/(?=[A-Z])/).join(", ")
    console.log(result)
}

pascal('SplitMeIfYouCanHaHaYouCantOrYouCan')