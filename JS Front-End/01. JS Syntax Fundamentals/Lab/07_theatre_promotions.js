function solve(dayType, age) {
    let price = 0
    if (age >= 0 && age <= 18) {
        if (dayType === "Weekday") {
            price = 12;
        }
        else if (dayType === "Weekend") {
            price = 15;
        }
        else {
            price = 5;
        }
         console.log(`${price}$`)
    }
    else if (age >18 && age <= 64) {
        if (dayType === "Weekday") {
            price = 18;
        }
        else if (dayType === "Weekend") {
            price = 20;
        }
        else {
            price = 12;
        }
         console.log(`${price}$`)
    }
    else if (age > 64 && age <= 122){
         if (dayType === "Weekday") {
            price = 12
        }
        else if (dayType === "Weekend") {
            price = 15
        }
        else {
            price = 10
        }
         console.log(`${price}$`)
    }
    else {
         console.log("Error!")
    }
}