function pyramid(base, increment) {
    let stone = 0;
    let marble = 0;
    let lazuli = 0;
    let gold = 0;
    let width = base;
    let length = base;
    let height = increment;
    let layer = 0;

    while (width > 0) {
        layer += 1;
        let size = width * length;
        let innerSize = ((width - 2) * (length - 2));
        let outerSize = size - innerSize;
        if (width === 1) {
            outerSize = 1
            innerSize = 0
            gold += outerSize * height
        } else if (width === 2) {
            outerSize = 4
            innerSize = 0
            gold += outerSize * height
        } else if (layer % 5 === 0) {
            lazuli += outerSize * height
        } else {
            marble += outerSize * height;
        }
        stone += innerSize * height;

        width -= 2;
        length -= 2;
    }
    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lazuli)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(layer * height)}`);
}

pyramid(11,
0.75)