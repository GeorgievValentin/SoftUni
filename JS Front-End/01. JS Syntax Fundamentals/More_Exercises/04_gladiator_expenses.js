function gladiator(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let costs = 0;
    let breakShield = 0;

    for (let i = 1; i <= lostFights; i++) {
        if ( i % 2 === 0) {
            costs += helmetPrice;
        } if (i % 3 === 0) {
            costs += swordPrice;
        } if (i % 2 === 0 && i % 3 === 0) {
            costs += shieldPrice;
            breakShield += 1;
            if (breakShield % 2 === 0) {
            costs += armorPrice
        }
        }
    }
    console.log(`Gladiator expenses: ${costs.toFixed(2)} aureus`)
}

gladiator(7,
2,
3,
4,
5)