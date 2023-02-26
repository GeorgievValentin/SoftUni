function mine(amount) {
    let totalDays = 0;
    let crewConsume = 26;
    let dayDrop = 10;
    let production = 0;

    while (amount >= 100) {
        totalDays += 1;
        production += amount;
        production -= crewConsume;
        amount -= dayDrop;
    }
    if (production >= crewConsume) {
        production -= crewConsume;
    } else {
        production = 0;
    }

    console.log(totalDays);
    console.log(production);
}
