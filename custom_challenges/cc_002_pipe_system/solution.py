def solve_problem(input_file_path: str = 'input.txt') -> str:
    def is_char_source(_char: str) -> bool:
        """Returns True if the character is a valid source (i.e., asterisk character *)."""
        return _char == '*'

    def is_char_sink(_char: str) -> bool:
        """Returns True if the character is a valid sink (i.e., characters [A-Z])."""
        return 65 <= ord(_char[0]) <= 90

    def get_cell_opening_directions_for_char(_char: str) -> list[str]:
        """Returns all the pipe opening directions for a given character (i.e., 'up, 'right', 'down', and/or 'left')."""
        if is_char_source(_char) or is_char_sink(_char):
            return ['up', 'right', 'down', 'left']

        if _char == '═':
            return ['right', 'left']
        elif _char == '║':
            return ['up', 'down']
        elif _char == '╔':
            return ['right', 'down']
        elif _char == '╗':
            return ['down', 'left']
        elif _char == '╚':
            return ['up', 'right']
        elif _char == '╝':
            return ['up', 'left']
        elif _char == '╠':
            return ['up', 'right', 'down']
        elif _char == '╣':
            return ['up', 'down', 'left']
        elif _char == '╦':
            return ['right', 'down', 'left']
        elif _char == '╩':
            return ['up', 'right', 'left']

        return []

    def get_next_coord_in_direction(_coord: tuple[int, int], _direction: str) -> tuple[int, int]:
        """Returns the coordinate of the neighboring cell in the given direction."""
        _y, _x = _coord

        if _direction == 'up':
            return _y - 1, _x
        elif _direction == 'right':
            return _y, _x + 1
        elif _direction == 'down':
            return _y + 1, _x
        elif _direction == 'left':
            return _y, _x - 1

        return _coord

    f = open(input_file_path, 'r')
    lines = f.readlines()
    n = len(lines)
    source_coord = 0, 0
    connected_sinks = set()

    # Construct a 2D matrix from the input list containing chars and their coordinates
    grid = [[' ' for _ in range(n)] for _ in range(n)]
    for line in lines:
        char, x, y = line.split(' ')
        x, y = int(x), int(y)
        grid[y][x] = char
        if is_char_source(char):
            source_coord = y, x

    # Perform BFS on the grid starting from the source (*) character
    queue = [source_coord]
    visited = set()
    while queue:
        # Explore the next unexplored coordinate in the queue
        curr_coord = queue.pop(0)

        # Ensure a coordinate is never explored twice to prevent infinite loops
        if curr_coord in visited:
            continue

        visited.add(curr_coord)
        char = grid[curr_coord[0]][curr_coord[1]]

        # The BFS run has reached a sink, so append the sink to the list of connected sinks
        if is_char_sink(char):
            connected_sinks.add(char)

        # Look in all the directions that can be explored from the current coordinate,
        # appending each accessible neighboring coordinate to the queue to be explored later
        directions = get_cell_opening_directions_for_char(char)
        for direction in directions:
            next_coord = get_next_coord_in_direction(curr_coord, direction)
            if (next_coord != curr_coord
                    and next_coord not in visited
                    and 0 <= next_coord[0] < n
                    and 0 <= next_coord[1] < n
                    and grid[next_coord[0]][next_coord[1]] != ' '):
                queue.append(next_coord)

    # Return the sorted list of connected sinks as a string
    return ''.join(sorted(connected_sinks))


if __name__ == '__main__':
    answer = solve_problem()
    assert answer == 'ACDEGHIJKLMNOPQTUVWXYZ'
    print('PASSED: answer =', answer)
