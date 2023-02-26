function login(inputArr) {
    let userName = inputArr.shift();
    let password = userName.split("").reverse().join("")

    for (let i = 1; i <= 4; i++) {
        if (inputArr.shift() === password) {
            console.log(`User ${userName} logged in.`);
            break
        } else {
            if (i < 4) {
                console.log("Incorrect password. Try again.")
            } else {
                console.log(`User ${userName} blocked!`)
            }
        }
    }
}
login(['sunny','rainy','cloudy','sunny','not sunny'])