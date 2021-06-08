//
// Exercice n°1 - Préparation minitieuse
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice1', dataset)

//
// Resolve function
//
function resolve(){

    const ergoPerUa = 5 

    const ergolMass = +input[0]
    const distance = +input[1]
    const mass = ergolMass + distance * ergoPerUa

    console.log(`-----------------------------`)
    console.log(`Exervice n°1`)
    console.log(`Dataset: ${dataset}`)
    console.log(`Result: ${mass}`)
    console.log(`Solution: ${output}`)
    console.log(`-----------------------------`)
}
resolve()