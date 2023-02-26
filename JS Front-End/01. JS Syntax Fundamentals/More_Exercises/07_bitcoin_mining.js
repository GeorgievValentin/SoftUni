function mining(shiftArr) {
    let bitcoinPrice = 11949.16;
    let goldPrice = 67.51;
    let amountBitcoin = 0;
    let fiatMoney = 0;
    let bitcoinDay = 0;
    let dayCounter = 0;

    for (let shift of shiftArr) {
        dayCounter += 1;
        if (!amountBitcoin) {
            bitcoinDay += 1;
        }
        if (dayCounter % 3 === 0) {
            fiatMoney += shift * goldPrice * 0.7;
        } else {
            fiatMoney += shift * goldPrice;
        }
        if (fiatMoney >= bitcoinPrice) {
            amountBitcoin += Math.floor(fiatMoney / bitcoinPrice);
            fiatMoney %= bitcoinPrice;
        }
    }
    console.log(`Bought bitcoins: ${amountBitcoin}`)
    if (amountBitcoin) {
        console.log(`Day of the first purchased bitcoin: ${bitcoinDay}`)
    }
    console.log(`Left money: ${fiatMoney.toFixed(2)} lv.`)
}
