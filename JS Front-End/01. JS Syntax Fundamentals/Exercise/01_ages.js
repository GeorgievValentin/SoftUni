function getAge(ages) {
    let age = "";

    if (ages >= 0 && ages <= 2) {
        age = "baby";
    } else if (ages >= 3 && ages <= 13) {
        age = "child";
    } else if (ages >= 14 && ages <= 19) {
        age = "teenager";
    } else if (ages >= 20 && ages <= 65) {
        age = "adult";
    } else if (ages >= 66) {
        age = "elder";
    } else {
        age = "out of bounds"
    }
    console.log(age)
}
