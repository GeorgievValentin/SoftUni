function vacation(peopleCount, groupType, dayOfWeek) {
    let totalPrice = 0;

    switch (groupType) {
        case "Students":
            if (dayOfWeek === "Friday") {
                totalPrice = peopleCount * 8.45;
            } else if (dayOfWeek === "Saturday") {
                totalPrice = peopleCount * 9.80;
            } else {
                totalPrice = peopleCount * 10.46;
            }
            if (peopleCount >= 30) {
                totalPrice *= 0.85;
            }
            break;
        case "Business":
            if (peopleCount >= 100) {
                peopleCount -= 10;
            }
            if (dayOfWeek === "Friday") {
                totalPrice = peopleCount * 10.90;
            } else if (dayOfWeek === "Saturday") {
                totalPrice = peopleCount * 15.60;
            } else {
                totalPrice = peopleCount * 16;
            }
            break;
        case "Regular":
            if (dayOfWeek === "Friday") {
                totalPrice = peopleCount * 15;
            } else if (dayOfWeek === "Saturday") {
                totalPrice = peopleCount * 20;
            } else {
                totalPrice = peopleCount * 22.50;
            }
            if (peopleCount >= 10 && peopleCount <= 20) {
                totalPrice *= 0.95;
            }
            break;
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}
