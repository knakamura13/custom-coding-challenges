import utils


class Solution:
    def __init__(self, _input):
        self.input = _input

    def solve_problem(self):
        """Solution: O(n * m) time, O(n * m) space."""
        n = len(self.input)
        source_coord = 0, 0
        connected_sinks = set()

        # Construct a 2D matrix from the input list containing chars and their coordinates
        grid = [[' ' for _ in range(n)] for _ in range(n)]
        for char, (x, y) in self.input:  # Note: input coords list x before y
            grid[y][x] = char
            if utils.is_char_source(char):
                source_coord = y, x

        # Perform BFS on the grid, starting at the source
        # Any sinks that can be reached using BFS must be connected to the source, so append them to connected_sinks
        queue = [source_coord]
        visited = set()
        while queue:
            curr_coord = queue.pop(0)

            if curr_coord in visited:
                continue

            visited.add(curr_coord)
            char = grid[curr_coord[0]][curr_coord[1]]

            if utils.is_char_sink(char):
                connected_sinks.add(char)

            directions = utils.get_cell_opening_directions_for_char(char)
            for direction in directions:
                next_coord = utils.get_next_coord_in_direction(curr_coord, direction)
                next_y, next_x = next_coord
                if (next_coord != curr_coord
                        and next_coord not in visited
                        and 0 <= next_y < n
                        and 0 <= next_x < n
                        and grid[next_y][next_x] != ' '):
                    queue.append(next_coord)

        return ''.join(sorted(connected_sinks))
