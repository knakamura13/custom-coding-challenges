class Solution:
    def __init__(self, _input):
        self.input = _input

    def solve_problem(self):
        """Solution: O(n) time, O(1) space."""
        S = self.input

        if len(S) < 3:
            return 'tie'

        x_flag, o_flag = False, False
        slow, fast = 0, 3

        for i in range(len(S)):
            window = S[slow:fast]

            if 'X' not in window:
                o_flag = True
            elif 'O' not in window:
                x_flag = True

            if fast >= len(S):
                break

            slow += 1
            fast += 1

        if x_flag and not o_flag:
            return 'X'
        elif o_flag and not x_flag:
            return 'O'

        return 'tie'
