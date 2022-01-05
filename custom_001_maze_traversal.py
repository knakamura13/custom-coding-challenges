"""
    Custom Challenge #001: Maze Traversal

    SUMMARY
    Traverse a maze from start to finish.

    DETAILS
    A maze is represented by a 2D array of strings and may contain the following values:
        'S': Start
        'E': Finish
        'X': Wall/Obstacle
        ' ': Empty Space
    A move is a traversal by one row or one column in the following directions:
        Up, Right, Down, or Left
    Moves will be prioritized in the following order: 
        Up, Right, Down, Left

    EXAMPLE #1
    Input:
        X X X X X X X
        X   X X   S X
        X           X
        X       X   X
        X X X   X X X
        X         E X
        X X X X X X X

    Output:
        [(1, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)]
        OR
        [(1, 5), (1, 4), (2, 4), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)]

    Explanation:
        The solution can be seen below, where the dots (•) represent the shortest path from start to finish:
              0 1 2 3 4 5 6
            0 X X X X X X X
            1 X   X X   S X
            2 X     • • • X
            3 X     • X   X
            4 X X X • X X X
            5 X     • • • X
            6 X X X X X X X
"""
####################
# Global Variables #
####################

# Global list containing the final result of the recursive DFS algorithm.
# Note: Unable to return the value from the recursive function for unknown reason.
dfs_path = []

# Global list containing the legal moves from a given coordinate, ordered by priority (up, right, down, left).
directions = [
    [-1, 0],  # Up
    [0, 1],  # Right
    [1, 0],  # Down
    [0, -1]  # Left
]


##############
# Test Cases #
##############

def example_1():
    maze = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', 'X', 'X', ' ', 'S', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', 'X', ' ', 'X'],
        ['X', 'X', 'X', ' ', 'X', 'X', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'E', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    start = 1, 5
    solutions = [
        [(1, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)],
        [(1, 5), (1, 4), (2, 4), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)]
    ]
    return maze, start, solutions


################
# DFS Solution #
################

def solution_dfs(maze, start):
    global dfs_path

    h = len(maze)
    if not h:
        return
    w = len(maze[0])

    visited = [
        [False for _ in range(w)]
        for _ in range(h)
    ]
    dfs(maze, start[0], start[1], [], visited)

    return dfs_path


def dfs(maze, row, col, path, visited):
    global dfs_path, directions

    h, w = len(maze), len(maze[0])
    val = maze[row][col]

    invalid_row = row < 0 or row >= h
    invalid_col = col < 0 or col >= w
    invalid_val = val == 'X'
    if invalid_row or invalid_col or invalid_val or visited[row][col]:
        return

    visited[row][col] = True
    path.append((row, col))
    if val == 'E':
        dfs_path = path
        return

    for _y, _x in directions:
        dfs(maze, row + _y, col + _x, path.copy(), visited)


################
# BFS Solution #
################

def solution_bfs(maze, start):
    queue = [[start]]
    h, w = len(maze), len(maze[0])
    visited = [
        [False for _ in range(w)]
        for _ in range(h)
    ]

    while queue:
        path = queue.pop(0)
        y, x = path[-1]
        val = maze[y][x]

        if val == 'E':
            return path

        for _y, _x in directions:
            row, col = y + _y, x + _x

            invalid_row = row < 0 or row >= h
            invalid_col = col < 0 or col >= w
            invalid_val = val == 'X'
            if invalid_row or invalid_col or invalid_val or visited[row][col]:
                continue

            queue.append(path + [(row, col)])
            visited[row][col] = True


################
# Main Program #
################

def main():
    # Define which test cases to run
    tests = [example_1]

    # Define which solution to use for testing
    solution = solution_bfs

    # Execute the tests and print the results
    for i, test in enumerate(tests):
        test_maze, test_start, test_solutions = test()
        solution_output = solution(test_maze, test_start)

        # Test all possible solutions for the current test
        result = 'PASS' if solution_output in test_solutions else 'FAIL'

        # Print the results for the current test
        print(f'Test #{i + 1}: {result}')


if __name__ == '__main__':
    # Execute the main program
    main()
