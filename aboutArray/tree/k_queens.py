# "K 皇后问题" 是经典的 "N 皇后问题" 的变种，它的目的是在一个 N x N 的棋盘上放置 K 个皇后，使得她们彼此不能攻击对方。皇后可以水平、垂直和对角线方向攻击，因此相互不能位于同一行、同一列或同一对角线上。

def solve_n_queens(k):
    def is_safe(board, row, col):
        # 检查当前行是否有皇后
        for c in range(col):
            if board[row][c]:
                return False

        # 检查左上方对角线
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[r][c]:
                return False

        # 检查左下方对角线
        for r, c in zip(range(row, k, 1), range(col, -1, -1)):
            if board[r][c]:
                return False

        return True

    def place_queen(board, col):
        if col >= k:
            # 所有皇后都已经放置完毕
            solutions.append([row[:] for row in board])
            return

        for row in range(k):
            if is_safe(board, row, col):
                board[row][col] = 1
                place_queen(board, col + 1)
                board[row][col] = 0  # 回溯

    solutions = []
    board = [[0 for _ in range(k)] for _ in range(k)]
    place_queen(board, 0)
    return solutions

# 示例使用
k = 8
solutions = solve_n_queens(k)
for solution in solutions:
    for row in solution:
        print(row)
    print("\n")