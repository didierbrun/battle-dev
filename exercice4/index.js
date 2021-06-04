//
// Exercice n°4 - Nettoyeur de l'espace
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice4', dataset)

//
// Resolve function
//
function resolve(){
    let length = Math.floor(input[0])
    let debrits = input[1].split('')
    let total = cumulate(debrits, 0, length)
    let initial = cumulate(debrits, 0, length / 2)
    let count = 0

    for (let i = 0; i < length / 2; i++){
        let result = compare(initial, total)
        if (result)count++
        add(debrits[i + length / 2], initial)
        remove(debrits[i], initial)
    }

    console.log(`-----------------------------`)
    console.log(`Dataset: ${dataset}`)
    console.log(`Entries: ${length}`)
    console.log(`Result: ${count * 2}`)
    console.log(`Solution: ${output}`)
    console.log(`-----------------------------`)
}
resolve()

//
// Methods
//
function compare(a, b){
    for (let z in a){
        if (a[z] * 2 !== b[z])return false
    }
    return true
}

function cumulate(datas, from, length){
    return datas.slice(from, length).reduce((a, c) => {
        if (a[c]){
            a[c] ++
        } else {
            a[c] = 1
        }
        return a
    }, {}) 
}

function add(l, datas){
    if (datas[l]){
        datas[l] ++
    } else {
        datas[l] = 1
    }
}

function remove(l, datas){
    if (datas[l]){
        datas[l] --
        if (datas[l] === 0)delete(datas[l])
    }
}

