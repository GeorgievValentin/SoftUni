function solve(num) {
    const months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    if (num in months) {
        console.log(months[num])
    } else {
        console.log("Error!")
    }
}

solve(-1)
solve(1)
solve(12)
solve(13)



