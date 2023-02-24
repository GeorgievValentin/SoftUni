function radar(speed, area) {
    let limits = {
        "motorway": 130,
        "interstate": 90,
        "city": 50,
        "residential": 20
    }
    let diff = Math.abs(speed - limits[area]);
    let status = "";

    if (diff <= 20) {
        status = "speeding";
    } else if (diff > 20 && diff <= 40) {
        status = "excessive speeding";
    } else {
        status = "reckless driving";
    }

    if (speed <= limits[area]) {
        console.log(`Driving ${speed} km/h in a ${limits[area]} zone`)
    } else {
        console.log(`The speed is ${diff} km/h faster than the allowed speed of ${limits[area]} - ${status}`)
    }
}
