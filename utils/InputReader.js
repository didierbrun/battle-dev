const fs = require('fs')

module.exports = (path, number) => {
    try {
        let input = fs.readFileSync(`${path}/datas/input${number}.txt`, 'utf8').split('\n')
        let output = fs.readFileSync(`${path}/datas/output${number}.txt`, 'utf8').split('\n')
        return {
            input,
            output
        }
    } catch (err) {
    }
}