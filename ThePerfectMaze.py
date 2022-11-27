import requests as requests

CELL_CONTENT_POS = 9
RED_COLOR = "\033[0;31m"
END_COLOR = "\033[0m"


def get_url(x, y):
    """
    Returns a URL of type https://hackeps2022.herokuapp.com/maze?x=1&y=2,
    for the given values for x and y.
    """
    URL = "https://hackeps2022.herokuapp.com/maze?"
    return URL + "x=" + str(x) + "&" + "y=" + str(y)


def get_cell_content(url):
    """
    Returns a string with the content of the cell given by the provided url.
    """
    cell_content = requests.get(url=url).text[CELL_CONTENT_POS]
    if cell_content != '#':
        cell_content = RED_COLOR + cell_content + END_COLOR
    return cell_content


def get_maze_len():
    """
    Looks through the maze cells in one row, to find the first one out of the
    maze range. This limit is shown with the cell content "{"error":"You are out of the map or the coordinates are not valid"}".
    Then returns the maze maximum size.
    """
    y = 0
    while True:
        current_url = get_url(0, y)
        cell_txt = requests.get(url=current_url).text
        if cell_txt == "{\"error\":\"You are out of the map or the coordinates are not valid\"}":
            break
        y += 1

    return y - 1


def print_maze():
    """
    Computes the content for each cell of the maze and prints the maze.
    """
    maze = []
    for x in range(N):
        row_list = []
        maze.append(row_list)
        for y in range(N):
            current_url = get_url(x, y)
            cell_content = get_cell_content(current_url)
            row_list.append(cell_content)

        print(' '.join(row_list))


if __name__ == '__main__':
    N = get_maze_len()
    print(N)
    print_maze()
