function sortNumbers(numbers) {
    let resultArr = [];
    let nums = [...numbers.sort((a, b) => a - b)];

    while (nums.length > 0) {
        resultArr.push(nums.shift());
        resultArr.push(nums.pop());
    }
   return resultArr;
}

sortNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])