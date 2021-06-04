//
// Exercice n°2 - 3, 2, 1... Décollage !
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice2', dataset)

//
// Resolve function
//
function resolve(){
    let pseudos = input.slice(1)

    let count = countNames(pseudos)
    let doubleName = count.filter(n => n[1] === 2)[0][0]

    console.log(`-----------------------------`)
    console.log(`Exervice n°2`)
    console.log(`Result ${doubleName}`)
    console.log(`Solution: ${output}`)
    console.log(`-----------------------------`)
}
resolve()

//
// Methods 
//
function countNames(names){
    let count = {}
    for (let name of names){
        if (count[name]){
            count[name] ++
        } else {
            count[name] = 1
        }
    }
    return Object.entries(count)
}