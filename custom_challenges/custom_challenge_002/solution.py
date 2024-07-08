import utils


class Solution:
    def __init__(self, _input):
        self.input = _input
        n = len(self.input)

        # Construct the 2D matrix from the input list containing chars and their coordinates
        self.grid = [[' ' for _ in range(n)] for _ in range(n)]
        for char, (x, y) in self.input:
            self.grid[y][x] = char

        utils.visualize_matrix(self.grid)

    def solve_problem(self):
        """Solution: O(n * m) time, O(n * m) space."""
        # Temp: return all the sinks even if they aren't connected to the source
        connected_sinks = [char[0] if 65 <= ord(char[0]) <= 90 else '' for char, coord in self.input]

        return ''.join(sorted(connected_sinks))
