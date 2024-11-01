// const readline = require("readline")

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// })
// input = []
input = [
    '4',
    '2 1 3 3',
    '5 1 2 1',
    '2 1 2 3',
    '5 1 1 1',
]
// rl.on("line", (line) => {
//     input.push(line)
// }).on("close", () => {
//     main(input)
// })

let N, ans;
let map = [];
let isVisited;
const dirX = [0, 1];
const dirY = [1, 0];
main(input)
function main(input) {
    N = input.shift().split("").map(Number)
    ans = -1
    isVisited = Array.from({ length: N }, () => Array(N).fill(false));

    for(let i=0;i<N;i++){
        line = input.shift().split(" ").map(Number)
        map.push(line)
    }
    solution();
}
function solution(){
    let maxDepth = 4;
    if (N === 2) {
        maxDepth = 2;
    }

    DFS(0, 0, maxDepth);
    console.log(ans);
}
function DFS(depth, sum, maxDepth) {
    if (depth === maxDepth) {
        ans = Math.max(ans, sum);
        return;
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (isVisited[i][j]) continue;

            for (let k = 0; k < 2; k++) {
                const nextX = dirX[k] + i;
                const nextY = dirY[k] + j;

                if (!isAble(nextX, nextY)) continue;

                isVisited[i][j] = true;
                isVisited[nextX][nextY] = true;
                DFS(depth + 1, sum + map[i][j] + map[nextX][nextY], maxDepth);
                isVisited[i][j] = false;
                isVisited[nextX][nextY] = false;
            }
        }
    }
}

function isAble(nextX, nextY) {
    return nextX >= 0 && nextX < N && nextY >= 0 && nextY < N && !isVisited[nextX][nextY];
}