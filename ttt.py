tic_tac_toe = [0 for i in range(9)]
lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
line_values = [0 for i in range(8)]
user_char = {1: "O", -1: "X", 0: "_"} # 3 состояния ячейки - нет хода, сходил юзер, сходил комп. 
turn = -1 # по умолчанию юзер ходит крестом и = -1


def game():
        global user_char, turn
        if input("Хочешь ли ты, чтобы ИИ ходил первым ? (Y - да / Any Key - нет) ").lower() == "y":
            user_char = {1:"X", -1:"O", 0:"_"}
            turn = 1
        display()
        while not has_winner():
            if 0 in tic_tac_toe:
                next_move(turn)
                turn *= -1
                display()
            else:
                print("Ничья !!!😑")
                break

def has_winner():
    if max(line_values) == 3:
        print("Я выиграл!!!😎")
        return True
    elif min(line_values) == -3:
        print("Ты выиграл!!!😢")
        return True

def next_move(turn):
        if turn == -1: # Ход юзера
            print("Твой ход (" + user_char[-1] + "): ")
            while not is_user_move_successful(input("Делай свой ход: ")):
                print("Не туда ходишь, сходи ещё раз... ")
        else: # Ход компа
            print("Мой ход: ")
            for line_value in [2, -2, -1, 1, 0]:
                cell = find_most_valuable_cell(line_value)
                if cell >= 0: # нашёл клетку для размещения
                    mark_cell(cell, turn)
                    print ("Выбираю клетку", str(cell))
                    return

def is_user_move_successful(user_input):
        s = list(user_input)[0]
        if '012345678'.find(s) >= 0 and tic_tac_toe[int(s)] == 0:
            mark_cell(int(s), turn)
            return True

def find_most_valuable_cell(line_value):
        if set(tic_tac_toe) == {0}:
            return 1
        all_lines = [i for i in range(8) if line_values[i] == line_value]
        all_cells = [j for line in all_lines for j in lines[line] if tic_tac_toe[j] == 0]
        cell_frequency = dict((c, all_cells.count(c)) for c in set(all_cells))
        if len(cell_frequency) > 0:
            return max(cell_frequency, key=cell_frequency.get)
        else:
            return -1

def mark_cell(cell, turn):
        global line_values, tic_tac_toe
        tic_tac_toe[cell] = turn
        line_values = [sum(cell_value) for line in lines for cell_value in [[tic_tac_toe[j] for j in line]]]

def display():
        print(' _ _ _\n' + ''.join('|' + user_char[tic_tac_toe[i]] + ('|\n' if i % 3 == 2 else '') for i in range(9)))
        
def rules():
        print(""" 
        Игра крестики-нолики.
        Инструкция: номера ячеек имеют следующий порядок:
                         _ _ _
                        |0|1|2|
                        |3|4|5|
                        |6|7|8|
        На каждом ходе пользователь вводит одно число, соответствующее номеру незаполненной ячейки.
        Если пользователь тупой, ИИ говорит ему, чтобы он сходил ещё раз и правильно.
        Игра заканчивается победой, когда один из игроков наберёт 3 совпадения по одной из 8 линий,
        либо ничьей, когда совпадений нет. Пользователю дано право выбора первого хода.
        """)

rules()
game()