function CookingByNumbers(numAsStr, ...actions) {
    let num = Number(numAsStr);

    actions.forEach((action) => {
        if (action === "chop") {
            num /= 2;
        } else if (action === "dice") {
            num = Math.sqrt(num);
        } else if (action === "spice") {
            num += 1;
        } else if (action === "bake") {
            num *= 3;
        } else {
            num *= 0.8
        }
         console.log(num)
    })
}
