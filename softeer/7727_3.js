const input = [
    '4 2',
    '20 26 185 80',
    '100 20 25 80',
    '20 20 88 99',
    '15 32 44 50',
    '1 2',
    '2 3',
];
const MAX_LENGTH = 4;
const MAX_DIRECTION = 4;
let dx = [0,0,-1,1]
let dy = [-1,1,0,0]
let N, M;
let board = [];
let friendFirstPoint = [];
let friendRoutes = [];
let vistedPoints = [];
let result = []

class Point {
  constructor(x,y) {
    this.x = x;
    this.y = y;
  }
  isSame(point) {
    return this.x === point.x && this.y === point.y
  }
}

class Route {
  constructor(points) {
    this.points = points.slice(0, MAX_LENGTH)
  }
}
function setUp(input) {
  const firstLine = input.shift().split(" ").map(Number)
  N = firstLine[0]
  M = firstLine[1]
  board = Array.from({length: N}, () => Array(N).fill(0))
  for(let i=0;i<N;i++) {
    line = input.shift().split(" ").map(Number)
    for(let j=0;j<N;j++) {
      board[i][j] = line[j]
    }
  }
  for(let i=0;i<M;i++) {
    line = input.shift().split(" ").map(Number)
    friendFirstPoint.push(new Point(line[1]-1, line[0]-1))
    friendRoutes.push([])
  }
}
function isVisited(vistedPoints, curPoint) {
  return vistedPoints.some((point) => curPoint.isSame(point))
} 
function findAllFriendsRoute() {
  friendFirstPoint.forEach((point, i) => {
    vistedPoints.push(point)
    findEachRoute(vistedPoints, i, point)
    vistedPoints = []
  })
}

function findEachRoute(vistedPoints, idx, curPoint) {
  if(vistedPoints.length === MAX_LENGTH) {
    friendRoutes[idx].push(new Route(vistedPoints))
    return;
  }

  for(let i=0;i<MAX_DIRECTION;i++) {
    nx = curPoint.x + dx[i]
    ny = curPoint.y + dy[i]

    if(nx>=0 && nx<N && ny>=0 && ny<N) {
      const newPoint = new Point(nx, ny)
      if(!isVisited(vistedPoints, newPoint)){
        vistedPoints.push(newPoint)
        findEachRoute(vistedPoints, idx, newPoint)
        vistedPoints.pop()
      } 
    }
  }
}
function getTotal(routes) {
  let total = 0
  const copyBoard = board.map(row => row.slice())
  for(const route of routes) {
    for(const point of route.points) {
      total += copyBoard[point.y][point.x]
      copyBoard[point.y][point.x] = 0
    }
  }
  return total
}
function findResult(idx, routes) {
  if(idx === M) {
    result.push(getTotal(routes))
    return
  }
  for(const route of friendRoutes[idx]) {
    routes.push(route)
    findResult(idx+1, routes)
    routes.pop()
  }
}
setUp(input)
findAllFriendsRoute()
findResult(0, [])
console.log(Math.max(...result))