def read_test_cases(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        test_cases = content.split('\n\n')
        return test_cases

def parse_test_case(test_cases):
    lines = test_cases.split('\n')
    size = tuple(map(int, lines[0].split(',')))
    grid = [list(map(int, line)) for line in lines[1:]]
    return size, grid

def run_test_cases(file_path):
    test_cases = read_test_cases(file_path)
    for test_case in test_cases:
        size, grid = parse_test_case(test_case)
        print(f"Size: {size}")
        print("Grid:")
        for row in grid:
            print(row)
        color_groups = flood_fill(grid)
        print(f"# of color groups: {len(color_groups)}")
        for group in color_groups:
            if len(group) <= 2:
                continue
            group = filtered_gems(group) 
            if len(group) > 0:
                print(group)
                draw_group(group)
                print(' ')

def flood_fill(grid):
    cols = len(grid[0])
    rows = len(grid)
    visited = [[False] * cols for _ in range(rows)]
    color_groups = []

    def dfs(x, y, color):
        if x < 0 or x >= cols or y < 0 or y >= rows or visited[y][x] or grid[y][x] != color:
            return
        visited[y][x] = True
        color_group.append((x,y))
        dfs(x-1, y, color)
        dfs(x+1, y, color)
        dfs(x, y-1, color)
        dfs(x, y+1, color)

    for j in range(rows):
        for i in range(cols):
            if not visited[j][i]:
                color_group = []
                dfs(i, j, grid[j][i])
                color_groups.append(color_group)
    return color_groups

def is_valid_element(group, x, y):
    count = 1
    for dx in [-1, 1]:
        nx = x + dx
        while (nx, y) in group:
            count += 1
            nx += dx
    if count >= 3:
        return True
    count = 1
    for dy in [-1, 1]:
        ny = y + dy
        while (x, ny) in group:
            count += 1
            ny += dy
    if count >= 3:
        return True
    return False

def filtered_gems(group):
    filtered = []
    for x, y in group:
        if is_valid_element(group, x, y):
            filtered.append((x,y))
    return filtered

def draw_group(group):
    if len(group) == 0:
        return
    rows = max(y for x, y in group)+1
    cols = max(x for x, y in group)+1
    for j in range(0, rows):
        r_ = []
        for i in range(0, cols):
            if (i,j) in group:
                r_.append(1)
            else:
                r_.append(0)
        print(r_)


if __name__ == "__main__":
    run_test_cases('./test.txt')
