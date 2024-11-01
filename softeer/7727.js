const readline = require("readline");

const VISITED_POINT = 4;
const DIRECT_NUMBER = 4;
const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
let board;
let N, M;
let friendPoints = [];
let visitedPoints = [];
let friendsRoutes = [];
let result = [];

class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    isSame(point) {
        return this.x === point.x && this.y === point.y;
    }
}

class Route {
    constructor(points) {
        this.points = points.slice(0, VISITED_POINT);
    }
}

function setUp(input) {
    const firstLine = input.shift().split(" ");
    N = parseInt(firstLine[0]);
    M = parseInt(firstLine[1]);
    board = Array.from({ length: N }, () => Array(N).fill(0));
    console.log("N M", N,M)
    console.log("Board", board)
    friendPoints = new Array(M);
    console.log("Friends-Points", friendPoints)
    for (let row = 0; row < N; row++) {
        const line = input.shift().split(" ").map(Number);
        for (let col = 0; col < N; col++) {
            board[row][col] = line[col];
        }
    }
    console.log("Board2", board)
    for (let i = 0; i < M; i++) {
        friendsRoutes.push([]);
        const [y, x] = input.shift().split(" ").map(v => parseInt(v) - 1);
        friendPoints[i] = new Point(x, y);
    }
    console.log("Friends-Points2", friendPoints)
}

function findAllFriendRoutes() {
    friendPoints.forEach((friendPoint, i) => {
        visitedPoints.push(friendPoint);
        // console.log("V1", visitedPoints)
        findEachFriendRoutes(visitedPoints, i, friendPoint);
        // console.log("V6", visitedPoints)
        visitedPoints = [];
        // console.log("V7", visitedPoints)
    });
}

function findEachFriendRoutes(visitedPoints, idx, currentPoint) {
    if (visitedPoints.length === VISITED_POINT) {
        // console.log("R1",friendsRoutes[idx])
        friendsRoutes[idx].push(new Route(visitedPoints));
        // console.log("R2",friendsRoutes[idx])
        return;
    }

    for (let i = 0; i < DIRECT_NUMBER; i++) {
        const nx = currentPoint.x + dx[i];
        const ny = currentPoint.y + dy[i];

        if (0 <= nx && nx < N && 0 <= ny && ny < N) {
            const newPoint = new Point(nx, ny);
            if (!isVisited(visitedPoints, newPoint)) {
                visitedPoints.push(newPoint);
                // console.log("V3", visitedPoints)
                findEachFriendRoutes(visitedPoints, idx, newPoint);
                // console.log("V4", visitedPoints)
                visitedPoints.pop();
                // console.log("V5", visitedPoints)
            }
        }
    }
}

function isVisited(visitedPoints, point) {
    return visitedPoints.some(visitedPoint => point.isSame(visitedPoint));
}

function findRouteCombination(friendIndex, routes) {
    if (friendIndex === M) {
        result.push(getTotalFruits(routes));
        return;
    }

    for (const route of friendsRoutes[friendIndex]) {
        routes.push(route);
        findRouteCombination(friendIndex + 1, routes);
        routes.pop();
    }
}

function getTotalFruits(routes) {
    let total = 0;
    const copyBoard = board.map(row => row.slice());
    // console.log("Test Check1", board)
    // console.log("Test Check2", copyBoard)
    for (const route of routes) {
        for (const point of route.points) {
            total += copyBoard[point.y][point.x];
            copyBoard[point.y][point.x] = 0;
        }
    }

    return total;
}

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// const input = [
//     '4 1',
//     '20 26 185 80',
//     '100 20 25 80',
//     '20 20 88 99',
//     '15 32 44 50',
//     '1 2',
// ];

// const input = [
//     '4 2',
//     '20 26 185 80',
//     '100 20 25 80',
//     '20 20 88 99',
//     '15 32 44 50',
//     '1 2',
//     '2 3',
// ];
rl.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    setUp(input);
    findAllFriendRoutes();

    for (let i = 0; i < M; i++) {
        findRouteCombination(i, []);
    }

    console.log(Math.max(...result));
});
