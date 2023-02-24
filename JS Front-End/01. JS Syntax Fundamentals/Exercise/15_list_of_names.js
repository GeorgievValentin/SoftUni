function sortNames(names) {
    names.sort((a, b) => a.localeCompare(b))
    let n = 1
    names.forEach(name => {
        console.log(`${n}.${name}`)
        n += 1;
    })
}
