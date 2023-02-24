function arrRotation([...nums], rotations) {
    nums.map(Number);

    for (let i = 1; i <= rotations; i++) {
        nums.push(nums.shift())
    }
    console.log(nums.join(" "))
}
