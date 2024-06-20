import numpy as np

ROWS = 6
COLS = 7
COL_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 初始化空棋盤
def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

# 檢查是否可以下棋
def is_valid_move(board, col):
    return board[ROWS-1][col] == 0  # 最上面一格為 0 表示可以下棋

# 下棋
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# 檢查勝利條件
def winning_move(board, piece):
    # 檢查垂直連線
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # 檢查水平連線
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # 檢查主對角線（左上到右下）連線
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # 檢查次對角線（右上到左下）連線
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

# 主遊戲迴圈
def play_game():
    board = create_board()
    turn = 0  # 0 表示玩家1，1 表示玩家2
    game_over = False

    while not game_over:
        # 畫面顯示
        print(np.flip(board, 0))
        if turn == 0:
            col_str = input("玩家1選擇列 (A-G): ").upper()
        else:
            col_str = input("玩家2選擇列 (A-G): ").upper()

        if col_str in COL_NAMES:
            col = COL_NAMES.index(col_str)
            if is_valid_move(board, col):
                row = next_empty_row(board, col)
                drop_piece(board, row, col, turn + 1)

                if winning_move(board, turn + 1):
                    print(np.flip(board, 0))
                    print(f"玩家 {turn + 1} 勝利!")
                    game_over = True

                turn = (turn + 1) % 2  # 切換玩家
            else:
                print("這列已滿，請重新選擇。")
        else:
            print("請輸入有效的列名 (A-G)。")

    print("遊戲結束！")

# 找到下一個空行
def next_empty_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

if __name__ == "__main__":
    play_game()
