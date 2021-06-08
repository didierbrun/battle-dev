//
// Exercice n°5 - Ceinture d'astéroïdes
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice5', dataset)

//
// Solution input1.txt : [ 1, 16, 31, 46, 62, 77, 92 ] => Total 249 / Dif 198
//

//
// Resolve function
//
function resolve(){

    const [length, duration, locked] = input[0].split(' ').map(o => +o)
    const asteroids = input[1].split(' ').map(o => +o)
    
    let cumul = cumulWindow(asteroids, duration)

    let nbmax = Math.ceil(length / (duration + locked))

    for (let i = 0; i < 100; i++){
        cumul.list.push(0)
    }

    let combine = 0

    let maxVal = 0

    let list = []

    for (let a = 0; a < 15; a++){
        for (let b = 0; b < 15; b++){
            for (let c = 0; c < 15; c++){
                for (let d = 0; d < 15; d++){
                    for (let e = 0; e < 15; e++){
                        for( let f = 0; f < 15; f++){
                            for (let g = 0; g < 15; g++){
                                let val = cumul.list[a] 
                                val += cumul.list[a + duration + locked + b]
                                val += cumul.list[a + duration + locked + b + duration + locked + c]
                                val += cumul.list[a + duration + locked + b + duration + locked + c + duration + locked + d]
                                val += cumul.list[a + duration + locked + b + duration + locked + c + duration + locked + d + duration + locked + e]
                                val += cumul.list[a + duration + locked + b + duration + locked + c + duration + locked + d + duration + locked + e + duration + locked + f]
                                val += cumul.list[a + duration + locked + b + duration + locked + c + duration + locked + d + duration + locked + e + duration + locked + f + duration + locked + g]
                                if (val >= maxVal){
                                    maxVal = val
                                    list.push({o:[
                                        a,
                                        a + duration + locked + b,
                                        a + duration + locked + b + duration + locked + c,
                                        a + duration + locked + b + duration + locked + c + duration + locked + d,
                                        a + duration + locked + b + duration + locked + c + duration + locked + d + duration + locked + e,
                                        a + duration + locked + b + duration + locked + c + duration + locked + d + duration + locked + e + duration + locked + f,
                                        a + duration + locked + b + duration + locked + c + duration + locked + d + duration + locked + e + duration + locked + f + duration + locked + g
                                    ], val: maxVal})
                                }
                            }
                        }
                    }
                }
            }
        }
    }



    console.log(list)

    console.log(cumul.total, maxVal, cumul.total - maxVal)
    

    console.log(`-----------------------------`)
    console.log(`Exervice n°5`)
    console.log(`Solution: ${output}`)
    console.log(`-----------------------------`)
}
resolve()

//
// Methods
//

function maxTiers(from, a, b, datas, dur, lock){

    let maxVal = 0
    let indices = []
    let total = 0

    for (let x = 0; x < a; x++){
        for (let y = 0; y < b; y++){
            //console.log(`(${x},${y}) I ${from + x} - ${from + x + dur + lock + y}`)
            let px = from + x < datas.length ? datas[from + x] : 0
            let py = from + x + dur + lock + y < datas.length ? datas[from + x + dur + lock + y] : 0 
            let val = px + py
            if (val > maxVal){
                maxVal = val
                total = px
                indices = [from + x, from + x + dur + lock + y]
            }
        }
    }

    return {
        maxVal,
        indices,
        total
    }
}

function cumulWindow(datas, winSize){
    let list = new Array(datas.length).fill(0)
    let total = 0

    for (let i = 0; i < list.length; i++){
        for (let j = 0; j < winSize; j++){
            if ((i -j) >= 0){
                list[i - j] += datas[i]
            }
        }
        total += datas[i]
    }

    return {
        list,
        total
    }
}

function maxInWindow(datas, from, winSize){
    console.log(`max from ${from}`)
    let max = -1
    let maxIndex = null
    for (let i = from; i < from + winSize; i++){
        if (datas[i] > max){
            max = datas[i]
            maxIndex = i
        }
    }
    return {
        index: maxIndex,
        value: max
    }
}