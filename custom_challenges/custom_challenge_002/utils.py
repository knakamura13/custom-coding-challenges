pipe_shapes = '═', '║', '╔', '╗', '╚', ' ╝', '╠', '╣', '╦', '╩'


def visualize_grid(grid: list[list[str]]):
    print()
    for row in grid:
        print(''.join(row))


def is_char_source(char: str) -> bool:
    """Returns True if the character is a valid source (i.e., asterisk character *)."""
    return char == '*'


def is_char_sink(char: str) -> bool:
    """Returns True if the character is a valid sink (i.e., characters [A-Z])."""
    return 65 <= ord(char[0]) <= 90


def is_char_pipe(char: str) -> bool:
    """Returns True if the character is a valid pipe shape."""
    return char in pipe_shapes


def get_cell_opening_directions_for_char(char: str) -> list[str]:
    """Returns all the pipe opening directions for a given character (i.e., 'up, 'right', 'down', and/or 'left')."""
    if is_char_source(char) or is_char_sink(char):
        return ['up', 'right', 'down', 'left']

    if char == '═':
        return ['right', 'left']
    elif char == '║':
        return ['up', 'down']
    elif char == '╔':
        return ['right', 'down']
    elif char == '╗':
        return ['down', 'left']
    elif char == '╚':
        return ['up', 'right']
    elif char == '╝':
        return ['up', 'left']
    elif char == '╠':
        return ['up', 'right', 'down']
    elif char == '╣':
        return ['up', 'down', 'left']
    elif char == '╦':
        return ['right', 'down', 'left']
    elif char == '╩':
        return ['up', 'right', 'left']

    return []


def get_next_coord_in_direction(coord: tuple[int, int], direction: str) -> tuple[int, int]:
    y, x = coord

    if direction == 'up':
        return y - 1, x
    elif direction == 'right':
        return y, x + 1
    elif direction == 'down':
        return y + 1, x
    elif direction == 'left':
        return y, x - 1

    return coord
