const VISITED_LENGTH = 4
const DIRECTION_NUM = 4
const dx = [0,0,-1,1]
const dy = [-1,1,0,0]
let N, M;
let board = []
let friendPoints=[]
let friendRoutes=[]
let visitedPoints=[]
let result = []

const input = [
    '4 2',
    '20 26 185 80',
    '100 20 25 80',
    '20 20 88 99',
    '15 32 44 50',
    '1 2',
    '2 3',
];

class Point {
    constructor(x, y) {
        this.x = x
        this.y = y
    }
    isSame(point) {
        return this.x === point.x && this.y === point.y
    }
}

class Route {
    constructor(points) {
        this.points = points.slice(0, VISITED_LENGTH)
    }
}

function setUp(input) {
    const firstLine = input.shift().split(" ").map(Number)
    N = firstLine[0]
    M = firstLine[1]
    board = Array.from({length: N}, () => Array(N).fill(0))
    for(let row=0;row<N;row++) {
        const line = input.shift().split(" ").map(Number)
        for(let col=0;col<N;col++) {
            board[row][col] = line[col]
        }
    }
    for(let j=0;j<M;j++) {
        friendRoutes.push([])
        const [y, x] = input.shift().split(" ").map((v) => parseInt(v) - 1)
        friendPoints[j] = new Point(x, y)
    }
}
function findAllFriendsRoute() {
    friendPoints.forEach((friendPoint, i) => {
        visitedPoints.push(friendPoint)
        findEachRoute(visitedPoints, i, friendPoint);
        visitedPoints = []
    })
}
function findEachRoute(visitedPoints, idx, curPoint) {
    if(visitedPoints.length === VISITED_LENGTH) {
        friendRoutes[idx].push(new Route(visitedPoints));
        return
    }
    for (let i=0;i<DIRECTION_NUM;i++) {
        let nx = curPoint.x + dx[i]
        let ny = curPoint.y + dy[i]
        if(nx>=0 && nx<N && ny>=0 && ny<N){
            const newPoint = new Point(nx, ny)
            if(!isVisited(visitedPoints, newPoint)){
                visitedPoints.push(newPoint)
                findEachRoute(visitedPoints, idx, newPoint)
                visitedPoints.pop()
            }

        }
    }
}
function isVisited(visitedPoints, curPoint) {
    return visitedPoints.some((point) => curPoint.isSame(point))
}
function findRouteCombination(idx, routes) {
    if (idx === M) {
        result.push(getTotal(routes))
        return;
    }
    for(const route of friendRoutes[idx]){
        routes.push(route)
        findRouteCombination(idx+1, routes)
        routes.pop()
    }
}
function getTotal(routes) {
    let total = 0;
    const copyBoard = board.map(row => row.slice())
    for (const route of routes) {
        for (const point of route.points) {
            total += copyBoard[point.y][point.x]
            copyBoard[point.y][point.x] = 0
        }
    }
    return total
}
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    setUp(input)
    findAllFriendsRoute()
    for (let i = 0; i < M; i++) {
        findRouteCombination(i, []);
    }
    console.log(Math.max(...result))
})