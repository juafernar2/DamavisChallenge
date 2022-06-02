# Juan Alfonso Fernández Naranjo
# No estoy seguro de si se puede utilizar la librería numpy, así que no la utilizo

def possible_mov(move: int, sneak: list, board: list) -> bool:
    # 0 -> R; 1 -> L; 2 -> U; "3" -> D
    head = sneak[-1]

    if move == 0:
        return ([head[0]+1, head[1]] not in sneak[1:-1]) and (head[0]+1 < board[0])
    elif move == 1:
        return ([head[0]-1, head[1]] not in sneak[1:-1]) and (head[0]-1 >= 0)
    elif move == 2:
        return ([head[0], head[1]+1] not in sneak[1:-1]) and (head[1]+1 < board[1])
    else:
        return ([head[0], head[1]-1] not in sneak[1:-1]) and (head[1]-1 >= 0)


def make_move(move: int, way: list, current_depth: int, len_snake: int) -> list:
    head = way[len_snake - 1 + current_depth]

    if move == 0:
        way[len_snake + current_depth] = [head[0]+1, head[1]]
    elif move == 1:
        way[len_snake + current_depth] = [head[0]-1, head[1]]
    elif move == 2:
        way[len_snake + current_depth] = [head[0], head[1]+1]
    else:
        way[len_snake + current_depth] = [head[0], head[1]-1]
    return way


def recursive_transformation(board: list, depth: int, len_snake: int, way: list, movements: list, current_depth: int,
                             count: int) -> tuple:
    if current_depth != depth:
        while movements[current_depth] < 4:
            if possible_mov(movements[current_depth], way[current_depth:current_depth + len_snake], board):
                way = make_move(movements[current_depth], way, current_depth, len_snake)
                count, way, movements, current_depth = recursive_transformation(board, depth, len_snake, way, movements,
                                                                                current_depth + 1, count)
            else:
                movements[current_depth] += 1

        way[len_snake + current_depth] = [0, 0]
        movements[current_depth] = 0

        if current_depth != 0:
            movements[current_depth - 1] += 1
        return count, way, movements, current_depth - 1

    else:
        movements[current_depth - 1] += 1
        return count + 1, way, movements, current_depth - 1


def num_paths(board: list, snake: list, depth: int) -> int:
    len_snake = len(snake)
    movements = [0] * depth
    snake.reverse()
    way = snake + [[0, 0]] * depth

    return recursive_transformation(board, depth, len_snake, way, movements, 0, 0)[0]


if __name__ == '__main__':
    test_board = [10, 10]
    test_snake = [[5, 5], [5, 4], [4, 4], [4, 5]]
    test_depth = 4

    print(num_paths(test_board, test_snake, test_depth))