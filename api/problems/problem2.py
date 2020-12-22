
def resolve(input):
    obstacles = {}
    list_input = input.split("\n")
    n, k = list_input[0].split(" ")
    rq, cq = list_input[1].split(" ")
    for input in list_input[2:]:
        coord = input.split(" ")
        obstacles["%s-%s" % (coord[0], coord[1])] = 0
    return "\n%d" % queensAttack(int(n) + 1, k, int(rq), int(cq), obstacles)


def queensAttack(n, k, rq, cq, obstacles):
    queen = [rq, cq]
    casillas = 0
    for y in reversed(range(1, queen[1])):
        if "%d-%d" % (queen[0], y) in obstacles:
            break
        else:
            casillas += 1
    for y in reversed(range(1, queen[1])):
        aux = queen[1] + (queen[0] - y)
        if "%d-%d" % (aux, y) in obstacles or aux >= n:
            break
        else:
            casillas += 1
    for x in range(queen[0] + 1, n):
        if "%d-%d" % (x, queen[1]) in obstacles:
            break
        else:
            casillas += 1
    for x in range(queen[0] + 1, n):
        aux = queen[1] + (x - queen[0])
        if "%d-%d" % (x, aux) in obstacles or aux >= n:
            break
        else:
            casillas += 1 
    for y in range(queen[1] + 1, n):
        if "%d-%d" % (queen[0], y) in obstacles:
            break
        else:
            casillas += 1 
    for y in range(queen[1] + 1, n):
        aux = queen[0] - (y - queen[1])
        if "%d-%d" % (aux, y) in obstacles or aux <= 0:
            break
        else:
            casillas += 1 
    for x in reversed(range(1, queen[0])):
        if "%d-%d" % (x, queen[1]) in obstacles:
            break
        else:
            casillas += 1 
    for x in reversed(range(1, queen[0])):
        aux = queen[1] - (queen[0] - x)
        if "%d-%d" % (x, aux) in obstacles or aux <= 0:
            break
        else:
            casillas += 1 
    return casillas
