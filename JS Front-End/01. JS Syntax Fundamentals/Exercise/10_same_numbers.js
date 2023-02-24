function sameNumbers(number) {
    let nums = String(number).split("").map(Number);
    let same = "true"
    let result = 0

    for (let num of nums) {
        if (nums[0] !== num) {
            same = "false";
            break
        }
    }
    result = nums.reduce((a, b) => a + b)
    console.log(same)
    console.log(result)
}
