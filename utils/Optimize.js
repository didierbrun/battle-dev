/**
 * Ex : memoizeReduce([32, 16], [...], () => {})
 */
function memoizeReduce(windows, datas, reduce){
    let counts = new Array(windows.length).fill(0)
    let values = new Array(windows.length).fill().map(_=>[{}])
    let total = {}
    for (let d of datas){
        if (total[d] == undefined){
            total[d] = 1
        } else {
            total[d] ++
        }
        for (let i = 0; i < windows.length; i++){
            reduce(values[i][values[i].length - 1], d)
            counts[i]++
            if (counts[i] >= windows[i]){
                counts[i] = 0
                values[i].push({})
            }
        }
    }
    for (let i = 0; i < windows.length; i++)values[i].pop()
    return {
        values,
        total
    }
}

/**
 * Ex : windowRanges([32, 16], 0, 80)
 */
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

module.exports = (path, number) => {
    windowRanges,
    memoizeReduce
}