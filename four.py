

class Cell:
    def __init__(self):
        self.is_occupied = False # 専有されている
        self.player_symbol = None

    def put(self, symbol):
        if self.is_occupied == False:
            self.player_symbol = symbol
            self.is_occupied = True

class Stage:
    def __init__(self):
        self.width = 4
        self.height = 4
        self.cells = self.init_cells(self.width, self.height)

    def init_cells(self, width, height): # セルを作って、初期状態のステージを返す
        cells = [] # [00, 01, 02, 03, 10, 11, .., 33] # [[o, x, o, o], [2行目], [], []]
        for h in range(self.height): # h <- [0, 1, 2, ... self.height-1] = [0, 1, 2, 3]
            cells.append([])
            for w in range(self.width):
                cells[-1].append(Cell())
        return cells

    def put_symbol(self, symbol, x, y):
        if not self.check_valid_input(x,y): return None # 不正な入力値の場合は何もしない

        cell = self.cells[y][x]
        if cell.is_occupied == False:
            cell.put(symbol)

    def check_valid_input(self, x, y):  # 正しい入力値なら true , 間違っていれば false
        is_valid = 0 <= x and x < self.width and 0 <= y and y < self.height
        return is_valid

    def judge(self, symbol):
        arr = [[int(self.cells[y][x].player_symbol == symbol) for x in range(self.width)] for y in range(self.height)]

        # 行
        for y in range(self.height):
            row = arr[y]
            count = sum(row)
            if count == 4: return True

        # 列
        for x in range(self.width):
            column = [arr[y][x] for y in range(self.height)]
            count = sum(column)
            if count == 4: return True

        # 斜め
        diag = [arr[n][n] for n in range(self.height)]
        count = sum(diag)
        if count == 4: return True

        cdiag = [arr[self.height-1-n][n] for n in range(self.height)]
        count = sum(cdiag)
        if count == 4: return True

        return False

class FourGame:
    def __init__(self):
        self.width = 4
        self.height = 4
        self.player_num = 2
        self.player_symbols = ["o", "x"]
        self.current_player = 0 # 0 or 1
        self.stage = Stage()

    def do_turn(self, x, y): # symbol を置いて、勝った場合はTrue を返す
        is_valid = self.stage.check_valid_input(x, y)
        if (not is_valid):
            print("入力が正しくありません")
            return None

        symbol = self.player_symbols[self.current_player]
        self.stage.put_symbol(symbol, x, y)
        judged = self.stage.judge(symbol)
        self.current_player = (self.current_player+1) % self.player_num

        return judged

    def render(self):
        hline = "-" * (self.width*2 + 1)
        print(hline)
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                symbol = self.stage.cells[y][x].player_symbol
                if symbol is None: symbol = " "
                line += symbol + "|"
            print(line)
            print(hline)


game = FourGame()
is_continue = True
while is_continue:
    x, y = [int(num) for num in input("x, y: ").split(",")]
    is_win = game.do_turn(x, y)
    game.render()
    is_continue = not is_win
