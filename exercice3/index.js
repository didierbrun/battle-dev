//
// Exercice n°3 - Tetris Bot 1.0
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice3', dataset)

//
// Resolve function
//
function resolve(){

    let solution = null

    for (let i = 0; i < input[0].length; i++){
        let first = firstFreeRow(i)

        if (first >= 3){
            let count = 0
            for (let i = 0; i >= -3; i--){
                if (countRow(first + i) === input[0].length - 1)count++
            }

            if (count === 4)solution = i + 1
        }
    }

    console.log(`-----------------------------`)
    console.log(`Exervice n°3`)
    console.log(`Result: ${solution ? `BOOL ${solution}`:`NOPE`}`)
    console.log(`Solution: ${output}`)
    console.log(`-----------------------------`)
}
resolve()

//
// Methods 
//
function firstFreeRow(column){
    let index = 0
    for (let i = 0; i < input.length; i++){
        if (input[i].charAt(column) === '#')return i - 1
    }
    return input.length - 1
}

function countRow(row){
    return input[row].split('').reduce((a, c) => c === '#' ? a + 1 : a, 0)
}
