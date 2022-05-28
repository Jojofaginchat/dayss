with open('input.txt') as f:
    N, M = map(int, f.readline().split())
    grid = []
    for i in range(N):
        grid.append(f.readline()[:-1])
    coord = []
    for j in range(1, N - 1):
        for i in range(1, M - 1):
            if grid[j][i] == '#':
                if grid[j][i + 1] == '#':
                    if grid[j - 1][i + 1]:
                        coord.append([(i + 1, j), (i + 1, j - 1)])
                    elif grid[j + 1][i + 1]:
                        coord.append([(i + 1, j), (i + 1, j + 1)])

                elif grid[j + 1][i] == '#':
                    if grid[j + 1][i + 1] == '#':
                        coord.append([(i, j + 1), (i + 1, j + 1)])
                    elif grid[j + 1][i - 1] == '#':
                        coord.append([(i, j + 1), (i - 1, j + 1)])

                elif grid[j][i - 1] == '#':
                    pass
                elif grid[j - 1][i] == '#':
                    pass
        print(coord)
