function valid(x1, y1, x2, y2) {
    let coordinates = [[x1, y1, 0, 0], [x2, y2, 0, 0], [x1, y1, x2, y2]]
    coordinates.forEach(el => {
        [x1, y1, x2, y2] = el;
        let check = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
        if (Number.isInteger(check)) {
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
        } else {
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
        }
    });
}