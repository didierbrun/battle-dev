//
// Exercice n°5 - Ceinture d'astéroïdes
//
const dataset = process.argv.length > 2 ? process.argv[2] : 1
const { input, output } = require('../utils/InputReader')('./exercice5', dataset)

//
// Resolve function
//
function resolve(){

    const [length, duration, locked] = input[0].split(' ').map(o => +o)
    const asteroids = input[1].split(' ').map(o => +o)
    
    let dp = new Array(length + duration + locked + 1).fill().map(o => 0)
    let debris = asteroids.slice(0, duration).reduce((c, v) => c + v, 0)
    let total = asteroids.reduce((c, v) => c + v, 0)

    for (let i = 0; i < length; i++){
        dp[i + 1] = Math.max(dp[i + 1], dp[i])
        dp[i + duration + locked] = dp[i] + debris
        debris += i + duration < length ? asteroids[i + duration] : 0
        debris -= asteroids[i]
    }

    console.log(`-----------------------------`)
    console.log(`Exervice n°5`)
    console.log(`Result: ${total - Math.max(...dp)}`)
    console.log(`Solution: ${output}`)
    console.log(`-----------------------------`)
}
resolve()