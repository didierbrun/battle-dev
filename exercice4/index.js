//
// Read the datas 
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice4', dataset)

//
// Resolve function
//
function resolve(){
    const datas = parseDatas(input)
    const windows = [65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4]

    let memo = memoizeReduce(windows, datas.debris, reduceOrbit)
    
    let total = 0

    for (let i = 0; i < datas.length / 2; i++){

        let r0 = clampRanges(i, datas.length / 2, datas.length)
        let r1 = clampRanges(i + datas.length / 2, datas.length / 2, datas.length)

        let cumul0 = {}
        let cumul1 = {}

        for (let r of r0){
            mergeOnFirst(cumul0, cumulate(datas.debris, windowRanges(windows, r.from, r.length), memo))
        }

        for (let r of r1){
            mergeOnFirst(cumul1, cumulate(datas.debris, windowRanges(windows, r.from, r.length), memo))
        }

        if (compare(cumul0, cumul1))total++

    }

    console.log("---------------------------------------------------")
    console.log(`Dataset n°${dataset}`)
    console.log(`Number of entries: ${datas.length}`)
    console.log(`Result: ${total > 0 ? total * 2 : 0}`)
    console.log(`Solution: ${output}`)
    console.log("---------------------------------------------------")

}
resolve()

//
// Methods
//
function parseDatas(_input){
    return {
        length: parseInt(_input[0]),
        debris: _input[1].split('')
    }
}

function compare(a, b){
    for (let z in b){
        if (a[z] !== b[z])return false
    }
    return true
}

function mergeOnFirst(a, b){
    for (let z in b){
        if (a[z] === undefined){
            a[z] = b[z]
        } else {
            a[z] += b[z]
        }
    }
}

function clampRanges(from, length, size){
    if (from + length > size){
        return[
            { from, length: size - from },
            { from: 0, length: length - (size - from)} 
        ]
    } else {
        return[{ from, length }]
    }
}

function cumulate(debris, ranges, memo){
    let result = {}
    for (let i = 0; i < ranges.sections.length; i++){
        if (ranges.sections[i].length > 0){
            for (let z of ranges.sections[i]){
                for (let d in memo[i][z]){
                    if (result[d] === undefined){
                        result[d] = memo[i][z][d]
                    } else {
                        result[d] += memo[i][z][d]
                    }
                }
            }
        }
    }
    if (ranges.parts.length > 0){
        for (let p of ranges.parts){
            for (let i = p.from; i < p.from + p.length; i++){
                let d = debris[i]
                if (result[d] === undefined){
                    result[d] = 1
                } else {
                    result[d] ++
                }
            }
        }
    }
    return result
}

function memoizeReduce(levels, datas, reduce){
    let counts = new Array(levels.length).fill(0)
    let values = new Array(levels.length).fill().map(_=>[{}])
    for (let d of datas){
        for (let i = 0; i < levels.length; i++){
            reduce(values[i][values[i].length - 1], d)
            counts[i]++
            if (counts[i] >= levels[i]){
                counts[i] = 0
                values[i].push({})
            }
        }
    }
    for (let i = 0; i < levels.length; i++)values[i].pop()
    return values
}

function reduceOrbit(accumulator, currentValue){
    accumulator[currentValue] !== undefined ? accumulator[currentValue]++ : accumulator[currentValue] = 1
}

function windowRanges(windows, from, length){
    let parts = new Array(windows.length + 1).fill().map(_ => [])
    let sections = new Array(windows.length).fill().map(_ => [])
    parts[0].push({ from, length })

    for (let i = 0; i < windows.length; i++){
        let w = windows[i]
        for (let p of parts[i]){
            let d0 = Math.ceil(p.from / w)
            let d1 = Math.floor((p.from + p.length) / w)
            if (d1 > d0){
                if (p.from < d0 * w)parts[i + 1].push({ from: p.from, length: d0 * w - p.from})
                if (d1 * w < p.from + p.length)parts[i + 1].push({ from: d1 * w, length: p.from + p.length - d1 * w})
                for (let s = d0; s < d1; s++)sections[i].push(s)
            } else {
                parts[i + 1].push({from: p.from, length: p.length})
            }
        }
    }
    return {
        sections, 
        parts: parts[parts.length - 1]
    }
}



